import time
import random


def display(columns, size):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


def place_n_queens(columns, size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1


def place_n_queens_pattern(columns, size):
    columns.clear()
    r = 1
    for i in range(size):
        columns.append(r)
        r += 2
        if r >= size:
            r = 0
    return columns


def is_valid_queens_solution(queens):
    N = len(queens)

    # Check if the length of the input array is equal to N
    if N <= 0:
        return False

    # Check for conflicts in rows, columns, and diagonals
    for i in range(N):
        for j in range(i + 1, N):
            # Check for conflicts in the same column
            if queens[i] == queens[j]:
                return False
            # Check for conflicts in the diagonals
            if abs(queens[i] - queens[j]) == abs(i - j):
                return False

    # If no conflicts were found, it's a valid solution
    return True


def count_conflicts_to(row, col, columns):
    result = 0
    for i in range(len(columns)):
        if i == row:
            continue
        if (col == columns[i]) or (abs(row - i) == abs(col - columns[i])):
            result += 1
    return result

def count_total_conflicts(columns):
    val = 0
    for i in range(len(columns)):
        val += count_conflicts_to(i, columns[i], columns)
        
    return val

def apply_move(move, columns):
    if move is None:
        return
    columns[move[0]] = move[1]


# We will choose a random row and move that queen to the location with the minimum conflicts
def get_next_state(columns, size):
    best_val = size
    best_move = None
    row = random.randint(0, size - 1)
    for i in range(size):  # For each queen
        conflicts = count_conflicts_to(row, i, columns)
        if conflicts < best_val:
            best_val = conflicts
            best_move = i

    columns[row] = best_move
    return columns


def solve_queens(size):
    # Place all the queens
    iters = 0
    moves = 0
    columns = []
    columns = place_n_queens_pattern(columns, size)
    moves += size
    val = count_total_conflicts(columns)
    # display(columns, size)
    # print(val)
    resets = 0
    iters_per_setup = 100
    countdown = iters_per_setup

    tic = time.time()
    timeout = 300
    while (val != 0) and (time.time() - tic < timeout):
        # find the successsor
        columns = get_next_state(columns, size)
        moves += 2
        val = count_total_conflicts(columns)
        iters += 1
        countdown -= 1
        if val == 0:
            return columns, iters, moves, time.time() - tic
        if countdown <= 0:
            # print("Countdown: ", countdown, " moves. Current val: ", val, ". Best val: ", best_val, ". Condition: ", best_val >= val )
            place_n_queens(columns, size)
            resets += 1
            moves += size
            val = count_total_conflicts(columns)
            countdown = iters_per_setup


    if time.time() - tic > timeout:
        print("TIMEOUT")
    return columns, iters, moves, time.time() - tic

def run(size):
    columns, iters, moves, runtime = solve_queens(size)
    print(size, iters, moves)
    if not is_valid_queens_solution(columns):
        raise Exception("This is not a valid solution!")
    
    return iters, moves, runtime


# size = 39
# for size in range(30, 100):
#     columns, iters, moves, runtime = run(size)
#     print(size, iters, resets, )
#     # display(columns, 8)
#     print()
