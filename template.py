from utils import Options
import time

# Description

def solve(opt):
    t0 = time.time()

    ## Solution

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')
    if opt.check:
        print('Check:')

    return

def main(opt):
    print('Answer:', solve(opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
