import argparse, importlib, os, re
from utils import Options

def solve(problem, opt):
    module = importlib.import_module('p' + problem)
    print('Problem', problem)
    module.main(opt)

if __name__ == '__main__':
    parser = Options().get_parser()
    parser.add_argument('problems', nargs='*', help='Problem numbers to solve')
    args = parser.parse_args()

    if not args.problems:
        _, _, files = next(os.walk('.'))
        for filename in sorted(files):
            m = re.match('p(\d\d\d)\.py', filename)
            if m:
                args.problems.append(m.group(1))

    for problem in args.problems:
        solve(problem.zfill(3), args)
