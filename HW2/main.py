from british_museum import run as bm_run
from dfs import run as dfs_run
from forward_checking import run as forward_checking_run
from min_conflicts import run as min_conflicts_run
import pandas as pd
import time
from tqdm import tqdm


def find_high_score(name, method):
    results = pd.DataFrame(
        columns=["n", "number_of_iterations", "number_of_moves", "time"])
    for i in range(4, 100):
        iterations, moves, runtime = method(i)
        results.loc[len(results)] = [i, iterations, moves, runtime]
        results.to_csv(str(name) + ".csv")
        if runtime > 30:
            break


def average_100_runs(name, method, reps, start_n, end_n):
    results = pd.DataFrame(columns=["n", "avg iterations", "average moves", "average time"])
    for n in tqdm(range(start_n, end_n)):
        total_iters = 0
        total_moves = 0
        total_runtime = 0
        for i in range(reps):
            iterations, moves, runtime = method(n)
            total_iters += iterations
            total_moves += moves
            total_runtime += runtime

        results.loc[len(results)] = [n, total_iters/ reps, total_moves/reps, total_runtime / reps]

        results.to_csv(str(name) + ".csv")


find_high_score("british_museum", bm_run)
find_high_score("dfs", dfs_run)
find_high_score("forward_checking", forward_checking_run)
find_high_score("min_conflict", min_conflicts_run)

average_100_runs("forward_checking", forward_checking_run, 100, 14, 19)
average_100_runs("min_conflicts", min_conflicts_run, 100, 14, 19)


