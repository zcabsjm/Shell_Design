import unittest
from applications.Cut import Cut
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cut = Cut()
        cls.exec = cut.exec

    def setUp(self):
        set_up_files()

    def test_cut_with_one_byte(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-b", "1", "file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["a\n", "z\n"])

    def test_cut_with_multiple_bytes(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-b", "1,3,4", "file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["abc\n", "zxy\n"])

    def test_cut_with_open_intervals(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-b", "-2,4-", "file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aac\n", "zzy\n"])

    def test_cut_with_overlapping_intervals(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-b", "1-3,2-4", "file1.txt"]

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_cut_with_no_args_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_cut_with_wrong_flag_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-c", "1-3,2-4", "file1.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_cut_with_opened_file(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-b", "1-3,2-4"]
        curr_input = open("file1.txt", "r")

        self.exec(args, curr_input, output)
        while len(output.output):
            result.append(output.output.popleft())
        self.assertEqual(result, ["aabc\n", "zzxy\n"])


if __name__ == "__main__":
    unittest.main()
