import unittest
from applications.Wc import Wc
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestWc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        wc = Wc()
        cls.exec = wc.exec

    def setUp(self):
        set_up_files()

    def test_wc_show_lines(self):

        output, curr_input, args, result = initialize_test_values()

        args = ["-l", "file1.txt"]
        self.exec(args, curr_input, output)

        result = [line for line in output]

        self.assertEqual(result, ["2\n"])

    def test_wc_show_words(self):

        output, curr_input, args, result = initialize_test_values()

        args = ["-w", "file1.txt"]
        self.exec(args, curr_input, output)

        result = [line for line in output]

        self.assertEqual(result, ["2\n"])

    def test_wc_all_counts(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["-l", "-m", "-w", "file1.txt"]
        self.exec(args, curr_input, output)

        result = [line for line in output]

        self.assertEqual(result, ["2 2 10\n"])

    def test_wc_show_all(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["file1.txt"]
        self.exec(args, curr_input, output)

        result = [line for line in output]

        self.assertEqual(result, ["2 2 10\n"])

    def test_wc_stdin(self):
        output, curr_input, args, result = initialize_test_values()

        args = []
        self.exec(args, open("file1.txt"), output)

        result = [line for line in output]

        self.assertEqual(result, ["2 2 10\n"])


if __name__ == "__main__":
    unittest.main()
