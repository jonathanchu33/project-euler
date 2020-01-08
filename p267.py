from utils import Options, nCr
import time
from scipy.optimize import minimize_scalar
import numpy as np

# The gains or losses after each turn can be expressed as multiplicative factors;
# since multiplication is commutative, we only have 1000 cases to consider - the
# number of winning coin flips. Then we simply optimize the objective function;
# even a brute numerical evaluation with a coarse loop is sufficient (see tests()).

def objective(f, threshold):
    probability = 0
    for i in range(1001):
        value = ((1 + 2 * f) ** i) * ((1 - f) ** (1000 - i))
        if value >= threshold:
            probability += (.5 ** 1000) * nCr(1000, i)
    return probability

def solve(threshold, opt):
    t0 = time.time()

    ## Solution
    # After the initial run this range was easy to choose, but as seen in tests()
    # the range (0, 1) doesn't take long to search with a simple loop
    res = minimize_scalar(lambda x: -objective(x, threshold), [0.05, .5])

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')
    if opt.check:
        print('Check:', res.x, objective(res.x, threshold))

    return -res.fun

def main(opt):
    print('Answer:', solve(1000000000, opt), '\n')

def tests(opt):
    print('Tests:')
    max_val, max_f = 0, 0
    for i in np.arange(0, 1, .01):
        prob = objective(i, 1000000000)
        if prob > max_val:
            max_f = i
            max_val = prob
    print('Maximum', max_val, 'with f =', max_f)

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)

