import unittest
from applications.Tail import Tail
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestTail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tail = Tail()
        cls.exec = tail.exec

    def setUp(self):
        set_up_files()

    def test_tail_no_flag(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir2/file4.txt"]
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result, [f"{i}\n" for i in range(90, 100)])

    def test_tail_no_flag_no_args(self):
        output, curr_input, args, result = initialize_test_values()

        curr_input = open("dir2/file4.txt", "r")
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result, [f"{i}\n" for i in range(90, 100)])

    def test_head_n0(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-n", "0", "dir2/file4.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(len(output.output), 0)

    def test_tail_n1(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-n", "1", "dir2/file4.txt"]
        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "99\n")
        self.assertEqual(len(output.output), 0)

    def test_tail_n50(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-n", "50", "dir2/file4.txt"]
        self.exec(args, curr_input, output)

        while len(output.output):
            result.append(output.output.popleft())

        self.assertEqual(result, [f"{i}\n" for i in range(50, 100)])

    def test_tail_with_wrong_flag_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-f", "50", "dir2/file4.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_tail_with_multiple_files_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-f", "50", "dir2/file4.txt", "file1.txt"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
