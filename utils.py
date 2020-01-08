import argparse
import operator as op
from functools import reduce

class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--check', '-c', action='store_true', help='Calculate and/or print checks, if any. Some are given test parameters from the problem statement; others are benchmarks to verify solution steps')
        self.parser.add_argument('--progress', '-p', nargs='?', type=int, default=False, const=100000, help='Print progress statements for problems with long loops')
        self.parser.add_argument('--time', '-t', action='store_true', help='Time calculations')

    def get_parser(self):
        return self.parser

    def parse(self):
        return self.parser.parse_args()

def nCr(n, r, int_floor=False):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n - r + 1, n + 1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom if int_floor else numer / denom
