from . import Application


class Sort(Application.Application):
    def exec(self, args, input, output):
        file = input
        reverse = False

        if len(args) == 0:
            pass
        elif len(args) == 1:
            if args[0] == "-r":
                reverse = True
            else:
                file = open(args[0])
        elif len(args) == 2:
            if args[0] != "-r":
                raise ValueError("Invalid arguments")

            reverse = True
            file = open(args[1])
        else:
            raise ValueError("Wrong number of command line arguments")

        lines = sorted(file.readlines(), reverse=reverse)
        for line in lines:
            output.write(line)
