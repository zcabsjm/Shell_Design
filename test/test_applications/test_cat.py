import unittest
from applications.Cat import Cat
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    def setUp(self):
        set_up_files()
        cat = Cat()
        self.exec = cat.exec

    def test_cat_with_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_cat_with_two_args(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["file1.txt", "dir1/file2.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(
            result, [
                "aabc\n", "zzxy\n", "bbb\n", "aa\n",
                "aa\n", "ddd\n", "ddd\n", "cc\n"])

    def test_cat_with_empty_file(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir1/file3.txt"]

        self.exec(args, curr_input, output)
        self.assertEqual(len(output.output), 0)

    def test_cat_with_opened_file(self):
        output, curr_input, args, result = initialize_test_values()

        curr_input = open("file1.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])


if __name__ == "__main__":
    unittest.main()
