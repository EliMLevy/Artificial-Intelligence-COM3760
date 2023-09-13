import time
import search


def run_benchmark(size: int, num_runs: int):
    print("***Size: " + str(size) + "***")
    total_added = 0
    total_removed = 0
    total_depth = 0
    total_time = 0

    for i in range(num_runs):
        tic = time.time()
        answer = search.search(size)
        toc = time.time()
        total_added += answer[1]
        total_removed += answer[2]
        total_depth += answer[3]
        total_time += (toc-tic)
        if toc - tic > 5:
            print("!!!TIMEOUT!!!")
            total_depth += 20 * (num_runs - i)
            total_added += 10000 * (num_runs - i)
            total_removed += 10000 * (num_runs - i)
            total_time += 100 * (num_runs - i)
            break

    print("Average depth: " + str(total_depth / num_runs))
    print("Average number inserted: " + str(total_added / num_runs))
    print("Average number removed: " + str(total_removed / num_runs))
    print("Average runtime: " + str(total_time) + " seconds")


run_benchmark(2, 100)
run_benchmark(3, 100)
run_benchmark(4, 100)
