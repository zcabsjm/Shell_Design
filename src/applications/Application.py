from abc import ABC, abstractmethod


class Application(ABC):
    def __init__(self):
        self._unsafe = False

    @abstractmethod
    def exec(self, args, input, output):
        pass

    def set_is_unsafe(self, unsafe):
        self._unsafe = unsafe

    def is_unsafe(self):
        return self._unsafe
