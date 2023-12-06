import game
import time


def test1():
    total = 0
    num_runs = 1000
    wins = 0
    for i in range(num_runs):
        board=game.game()
        game.create(board)
        tic = time.time()
        while not game.isFinished(board):
            game.inputTrueRandomAgentFast2(board)
        if board.val == game.VICTORY:
            wins += 1
        result = time.time() - tic
        total += result

    print(total / num_runs)

def test2():
    num_runs = 10
    total = 0
    for _ in range(num_runs):
        # print(i)
        board=game.game()
        game.create(board)
        tic = time.time()
        game.inputMCParallel(board) 
        dur = time.time() - tic
        # print(dur)
        total += dur

    print(total / num_runs)


if __name__ == "__main__":
    test2()