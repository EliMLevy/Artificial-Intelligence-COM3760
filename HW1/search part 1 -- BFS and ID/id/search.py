#search

import state
import frontier
import time

max_time = 5

def search(n):
    s=state.create(n)
    # print(s)
    f=frontier.create(s)
    tic = time.time()

    while not frontier.is_empty(f):
        if time.time() - tic > max_time:
            raise Exception("Timeout")
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[4], f[5]]
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
    return 0


