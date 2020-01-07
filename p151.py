from options import Options
import time
from collections import Counter

# Let X_i be an indicator random variable for the i^th batch, equal to 1 if
# the envelope contains a single sheet of paper for that batch. Then the number
# of times the foreman finds a single sheet of paper in a week is X = \sum_i X_i,
# and E(X) = \sum_i E(X_i) is our desired quantity by linearity of expectation.
# But E(X_i) is simply the probability that the envelope of the i^th batch
# contains a single sheet of paper. We can find E(X_i) by calculating the
# probabilities of all possible paper configurations for each batch, using
# dynamic programming to implement the Law of Total Probability. Note that E(X)
# simplifies to the sum of three terms as E(X_i) is only nonzero for three
# batches (excluding the last) - the 2nd, 4th, and 8th last.

def solve(opt):
    t0 = time.time()

    ## Solution
    probabilities = [Counter() for i in range(15)]
    probabilities[0]['1248'] = 1

    for batch in range(1, 15):
        for combo, prob in probabilities[batch - 1].items():
            for i in range(len(combo)):
                cur_sheet = int(combo[i])
                new_combo = combo[:i] + combo[i + 1:]
                while cur_sheet > 1:
                    cur_sheet /= 2
                    new_combo += str(int(cur_sheet))
                probabilities[batch][''.join(sorted(new_combo))] += prob / len(combo) # LOTP - sheets are selected from envelope uniformly at random

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')
    if opt.check:
        print('Check:', probabilities[7]['8'], probabilities[11]['4'], probabilities[13]['2'])

    return probabilities[7]['8'] + probabilities[11]['4'] + probabilities[13]['2']

def main(opt):
    print('Answer:', solve(opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
