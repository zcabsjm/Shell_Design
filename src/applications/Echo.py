from . import Application


class Echo(Application.Application):
    def exec(self, args, input, output):
        output.write(" ".join(args) + "\n")
