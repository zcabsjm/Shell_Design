import unittest
from applications.Pwd import Pwd
import os
from utils.set_up_files import set_up_files
from utils.initialize_test_values import initialize_test_values


class TestPwd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pwd = Pwd()
        cls.exec = pwd.exec
        cls.test_dir = "/comp0010/test-dir"

    def setUp(self):
        set_up_files()

    def test_pwd_no_arg(self):
        output, curr_input, args, result = initialize_test_values()

        args = []

        self.exec(args, curr_input, output)
        self.assertEqual(os.getcwd(), f"{self.test_dir}")


if __name__ == "__main__":
    unittest.main()
