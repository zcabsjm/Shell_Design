import sys
import os
from collections import deque
from glob import glob
from Output import Output
from Input import Input
from Factory import Factory
from AutoComplete import AutoComplete
from lark import Lark, Token
from AutoComplete import readline

parser = Lark(
    """
    start        : command
    command      : pipe | _seq | call
    pipe         : call "|" call | pipe "|" call
    _seq          : command ";" command
    quoted       : single_quoted | double_quoted | backquoted
    unquoted     : /[^ \t "'`;|<>]+/
    single_quoted: "'" /[^']+/ "'"
    backquoted   : "`" /[^`]+/ "`"
    double_quoted: /"/ ( backquoted |  /[^"`]+/ )* /"/
    _whitespace   : (" " | /\t/ )+
    call         : [ _whitespace ] [ redirection _whitespace ]* \
    argument [ _whitespace _atom ]* [ _whitespace ]
    _atom         : redirection | argument
    argument     : ( quoted | unquoted )+
    !redirection  : "<" [ _whitespace ] argument
                 | ">" [ _whitespace ] argument
                     """,
)


def run_command(app, args, curr_input, output):
    try:
        application = Factory(app)
        application.exec(args, curr_input, output)
    except ModuleNotFoundError:
        raise
    except Exception as e:
        if application.is_unsafe():
            output.write("Unexpected error: " + str(e) + "\n")
        else:
            raise


def parse_argument(arg_tree):
    ret = ""
    for ch in arg_tree.children:
        if ch.data == "unquoted":
            ret += ch.children[0]
        else:
            quoted = ch.children[0]
            quoted_arg = ""
            if quoted.data == "single_quoted":
                quoted_arg += quoted.children[0]
            elif quoted.data == "double_quoted":
                for arg in quoted.children[1:-1]:
                    if isinstance(arg, Token):
                        quoted_arg += arg
                    else:  # backquoted
                        output = Output(deque())
                        eval_command_line(arg.children[0], output)
                        quoted_arg += (
                            "".join([item.replace("\n", " ")
                                     for item in output])
                        ).strip()
            else:
                output = Output(deque())
                eval_command_line(quoted.children[0], output)
                if len(arg_tree.children) == 1:
                    return [item.replace("\n", " ").strip() for item in output]

                quoted_arg += (
                    "".join([item.replace("\n", " ") for item in output])
                ).strip()

            ret += quoted_arg.replace("*", r"\\*")

    globbing = glob(ret)
    if globbing:
        return globbing
    else:
        return [ret.replace(r"\\*", "*")]


def redirect_io(redirection_tree, input, out):
    if redirection_tree.children[0] == "<":
        if input.redirected:
            raise ValueError("wrong number of IO redirections")

        input.redirect(open(
            parse_argument(redirection_tree.children[1])[0],
            "r"))
    else:
        if out.redirected:
            raise ValueError("wrong number of IO redirections")

        out.redirect(open(
            parse_argument(redirection_tree.children[1])[0],
            "w+"))


def eval_call(cmd_tree, curr_input, out):
    tokens = []
    for ch in cmd_tree.children:
        if ch is None:
            continue
        elif ch.data == "redirection":
            redirect_io(ch, curr_input, out)
        else:  # ch.data == argument
            tokens.extend(parse_argument(ch))

    app, args = tokens[0], tokens[1:]

    run_command(app, args, curr_input, out)


def eval_pipe(cmd_tree, input, out):
    output = Output(deque())
    if cmd_tree.children[0].data == "pipe":
        eval_pipe(cmd_tree.children[0], input, output)
        output.pipe(input)
    else:
        eval_call(cmd_tree.children[0], input, output)
        output.pipe(input)

    eval_call(cmd_tree.children[1], input, out)


def eval_command(cmd_tree, out):
    output = Output(deque())

    if cmd_tree.data == "pipe":
        eval_pipe(cmd_tree, Input(sys.stdin), output)
    elif cmd_tree.data == "call":
        eval_call(cmd_tree, Input(sys.stdin), output)
    elif cmd_tree.data == "command":
        for ch in cmd_tree.children:
            eval_command(ch, out)

    piped_input = Input(deque())
    output.pipe(piped_input)

    for line in piped_input:
        out.write(line)


def eval_command_line(cmd, out):
    global parser

    tree = parser.parse(cmd)

    eval_command(tree.children[0], out)


if __name__ == "__main__":
    auto_complete = AutoComplete()
    readline.set_completer(auto_complete.complete)
    readline.parse_and_bind("tab: complete")

    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")

        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")

        out = Output(deque())
        eval_command_line(sys.argv[2], out)
        out.print(end="")
    else:
        while True:
            cmdline = input(os.getcwd() + "> ")
            out = Output(deque())
            eval_command_line(cmdline, out)
            out.print(end="")
