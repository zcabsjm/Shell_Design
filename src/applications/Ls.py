import os
from os import listdir
from . import Application


class Ls(Application.Application):
    def exec(self, args, input, output):
        if len(args) == 0:
            ls_dir = os.getcwd()
        elif len(args) > 1:
            raise ValueError("wrong number of command line arguments")
        else:
            ls_dir = args[0]

        for f in listdir(ls_dir):
            if not f.startswith("."):
                output.write(f + "\n")
