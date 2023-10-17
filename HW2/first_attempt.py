import time
from helper import *
import random

size = 30
columns = []

# 1) place n random queens
place_n_queens(size, columns)
# columns = [3, 1, 0, 1]
# display(size, columns)
print(columns)

# 2) for each queen, count the number of threats
num_threats, lst = count_threats(size, columns)
print("Total threats: ", num_threats, lst)
iterations = 0
moves = 0
tic = time.time()
timeout = 60
while num_threats > 0 and time.time() - tic < timeout:
    best_move, threats_left = find_best_move(size, columns)
    if threats_left < num_threats:
        num_threats = threats_left
        do_move(columns, best_move)
        moves += 1
    else:
        place_n_queens(size, columns)
        num_threats, lst = count_threats(size, columns)
        moves += size
    iterations += 1

if num_threats == 0:
    print("Found solution! Iterations: ", iterations, " Moves: ", moves)
    print("Time: ", time.time() - tic)
    print(columns)
else:
    print("Timed out!")


