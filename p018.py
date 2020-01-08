from utils import Options
import time

# Use dynamic programming

def load(filename, pyramid):
    file = open(filename, 'r')
    for line in file:
        pyramid.append([int(num) for num in line.rstrip('\n').split()])
    file.close()

def solve(file, opt):
    t0 = time.time()

    ## Solution
    pyramid = []
    load(file, pyramid)
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = max(pyramid[i][j] + pyramid[i + 1][j],
                                pyramid[i][j] + pyramid[i + 1][j + 1])

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return pyramid[0][0]

def main(opt):
    print('Answer:', solve('handout/problem18.txt', opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
