import unittest
from applications.Grep import Grep
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        grep = Grep()
        cls.exec = grep.exec

    def setUp(self):
        set_up_files()

    def test_grep_one_file(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["a", "file1.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "aabc\n")
        self.assertEqual(len(output.output), 0)

    def test_grep_no_matches(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["f", "file1.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(len(output.output), 0)

    def test_grep_with_wildcard(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["d.", "dir1/file2.txt"]
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result, ["ddd\n", "ddd\n"])

    def test_grep_opened_file(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["a"]
        curr_input = open("dir1/file2.txt", "r")
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result, ["aa\n", "aa\n"])

    def test_grep_multipl_files(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["a.", "file1.txt", "dir1/file2.txt"]
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result,
                         ['file1.txt:aabc\n',
                          'dir1/file2.txt:aa\n',
                          'dir1/file2.txt:aa\n'])

    def test_grep_with_no_args_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
