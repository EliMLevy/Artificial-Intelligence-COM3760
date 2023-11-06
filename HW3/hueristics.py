import random
import game

def naive_hueristic(s):
    #Returns the heuristic value of s
    s[1] = 1  # your code here ###
    return s[1]

def random_hueristic(s):
    s[1] = random.randint(-5, 5)
    return s[1]


def side_grabber_hueristic(s):

    mask = [0,0,0,0,0,0,0,0,0,0,0,
        10, 10, 10, 10, 10, 10, 10, 10,0,0,
            10, 0, 0, 0, 0, 0, 0, 10, 0,0,
            10, 0, 0, 0, 0, 0, 0, 10, 0,0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0,0,
            10, 0, 0, 0, 0, 0, 0, 10, 0,0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 10, 10, 10, 10, 10, 10, 10, ]
    val = 0
    for i, square in enumerate(s[0]):
        if (square != game.EMPTY):
            if square == game.COMPUTER:
                val += mask[i]
            else:
                val -= mask[i]



    return val


def corner_grabber_hueristic(s):

    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1000, 10, 10, 10, 10, 10, 10, 1000, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            10, 0, 0, 0, 0, 0, 0, 10, 0, 0,
            1000, 10, 10, 10, 10, 10, 10, 1000, ]
    val = 0
    for i, square in enumerate(s[0]):
        if (square != game.EMPTY):
            if square == game.COMPUTER:
                val += mask[i]
            else:
                val -= mask[i]

    return val


def defensive_corner_grabber_hueristic(s):

    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1000, 10, 10, 10, 10, 10, 10, 1000, 0, 0,
            10, -5, -3, -3, -3, -3, -5, 10, 0, 0,
            10, -3, 0, 0, 0, 0, -3, 10, 0, 0,
            10, -3, 0, 4, 4, 0, -3, 10, 0, 0,
            10, -3, 0, 4, 4, 0, -3, 10, 0, 0,
            10, -3, 0, 0, 0, 0, -3, 10, 0, 0,
            10, -5, -3, -3, -3, -3, -5, 10, 0, 0,
            1000, 10, 10, 10, 10, 10, 10, 1000, ]
    val = 0
    for i, square in enumerate(s[0]):
        if (square != game.EMPTY):
            if square == game.COMPUTER:
                val += mask[i]
            else:
                val -= mask[i]

    return val
