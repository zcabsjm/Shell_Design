from . import Application


class Uniq(Application.Application):
    def exec(self, args, input, output):
        caseSensitive = True
        file = input

        if len(args) == 0:
            pass
        elif len(args) == 1:
            if args[0] == "-i":
                caseSensitive = False
            else:
                file = open(args[0])
        elif len(args) == 2:
            if args[0] != "-i":
                raise ValueError("wrong flags")
            else:
                caseSensitive = False
                file = open(args[1])
        else:
            raise ValueError("wrong number of command line arguments")

        lastLine = None

        for line in file:
            if lastLine is not None and caseSensitive and line == lastLine:
                continue

            if (
                lastLine is not None
                and not caseSensitive
                and line.casefold() == lastLine.casefold()
            ):
                continue

            output.write(line)
            lastLine = line
