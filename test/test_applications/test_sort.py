import unittest
from src.applications.Sort import Sort
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestSort(unittest.TestCase):
    def setUp(self):
        set_up_files()
        sort = Sort()
        self.exec = sort.exec

    def test_sort_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_sort_two_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-r", "file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["zzxy\n", "aabc\n"])

    def test_sort_no_arg(self):
        output, curr_input, args, result = initialize_test_values()

        curr_input = open("file1.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_sort_reverse_no_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-r"]
        curr_input = open("file1.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["zzxy\n", "aabc\n"])

    def test_sort_with_wrong_flag_should_throw_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-d", "file1.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_sort_with_too_many_files_should_throw_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-r", "file1.txt", "file2.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
