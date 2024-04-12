import unittest

from applications.Uniq import Uniq
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestUniq(unittest.TestCase):
    def setUp(self):
        set_up_files()
        uniq = Uniq()
        self.exec = uniq.exec

    def test_uniq_with_two_arg(self):
        output, curr_input, args, result = initialize_test_values()
        args = ["-i", "dir1/file2.txt"]
        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["bbb\n", "aa\n", "ddd\n", "cc\n"])

    def test_uniq_one_arg(self):
        output, curr_input, args, result = initialize_test_values()
        args = ["dir1/file2.txt"]
        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["bbb\n", "aa\n", "ddd\n", "cc\n"])

    def test_uniq_stdin(self):
        output, curr_input, args, result = initialize_test_values()

        curr_input = open("dir1/file2.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["bbb\n", "aa\n", "ddd\n", "cc\n"])

    def test_uniq_case_insensitive_stdin(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-i"]

        curr_input = open("dir1/file2.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["bbb\n", "aa\n", "ddd\n", "cc\n"])

    def test_uniq_with_wrong_flag_should_throw_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-t", "dir1/file2.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_uniq_with_too_many_files_should_throw_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-i", "dir1/file2.txt", "file2.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
