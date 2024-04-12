from src.Output import Output
from src.Input import Input
from collections import deque
import sys


def initialize_test_values():
    output = Output(deque())
    curr_input = Input(sys.stdin)
    args = []
    result = []
    return (output, curr_input, args, result)
