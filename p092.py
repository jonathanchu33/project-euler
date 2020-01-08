from utils import Options
import time

# Use memoization to truncate chains

def solve(endpoint, opt):
    t0 = time.time()

    ## Solution
    seen = {1: False, 89: True} # Records 'endpoint' of every number's chain using T/F
    for i in range(1, endpoint):
        if opt.progress and i % opt.progress == 0:
            print(i, '/', endpoint)

        chain = [i]
        current = i
        while current not in seen:
            sum_square = 0
            while current > 0:
                sum_square += (current % 10) ** 2
                current //= 10
            chain.append(sum_square)
            current = sum_square

        for el in chain:
            seen[el] = True if seen[current] else False

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return sum(seen.values())

def main(opt):
    print('Answer:', solve(10000000, opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
