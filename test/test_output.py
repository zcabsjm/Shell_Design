import unittest
from Output import Output
from collections import deque
import sys


class TestOutput(unittest.TestCase):
    def setUp(self):
        self.output = Output(deque())

    def test_output_constructor(self):
        self.assertFalse(self.output.redirected)
        self.assertEqual(self.output.output, deque())

    def test_output_redirect(self):
        redirectFile = "redirectFile"
        self.output.redirect(redirectFile)

        self.assertEqual(self.output.outputRedirect, redirectFile)
        self.assertTrue(self.output.redirected)

    def test_output_write(self):

        self.output.write("aaa\n")

        self.assertEqual(self.output.output.popleft(), 'aaa\n')

    def test_output_print_to_other_file(self):
        self.output.output.append("aaa\n")
        self.output.output.append("bbb\n")

        redirectFile = open("file.txt", "w")
        self.output.outputRedirect = redirectFile

        self.output.print()
        redirectFile.close()

        f = open("file.txt", "r")
        lines = f.readlines()
        self.assertEqual(lines, ["aaa\n", "bbb\n"])

    def test_output_pipe_with_output_redirect(self):
        self.output.output.append("aaa\n")
        self.output.output.append("bbb\n")

        redirectFile = open("file.txt", "w")
        self.output.outputRedirect = redirectFile

        self.output.pipe(sys.stdin)

        redirectFile.close()

        f = open("file.txt", "r")
        lines = f.readlines()
        self.assertEqual(lines, ["aaa\n", "bbb\n"])

    def test_output_prints_stdout(self):
        self.output.output.append("aaa\n")

        self.output.print()
