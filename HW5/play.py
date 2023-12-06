import game
import time

if __name__ == "__main__":
    board=game.game()
    game.create(board)
    print("Initial Game")
    game.printState(board)
    game.decideWhoIsFirst(board)
    comp_count = 0
    total_time = 0
    for i in range(0,100):#This loops takes about 15 seconds on my computer  
        huer_timer = 0
        mc_timer = 0
        tic = time.time()
        while not game.isFinished(board):
            if game.isHumTurn(board): #The simple agent plays "Human"
                # game.inputMove(board)
                hur_tic = time.time()
                game.inputHeuristic(board)
                huer_timer += time.time() - hur_tic
                # game.inputRandom(board)
            else:
                mc_tic = time.time()
                game.inputMC(board) #The MC agent plays "Computer"
                mc_timer += time.time() - mc_tic
            # game.printState(board)
        if game.value(board)==10**20: #the MC Agent won
            comp_count+=1
        dur = time.time() - tic
        total_time += dur
        print(comp_count, "/", (i + 1), ". Time took: ", dur, ". Total time: ", total_time, ". MC: ", mc_timer, ". Huer: ", huer_timer)
        print("Start another game")
        game.create(board)
    print("The MC agent beat the baseline:", comp_count, " out of ", i+1)



