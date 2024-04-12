import unittest
from applications.Find import Find
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        find = Find()
        cls.exec = find.exec

    def setUp(self):
        set_up_files()

    def test_find_with_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-name", "file1.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "./file1.txt\n")
        self.assertEqual(len(output.output), 0)

    def test_find_with_file_in_different_directory(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-name", "file2.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "./dir1/file2.txt\n")
        self.assertEqual(len(output.output), 0)

    def test_find_pattern(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-name", "*.txt"]
        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(set(result), {
            "./file1.txt\n",
            "./dir1/file2.txt\n",
            "./dir1/file3.txt\n",
            "./dir2/file4.txt\n"
        })

    def test_find_with_specified_directory(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir2", "-name", "*.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "dir2/file4.txt\n")
        self.assertEqual(len(output.output), 0)

    def test_find_with_no_args_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_find_with_wrong_flag_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-n", "file1.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_find_with_wrong_flag_and_specified_dir_should_raise_exception(
            self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir1", "-n", "file1.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
