import random
import game

'''
Default hueristic
deterministic and not very good 
'''
def naive_hueristic(s):
    #Returns the heuristic value of s
    s[1] = 1  # your code here ###
    return s[1]


'''
Random hueristic
non-deterministic and not very good 
'''
def random_hueristic(s):
    s[1] = random.randint(-5, 5)
    return s[1]


'''
Side grabber hueristic
The sides are better because they are not so easily captured.
'''
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

'''
The corners are even better than the sides because they are impossible to capture
'''
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


'''
The corners are best and the sides are important. It is also important to try preventing the opponent 
from getting the sides and corners. It is not strictly necessary to put the negative values in the
spots that allow the opponent to get the sides and corners becuase the minimax algorithm will give negative
scores to the states where the opponent gets the sides and corners. However, since the depth is limited, the 
negative weights give us an extra level of depth for free by disincentivizing going somewhere that the 
opponent can get a corner or side on the next turn.

The middle four squares are given value because in the end game, controlling the center often turns the tide
when the difference in pieces is close.
'''
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
