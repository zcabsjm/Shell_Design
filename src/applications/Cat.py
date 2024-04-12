from . import Application


class Cat(Application.Application):

    def exec(self, args, input, output):
        concatenated = ""

        for a in args:
            with open(a) as f:
                concatenated += f.read()

        if len(args) == 0:
            for line in input:
                concatenated += line

        if len(concatenated) > 0:
            output.write(concatenated)
