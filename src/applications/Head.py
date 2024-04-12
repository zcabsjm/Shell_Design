from . import Application


class Head(Application.Application):
    def exec(self, args, input, output):
        if len(args) == 0:
            num_lines = 10
            file = input
        elif len(args) == 1:
            num_lines = 10
            file = open(args[0])
        elif len(args) == 3:
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = open(args[2])
        else:
            raise ValueError("wrong number of command line arguments")

        if num_lines <= 0:
            return

        cnt = 0
        for line in file:
            output.write(line)
            cnt += 1

            if cnt >= num_lines:
                break
