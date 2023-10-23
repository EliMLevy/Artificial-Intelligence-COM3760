import time
import random
import pandas as pd


def place_n_queens(columns, size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1


def display(columns, size):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


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



def run(size):
    columns = []
    number_of_iterations = 0
    number_of_moves = 0
    timeout = 60

    tic = time.time()

    while (not is_valid_queens_solution(columns)) and time.time() - tic < timeout:
        number_of_iterations += 1
        number_of_moves += size
        place_n_queens(columns, size)



    if is_valid_queens_solution(columns):
        print("Success! Took ", number_of_iterations, " iterations and ",
                time.time() - tic, " seconds and ", number_of_moves, " number_of_moves")
    else:
        print("Failed! Took ", number_of_iterations, " iterations and ",
                time.time() - tic, " seconds and ", number_of_moves, " number_of_moves")
    display(columns, size)
    return number_of_iterations, number_of_moves, time.time() - tic
