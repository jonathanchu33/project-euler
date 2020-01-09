from utils import Options
import time
from collections import Counter
from math import factorial
import operator as op
from functools import reduce

# Basic approach: Loop through all numbers, following each number's chain until
# arriving at a number that has already been memoized. We make some optimizations.

# Observe that for any number which is <= X digits long, the maximum value of the
# second element in its chain is 9^2 * X. Therefore, we only need to use the basic
# approach to determine the endpoints of the numbers [1, 9^2 * X], which we store
# in a lookup table. For all other numbers, the next element in their chains are
# guaranteed to be in this lookup table.

# Next, observe that all permutations of a given set of digits lead to the same
# next chain element, e.g. 12 -> 5 and 21 -> 5. Thus, instead of iterating through
# [1, 10^X), we only need to iterate through all unique combinations of digits -
# i.e. all X-digit numbers (leading 0s being significant) whose digits are in
# non-decreasing order. For instance, the set of combinations (not permutations!)
# of 3 digits is fully specified by the numbers {ABC | A<=B<=C, for digits A, B, C}.
# Moreover, given a combination of digits, the number of permutations of those
# digits is given by the coresponding multinomial coefficient. For example, there
# are 6!/(1!2!3!) permutations of the number 122333. Altogether, for every
# combination of digits whose chain ends on 89, we add its multinomial coefficient
# to the final count.

squares = [i ** 2 for i in range(10)]
def f_map_reduce(num_as_list):
    """Sum digits' squares."""
    return sum(map(lambda x: squares[x], num_as_list))

class DigitCombinations:
    """Enumerates all combinations of X digits in lexicographical order."""
    def __init__(self, digits):
        self.digits = digits

    def __iter__(self):
        self.combination = [0 for i in range(self.digits)]
        return self

    def __next__(self):
        incr_digit = -1
        self.combination[incr_digit] += 1
        while self.combination[incr_digit] > 9:
            incr_digit -= 1
            if incr_digit < -self.digits:
                raise StopIteration
            self.combination[incr_digit] += 1
        floor_value = self.combination[incr_digit]
        for i in range(incr_digit + 1, 0):
            self.combination[i] = floor_value
        return self.combination, Counter(self.combination).values()

def solve(digits, opt):
    t0 = time.time()

    ## Solution
    # Records 'endpoint' of every number's chain using T/F
    endpoints = {1: False, 89: True}

    # Basic approach for the first (digits * 81)
    for i in range(1, digits * 81 + 1):
        chain = [i]
        current = i
        while current not in endpoints:
            current = f_map_reduce(list(map(lambda x: int(x), str(current))))
            chain.append(current)

        for el in chain:
            endpoints[el] = True if endpoints[current] else False

    # Count using multinomial coefficient
    count = 0
    for combo, duplicates in DigitCombinations(digits):
        if endpoints[f_map_reduce(combo)]:
            count += factorial(digits) / reduce(op.mul, map(lambda x: factorial(x), duplicates), 1)

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return int(count)

def main(opt):
    print('Answer:', solve(7, opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
