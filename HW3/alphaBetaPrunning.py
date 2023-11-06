import game
import copy
DEPTH=3

def go(s, hueristic):
    if game.isHumTurn(s):
        # print(game.legalMoves(s))
        ret = abmin(s, DEPTH, float("-inf"), float("inf"), hueristic)
        return ret[1]
    else:
        # print(game.legalMoves(s))
        ret = abmax(s, DEPTH, float("-inf"), float("inf"), hueristic)
        return ret[1]
    # s = the state (max's turn)
    # d = max. depth of search
    # a,b = alpha and beta
    # returns [v, ns]: v = state s's value. ns = the state after recomended move.
    #        if s is a terminal state ns=0.


def abmax(s, d, a, b, hueristic):
        if d == 0 or game.isFinished(s):
            return [hueristic(s), 0]
        v = float("-inf")
        ns = game.getNext(s)
        bestMove = 0
        for i in ns:
            tmp = abmin(copy.deepcopy(i), d - 1, a, b, hueristic)
            if tmp[0] > v:
                v = tmp[0]
                bestMove = i
            if v >= b:
                return [v, i]
            if v > a:
                a = v
        return [v, bestMove]

    # s = the state (min's turn)
    # d = max. depth of search
    # a,b = alpha and beta
    # returns [v, ns]: v = state s's value. ns = the state after recomended move.
    #        if s is a terminal state ns=0.


def abmin(s, d, a, b, hueristic):
        if d == 0 or game.isFinished(s):
            return [hueristic(s), 0]
        v = float("inf")
        ns = game.getNext(s)
        bestMove = 0
        for i in ns:
            tmp = abmax(copy.deepcopy(i), d - 1, a, b, hueristic)
            if tmp[0] < v:
                v = tmp[0]
                bestMove = i
            if v <= a:
                return [v, i]
            if v < b:
                b = v
        return [v, bestMove]
