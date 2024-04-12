import unittest
from Input import Input
from utils.set_up_files import set_up_files


class TestInput(unittest.TestCase):

    def setUp(self):
        set_up_files()
        self.input = Input(open("file1.txt"))

    def test_is_iterable(self):
        result = []
        for line in self.input:
            result.append(line)

        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_has_readlines(self):
        result = self.input.readlines()

        self.assertEqual(result, ["aabc\n", "zzxy\n"])

    def test_redirects_input(self):
        self.input.redirect(open("dir1/file2.txt"))

        self.assertEqual(True, self.input.redirected)
        result = self.input.readlines()
        self.assertEqual(result, ["bbb\n", "aa\n", "aa\n",
                                  "ddd\n", "ddd\n", "cc\n"])


if __name__ == "__main__":
    unittest.main()
