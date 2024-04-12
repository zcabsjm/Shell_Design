class Output:
    def __init__(self, outputStream):
        self.output = outputStream
        self.redirected = False

    def __iter__(self):
        return (t for t in self.output)

    def redirect(self, redirectFile):
        self.outputRedirect = redirectFile
        self.redirected = True

    def write(self, line):
        for subline in line.split("\n"):
            if subline:
                self.output.append(subline + "\n")

    def print(self, end=""):
        for line in self.output:
            if hasattr(self, "outputRedirect"):
                self.outputRedirect.write(line)
            else:
                print(line, end=end)

    def pipe(self, input):
        if hasattr(self, "outputRedirect"):
            for line in self.output:
                self.outputRedirect.write(line)
        else:
            input.input = self.output
