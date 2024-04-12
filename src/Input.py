class Input:
    def __init__(self, inputStream):
        self.input = inputStream
        self.redirected = False

    def __iter__(self):
        return (t for t in self.input)

    def redirect(self, otherInput):
        self.input = otherInput
        self.redirected = True

    def readlines(self):
        return [t for t in self.input]
