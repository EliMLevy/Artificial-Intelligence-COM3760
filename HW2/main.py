from british_museum import run as bm_run
from dfs import run as dfs_run
from forward_checking import run as forward_checking_run
from min_conflicts import run as min_conflicts_run
import pandas as pd
import time


results = pd.DataFrame(
    columns=["n", "number_of_iterations", "number_of_moves", "time"])
for i in range(4, 100):
    iterations, moves, runtime = min_conflicts_run(i)
    results.loc[len(results)] = [i, iterations, moves, runtime]
    results.to_csv("testing.csv")
    if runtime > 30:
        break


