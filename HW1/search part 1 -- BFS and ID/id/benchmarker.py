import time
from tqdm import tqdm
import search
import pandas as pd


def run_benchmark(size: int, num_runs: int):
    print("***Size: " + str(size) + "***")
    total_added = 0
    total_removed = 0
    total_depth = 0
    total_time = 0
    timeouts = 0
    for i in tqdm(range(num_runs)):
        tic = time.time()
        try:
            answer = search.search(size)
            toc = time.time()
            total_added += answer[2]
            total_removed += answer[3]
            total_depth += answer[1]
            total_time += (toc-tic)
        except Exception:
            timeouts += 1
            total_added += 10000
            total_removed += 10000
            total_depth += 20
            total_time += 100
    result = pd.DataFrame({"name": ["id"], "depth": [total_depth / num_runs], "inserts": [total_added / num_runs],
                          "removes": [total_removed / num_runs], "time": [str(total_time/num_runs) + " seconds"]})
    result.to_csv("./results_" + str(size) + "x" + str(size) + ".csv", mode='a', header=False, index=False)
    print("Timeouts: " + str(timeouts))
    print("Average depth: " + str(total_depth / num_runs))
    print("Average number inserted: " + str(total_added / num_runs))
    print("Average number removed: " + str(total_removed / num_runs))
    print("Average runtime: " + str(total_time/num_runs) + " seconds")


run_benchmark(2, 100)
run_benchmark(3, 100)
run_benchmark(4, 100)
