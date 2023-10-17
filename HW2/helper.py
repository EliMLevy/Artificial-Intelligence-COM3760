import random

def place_n_queens(size, columns):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size)
        columns.append(column)
        row += 1


def display(size, columns):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


# Since the attacking is reflexive, we only need to count half the attacks
# I.e If we identify that A is threatened by B, we need not indentify that B is threatened by A
# Thus, we need only find queens that are threatened BELOW the current queens

def calculate_threats(columns, index):
  result = 0
  # Count queens in the same col
  for i in range(index + 1, len(columns)):
    if i != index and columns[i] == columns[index]:
      result += 1
  # Count queens in the same diagonal above
  # for i in range(1, index):
  #   if index - i >= 0:
  #     # left
  #     if columns[index] - i == columns[index - i]:
  #       result += 1
  #     # Right
  #     if columns[index] + i == columns[index - i]:
  #       result += 1

  # Count queens in the same diagonal below
  for i in range(1, len(columns) - index):
    # print(i)
    if index + i < len(columns):
      # left
      if columns[index] - i == columns[index + i]:
        result += 1
      # Right
      if columns[index] + i == columns[index + i]:
        result += 1
  return result


def count_threats(size, columns):
  threats = []
  total_threats = 0
  for i in range(size):
    # print("checking queen: ", i)
    val = calculate_threats(columns, i)
    total_threats += val
    threats.append(val)
  return total_threats,threats


# Finds the best move that is less than total_threats
# Returns a tuple (X,Y) which indicates moving the queen in row X to column Y
def find_best_move(size, columns):
  best_move = (-1, -1)             # Move queen in row X to column Y
  least_threats = len(columns)**2  # initialize the best option to infinity
  threat_lst = []                 # for debugging
  for row_num in range(size):
    for col_num in range(size):
      # If this row's queen is already in this column we can skip this calculation
      if col_num == columns[row_num]:
        continue
      temp = columns[row_num]  # Store this value so we can replace it
      columns[row_num] = col_num
      threats, lst = count_threats(size, columns)
      columns[row_num] = temp

      if threats < least_threats:
        best_move = (row_num, col_num)
        least_threats = threats
        threat_lst = lst
      if threats == 0:
        break

    if least_threats == 0:
      break
  return best_move, least_threats


def do_move(columns, move):
  columns[move[0]] = move[1]
