import re
from . import Application


class Grep(Application.Application):
    def exec(self, args, input, output):
        if len(args) < 1:
            raise ValueError("wrong number of command line arguments")

        pattern = args[0]

        if len(args) > 1:
            files = [open(x) for x in args[1:]]
        else:
            files = [input]

        for i, file in enumerate(files):
            for unparsed_line in file:
                for line in unparsed_line.split("\n"):

                    if re.search(pattern, line):
                        if len(files) > 1:
                            output.write(f"{args[1 + i]}:{line}\n")
                        else:
                            output.write(line + "\n")
