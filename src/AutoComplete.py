import readline
from glob import glob
import os


class AutoComplete:
    def __init__(self):
        self.commands = [
            "cat",
            "cd",
            "cut",
            "echo",
            "find",
            "grep",
            "head",
            "ls",
            "pwd",
            "sort",
            "tail",
            "uniq"
        ]

    def complete(self, last_word, index):
        if self._look_for_files(readline.get_line_buffer()):
            return self._get_matching_files(index)

        return self._get_matching_commands(last_word, index)

    # if space exists in current line we want to match files
    # rather than commands
    def _look_for_files(self, current_buffer):
        return current_buffer.count(' ') >= 1

    def _get_matching_files(self, index):
        last_word = readline.get_line_buffer().split(' ')[-1]
        file_start = last_word + '*'
        matches = glob(file_start)

        if index < len(matches):
            match = matches[index]
            if os.path.isdir(match):
                return match.split('/')[-1] + '/'
            return match.split('/')[-1]

    def _get_matching_commands(self, last_word, index):
        matches = [x for x in self.commands if x.startswith(last_word)]
        if index < len(matches):
            return matches[index]
