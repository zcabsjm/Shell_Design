from . import Application
import fnmatch
import os


class Find(Application.Application):
    def exec(self, args, input, output):
        dir = "."
        pattern = ""

        if len(args) == 2:
            if args[0] != "-name":
                raise ValueError("command line arguments are incorrect")
            pattern = args[1]
        elif len(args) == 3:
            if args[1] != "-name":
                raise ValueError("command line arguments are incorrect")
            dir = args[0]
            pattern = args[2]
        else:
            raise ValueError("wrong number of command line arguments")

        for path, dirlist, filelist in os.walk(dir):
            for name in fnmatch.filter(filelist, pattern):
                output.write(os.path.join(path, name))
