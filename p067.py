from utils import Options
import time
from p018 import solve as solve18

# See problem 18

def solve(file, opt):
    return solve18(file, opt)

def main(opt):
    print('Answer:', solve('handout/problem67.txt', opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
