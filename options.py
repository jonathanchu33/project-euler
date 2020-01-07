import argparse

class Options:
    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--check', '-c', action='store_true', help='Calculate and/or print checks, if any. Some are given test parameters from the problem statement; others are benchmarks to verify solution steps')
        parser.add_argument('--time', '-t', action='store_true', help='Time calculations')
        return parser.parse_args()
