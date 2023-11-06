import alphaBetaPrunning
import game
import hueristics
oneMoreChance = False

'''
Board is [gamestate, value, whose turn, game over]
'''

board=game.create()
board = game.whoIsFirst(board)
print(game.legalMoves(board))
while not game.isFinished(board) or oneMoreChance:
    # print(board)
    if game.isHumTurn(board):
        # print(board)
        game.inputMove(board)
        # print(board)
    else:
        board=alphaBetaPrunning.go(board,hueristics.corner_grabber_hueristic )
    if (game.isFinished(board) and not(oneMoreChance)):
        if (game.anyLegalMove(board)):
            print ("No more moves - One more chance")
            game.changePlayer(board)
        else:
            oneMoreChance = False
    else:
        oneMoreChance=False
game.printState(board)

