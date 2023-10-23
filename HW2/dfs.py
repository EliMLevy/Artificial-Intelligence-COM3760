import random
import time



def place_n_queens(columns, size):
    columns.clear()
    row = 0
    while row < size:
        column=random.randrange(0,size)
        columns.append(column)
        row+=1


def display(columns, size):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


def place_in_next_row(columns, column):
    columns.append(column)


def remove_in_current_row(columns):
    if len(columns) > 0:
        return columns.pop()
    return -1


def next_row_is_safe(columns, size, column):
    row = len(columns)
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            return False
    return True


def solve_queen(columns, size):
    columns.clear()
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        #place queen in next row
        #print(columns)
        #print("I have ", row, " number of queens put down")
        #display()
        while column < size:
            number_of_iterations += 1
            if next_row_is_safe(columns, size, column):
                place_in_next_row(columns, column)
                number_of_moves += 1
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if (column == size or row == size):
            number_of_iterations += 1
            # if board is full, we have a solution
            if row == size:
                # print("I did it! Here is my solution")
                # display(columns, size)
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row(columns)
            number_of_moves += 1
            if (prev_column == -1):  # I backtracked past column 1
                print("There are no solutions")
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column


def run(size):
    columns = []
    #size = int(input('Enter n: '))
    num_iterations = 0
    number_moves = 0
    #for i in range(0, 100):
    #    columns = [] #columns is the locations for each of the queens
    tic = time.time()
    num_iterations, number_moves = solve_queen(columns, size)
    
    print(size, num_iterations, number_moves)
    return num_iterations, number_moves, time.time() - tic

