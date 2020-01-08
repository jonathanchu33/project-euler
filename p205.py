from utils import Options
import time
import numpy as np

# Instead of manually enumerating the probabilities, just use numpy to calculate
# the convolutions! Our desired PMFs are simply convolutions of discrete uniform RVs.

def solve(opt):
    t0 = time.time()

    ## Solution
    pyramid_pmfs = np.array([
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                                [.25, .25, .25, .25],
                            ])
    cube_pmfs = np.array([
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                             [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                         ])

    peter_pmf = pyramid_pmfs[0]
    for i in range(1, pyramid_pmfs.shape[0]):
        peter_pmf = np.convolve(pyramid_pmfs[i], peter_pmf)
    colin_pmf = cube_pmfs[0]
    for i in range(1, cube_pmfs.shape[0]):
        colin_pmf = np.convolve(cube_pmfs[i], colin_pmf)

    # Include 0-probability values to pad probability values for 1 - 36
    peter_pmf = np.append(np.zeros(8), peter_pmf)
    colin_pmf = np.append(np.zeros(5), colin_pmf)

    # Calculate Peter's winning probability
    peter_win = 0
    for i in range(len(peter_pmf)):
        for j in range(i):
            peter_win += peter_pmf[i] * colin_pmf[j]

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')
    if opt.check:
        print('Check:', peter_pmf.sum(), colin_pmf.sum())

    return peter_win

def main(opt):
    print('Answer:', solve(opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)

