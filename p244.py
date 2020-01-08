from utils import Options
import time
import math

# Modified BFS. Search paths until final state is found. Each state is only
# visited once in the BFS queue, but multiple paths to the same state (if they)
# are of the same minimum length) are tracked by storing lists of their checksums.

visited = {}   # Store visit depth of visited states
checksums = {} # Store list of checksums from paths leading to visited state

def get_neighbors(state, w_loc):
    """Returns list of states attainable by iterating one move from state, each
    represented as (state_string, new_w_location, list_of_new_checksums).
    """
    i, j = w_loc
    dim = int(math.sqrt(len(state)))
    neighbors = []

    def move(new_w_loc, mk):
        """Move W to new_w_loc, with the appropriate ASCII value mk to update checksums."""
        x, y = new_w_loc
        new_state = list(state)
        new_state[i * dim + j] = new_state[x * dim + y]
        new_state[x * dim + y] = 'W'
        neighbors.append((''.join(new_state), new_w_loc, [(csum * 243 + mk) % 100000007 for csum in checksums[state]]))

    if i > 0:
        move((i - 1, j), 68) # D
    if i < dim - 1:
        move((i + 1, j), 85) # U
    if j > 0:
        move((i, j - 1), 82) # R
    if j < dim - 1:
        move((i, j + 1), 76) # L

    return neighbors

def solve(root, w_root, final, opt):
    t0 = time.time()

    ## Solution
    # Instantiate BFS queue
    bfs_queue = [(root, w_root, 0)] # state, W location, visit depth
    visited[root], checksums[root] = 0, [0]
    index = 0
    sum_checksums = 0

    while index < len(bfs_queue):
        current_state, w_loc, depth = bfs_queue[index]

        # When found, sum checksums of paths to final state
        if current_state == final:
            for checksum in checksums[current_state]:
                sum_checksums += checksum
                sum_checksums %= 100000007
            break

        # Otherwise, add next states to queue
        for neighbor, w_new, new_csum_list in get_neighbors(current_state, w_loc):
            if neighbor not in visited:
                # First visit to neighbor
                bfs_queue.append((neighbor, w_new, depth + 1))
                visited[neighbor] = depth + 1
                checksums[neighbor] = new_csum_list
            elif visited[neighbor] == depth + 1:
                # Different path to neighbor of the same length as before is found
                # (note this length is minimum by the nature of BFS)
                checksums[neighbor].extend(new_csum_list)

        index += 1

    ## Options
    if opt.time:
        print('Time:', time.time() - t0, 'sec')

    return sum_checksums

def main(opt):
    w_initial = (0, 0)
    initial_state = 'WRBBRRBBRRBBRRBB'
    final_state = 'WBRBBRBRRBRBBRBR'
    print('Answer:', solve(initial_state, w_initial, final_state, opt), '\n')

def tests(opt):
    pass

if __name__ == '__main__':
    opt = Options().parse()
    main(opt)
    if opt.check:
        tests(opt)
