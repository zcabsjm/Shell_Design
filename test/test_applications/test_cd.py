import unittest
from applications.Cd import Cd
import os
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestCat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cd = Cd()
        cls.exec = cd.exec
        cls.test_dir = "/comp0010/test-dir"

    def setUp(self):
        set_up_files()

    def test_cd_with_one_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir1"]

        self.exec(args, curr_input, output)
        self.assertEqual(os.getcwd(), f"{self.test_dir}/dir1")

    def test_cd_with_no_args_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        self.assertRaises(ValueError, self.exec, args, curr_input, output)

    def test_cd_with_two_args_should_raise_exception(self):
        output, curr_input, args, result = initialize_test_values()

        args = ["dir1", "dir2"]

        self.assertRaises(ValueError, self.exec, args, curr_input, output)


if __name__ == "__main__":
    unittest.main()
