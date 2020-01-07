from options import Options
import time

# Use dynamic programming

RED = 2
GREEN = 3
BLUE = 4

def solve(block_size, tiles, opt):
    t0 = time.time()

    ## Solution
    combos = [0 for i in range(tiles)]
    combos[block_size - 1] = 1 # All-gray is not a valid arrangement
    for i in range(block_size, len(combos)):
        combos[i] = combos[i - block_size] + 1 + combos[i - 1]

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return combos[-1]

def main(opt):
    print('Answer:', solve(RED, 50, opt) + solve(GREEN, 50, opt) + solve(BLUE, 50, opt), '\n')

def tests(opt):
    print('Tests:')
    print(solve(RED, 5, opt))
    print(solve(GREEN, 5, opt))
    print(solve(BLUE, 5, opt))

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
