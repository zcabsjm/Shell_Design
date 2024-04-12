import unittest
from applications.Echo import Echo
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        echo = Echo()
        cls.exec = echo.exec

    def setUp(self):
        set_up_files()

    def test_echo_with_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["abc"]

        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "abc\n")
        self.assertEqual(len(output.output), 0)

    def test_echo_with_two_args(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["abc", "zzz"]

        self.exec(args, curr_input, output)

        self.assertEqual(output.output.popleft(), "abc zzz\n")
        self.assertEqual(len(output.output), 0)


if __name__ == "__main__":
    unittest.main()
