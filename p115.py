from utils import Options
import time
from p114 import solve as solve114

# A slightly modified version of solve114

def solve(min_length, threshold, opt):
    t0 = time.time()

    ## Solution
    combos = [0 for i in range(min_length)]

    # All-gray is a valid arrangement
    for i in range(min_length - 1):
        combos[i] = 1
    combos[min_length - 1] = 2

    while combos[-1] <= threshold:
        combos.append(0)
        i = len(combos) - 1
        # Cases where the newest (i+1th) tile is filled by a block of length j
        for j in range(min_length, i + 2):
            combos[-1] += 1 if j >= i else combos[i - j - 1] # (i + 1) - (j + 1) - 1
        # Case where the newest tile is unfilled
        combos[i] += combos[i - 1]

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')
    if opt.check:
        print('Check:', combos[-1])

    return len(combos)

def main(opt):
    print('Answer:', solve(50, 1000000, opt), '\n')

def tests(opt):
    print('Tests:')
    print(solve114(3, 29, opt))
    print(solve114(3, 30, opt))
    print(solve114(10, 56, opt))
    print(solve114(10, 57, opt))
    print(solve114(50, 167, opt))
    print(solve114(50, 168, opt))

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
