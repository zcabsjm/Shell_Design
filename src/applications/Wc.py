from . import Application


class Wc(Application.Application):
    def exec(self, args, input, output):
        show_all = True
        show_lines = False
        show_words = False
        show_characters = False

        inputs = []

        for arg in args:
            if arg == "-l":
                show_lines = True
                show_all = False
            elif arg == "-m":
                show_characters = True
                show_all = False
            elif arg == "-w":
                show_words = True
                show_all = False
            else:
                inputs.append(open(arg))

        if len(inputs) == 0:
            inputs.append(input)

        lines = []
        for file in inputs:
            lines.extend(file.readlines())

        line_cnt = len(lines)
        word_cnt = sum([len(line.split()) for line in lines])
        chr_cnt = sum([len(line) for line in lines])

        if show_all:
            output.write(f"{line_cnt} {word_cnt} {chr_cnt}\n")
        else:
            out = ""
            if show_lines:
                out += str(line_cnt) + " "
            if show_words:
                out += str(word_cnt) + " "
            if show_characters:
                out += str(chr_cnt) + " "

            output.write(out[:-1] + "\n")
