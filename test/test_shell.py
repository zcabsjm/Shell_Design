import unittest

from shell import eval_command_line
from Output import Output
from collections import deque

from utils.set_up_files import set_up_files


class TestShell(unittest.TestCase):
    def setUp(self):
        set_up_files()

    def test_cat_with_one_arg(self):
        out = Output(deque())
        eval_command_line("cat file1.txt", out)

        result = [line for line in out]

        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_exception_on_wrong_application(self):
        out = Output(deque())

        self.assertRaises(ModuleNotFoundError, eval_command_line,
                          "randomapp file1.txt", out)

    def test_correct_arg_parsing(self):
        out = Output(deque())
        eval_command_line("echo a'bc'd", out)

        result = [line for line in out]

        self.assertEqual(result, ["abcd\n"])

    def test_command_substitution(self):
        out = Output(deque())
        eval_command_line("echo `echo echo`", out)

        result = [line for line in out]

        self.assertEqual(result, ["echo\n"])

    def test_redirects_output(self):
        out = Output(deque())
        eval_command_line("echo hello > test.txt", out)

        result = [line for line in out]

        self.assertEqual(result, [])

    def test_redirects_input(self):
        out = Output(deque())
        eval_command_line("cat < file1.txt", out)

        result = [line for line in out]

        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_pipes(self):

        out = Output(deque())
        eval_command_line("echo abc | cut -b -1,2-", out)

        result = [line for line in out]

        self.assertEqual(result, ["abc\n"])

    def test_substitution_in_double_quotes(self):

        out = Output(deque())
        eval_command_line('echo "`echo foo`"', out)

        result = [line for line in out]

        self.assertEqual(result, ["foo\n"])

    def test_two_input_redirections(self):
        out = Output(deque())

        self.assertRaises(ValueError, eval_command_line,
                          "cat < file1.txt < dir1/file2.txt", out)

    def test_two_output_redirections(self):
        out = Output(deque())

        self.assertRaises(ValueError, eval_command_line,
                          "cat > file1.txt > dir1/file2.txt", out)

    def test_double_pipe(self):
        out = Output(deque())
        eval_command_line("cat file1.txt | sort | uniq", out)

        result = [line for line in out]

        self.assertEqual(result, ["aabc\n", "zzxy\n"])


if __name__ == "__main__":
    unittest.main()
