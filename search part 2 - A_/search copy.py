#search

import state
import frontier

def search(n):
    s=state.create(n)
    # print(s)
    added = 0
    removed = 0
    depth = 0
    f=frontier.create(s)
    while not frontier.is_empty(f):
        removed += 1
        s=frontier.remove(f)
        if len(s[1]) > depth:
            depth = len(s[1])
        if state.is_target(s):
            return [s, f[1], added, removed, depth]
        ns=state.get_next(s)
        for i in ns:
            added += 1
            frontier.insert(f,i)
    return 0

# print (search(3))





