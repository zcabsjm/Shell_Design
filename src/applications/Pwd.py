import os
from . import Application


class Pwd(Application.Application):
    def exec(self, args, input, output):
        output.write(os.getcwd() + "\n")
