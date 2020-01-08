from utils import Options
import time

# In spirit, a combination of the previous three

RED = 2
GREEN = 3
BLUE = 4

def solve(block_sizes, tiles, opt):
    t0 = time.time()

    ## Solution
    blocks = sorted(block_sizes)

    # Prepopulate combinations up to smallest given block size; all-gray is a valid arrangement
    combos = [0 for i in range(tiles)]
    for i in range(blocks[0] - 1):
        combos[i] = 1
    combos[blocks[0] - 1] = 2

    for i in range(blocks[0], len(combos)):
        for j in blocks:
            if j > i + 1:
                break
            combos[i] += 1 if j == i + 1 else combos[i - j]
        combos[i] += combos[i - 1]

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return combos[-1]

def main(opt):
    print('Answer:', solve([RED, GREEN, BLUE], 50, opt), '\n')

def tests(opt):
    print('Tests:')
    print(solve([RED, GREEN, BLUE], 5, opt))

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
