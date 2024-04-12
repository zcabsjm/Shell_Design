import unittest
from applications.Ls import Ls
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestLs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ls = Ls()
        cls.exec = ls.exec
        cls.test_dir = "/comp0010/test-dir"

    def setUp(self):
        set_up_files()

    def test_ls_no_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = []
        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(sorted(result),
                         sorted(["dir2\n", "file1.txt\n", "dir1\n"]))

    def test_ls_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir2"]
        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["file4.txt\n"])

    def test_ls_with_too_many_files_should_throw_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir1", "dir2"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)
