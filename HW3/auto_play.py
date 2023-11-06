import alphaBetaPrunning
import game
from hueristics import *
from tqdm import tqdm


def play_one_game(p1, p2):
    oneMoreChance = False
    board = game.create()
    round = 0
    board = game.setHumanComputer(board, p1[0], p2[0])
    while not game.isFinished(board) or oneMoreChance:
        # print(round)
        # print(board)

        # game.printState(board)
        # if round > 20:
        #     quit()

        if game.isHumTurn(board):
            # game.inputMove(board)
            # Get input from the computer pretending to be a human
            ret = alphaBetaPrunning.go(board, p1[1])
            if ret == 0:
                # print("No more moves")
                oneMoreChance = True
                game.changePlayer(board)

            else:
                board = ret
        else:
            ret = alphaBetaPrunning.go(board, p2[1])
            if ret == 0:
                # print("No more moves")
                oneMoreChance = True
                game.changePlayer(board)

            else:
                board = ret
        # print(board)
        if (game.isFinished(board) and not (oneMoreChance)):
            if (game.anyLegalMove(board)):
                # print("No more moves - One more chance")
                game.changePlayer(board)
            else:
                oneMoreChance = False
        else:
            oneMoreChance = False
        round += 1
    # game.printState(board)
    return board

p1_wins = 0
p2_wins = 0
flag = False
for i in tqdm(range(100)):
    flag = not flag
    board = play_one_game(('○' if flag else '●', defensive_corner_grabber_hueristic), ('●' if flag else '○', corner_grabber_hueristic))
    winner = game.whoWin(board)
    if winner < 0: # Black wins
        if flag:
            p2_wins += 1
        else:
            p1_wins += 1
    elif winner > 0: # White wins
        if flag:
            p1_wins += 1
        else:
            p2_wins += 1
    print()
    print(p1_wins, "-", p2_wins)


print("P1 wins:", p1_wins)
print("P2 wins:", p2_wins)
