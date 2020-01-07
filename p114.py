from options import Options
import time

# Use dynamic programming

def solve(min_length, tiles, opt):
    t0 = time.time()

    ## Solution
    combos = [0 for i in range(tiles)]

    # All-gray is a valid arrangement
    for i in range(min_length - 1):
        combos[i] = 1
    combos[min_length - 1] = 2

    for i in range(min_length, len(combos)):
        # Cases where the newest (i+1th) tile is filled by a block of length j
        for j in range(min_length, i + 2):
            combos[i] += 1 if j >= i else combos[i - j - 1] # (i + 1) - (j + 1) - 1
        # Case where the newest tile is unfilled
        combos[i] += combos[i - 1]

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return combos[-1]

def main(opt):
    print('Answer:', solve(3, 50, opt), '\n')

def tests(opt):
    print('Tests:')
    print(solve(3, 7, opt))

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
