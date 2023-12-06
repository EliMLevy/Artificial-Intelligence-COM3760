from  game import *


board=game()
create(board)

c = 3
r = makeMove(board, c)

while checkIfPieceEndedGame(board, r, c) not in [TIE, VICTORY, LOSS]: # while game is not over
    r, c = inputTrueRandomAgentFast(board) # player true random move
    print("Row: ", r, " Col: ", c, ". Result: ", checkIfPieceEndedGame(board, r, c))
    printState(board)
