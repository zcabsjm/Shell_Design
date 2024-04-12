import os
from . import Application


class Cd(Application.Application):
    def exec(self, args, input, output):
        if len(args) == 0 or len(args) > 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(args[0])
