import game
import concurrent.futures



'''
A faster way to choose a purely random move
Returns the location of the placed chip so that we can efficiently check if the game is over
'''
def inputTrueRandomAgentFast(s):
    valid_columns = [col for col in range(game.columns) if s.board[0][col] == 0] # Retrieve all 
    if not valid_columns: # If there are no moves left then the game is over and something went wrong
        game.printState(s)
        print("No valid moves.", s.size)
        return
    
    c = game.random.choice(valid_columns) # choose a random valid col
    r = game.makeMove(s, c) # place the chip
    return r, c # Return the location of the placed chip


'''
Checks if the the specified chip created a four in a row
Instead of iterating over the whole board, checking each peice to
see if someone won, just check if the most recently placed piece
caused a winner. 
Args:
s=the board state
r=the row of the most recently placed piece
c=the column of the most recently placed piece
Returns LOSS, VICTORY, or TIE if appropriate or 0.1 is the game is ongoing
'''
def checkIfPieceEndedGame(s, r, c):
    dirs = [(1, 0), (1, -1), (0, 1), (1, 1)]
    for dir in dirs:
        t = checkLongSeq(s, r, c, dir[0], dir[1])
        if t in [game.LOSS, game.VICTORY]:
            return t

    if s.size == 0:
        return game.TIE
    
    return 0.1


'''
A more efficient way to check for a four in a row.
Instead of checking for a single four in a row, lets check a whole line of the board.

- r: Row index of the latest move.
- c: Column index of the latest move.
- step_r: Row direction of the check (0, 1, or -1).
- step_c: Column direction of the check (0, 1, or -1).
'''
def checkLongSeq(s, r, c, step_r, step_c):


    start_r = r + game.SIZE*-step_r
    start_c = c + game.SIZE*-step_c
    end_r = r
    end_c = c

    sum = 0
    for i in range(game.SIZE):
        if start_r+i*step_r < 0 or start_r+i*step_r >= game.rows or start_c+i*step_c < 0 or start_c+i*step_c >= game.columns:
            continue
        sum += s.board[start_r+i*step_r][start_c+i*step_c]

    # print(start_r, start_c, step_r, step_c, sum)

    if sum == game.COMPUTER*game.SIZE:
        return game.VICTORY

    elif sum == game.HUMAN*game.SIZE:
        return game.LOSS


    for i in range(game.SIZE):
        if start_r >= 0 and start_r < game.rows and start_c >= 0 and start_c < game.columns:
            sum -= s.board[start_r][start_c]
        start_r += step_r
        start_c += step_c
        if end_r >= 0 and end_r < game.rows and end_c >= 0 and end_c < game.columns:
            sum += s.board[end_r][end_c]
        # print(start_r, start_c, step_r, step_c, end_r, end_c, sum)
        end_r += step_r
        end_c += step_c


        if sum == game.COMPUTER*game.SIZE:
            return game.VICTORY

        elif sum == game.HUMAN*game.SIZE:
            return game.LOSS

    return 0.00001

'''
Single threaded version of the Monte Carlo agent
When the MC agent goes first I found that it wins nearly 100% of the time.
When the MC agent goes second it wins ~92% of the time. After investigating the reason
it loses those ~8% of games I found that the MC agent will often end up losing like this:
| | | | | | | |
| | | | | | | |
| | | |O| | | |
| | | |O|X| | |
| | | |O|X| | |
| | | |O|X| | |
 0 1 2 3 4 5 6
Where O is the oponent and x is the MC agent.
I think the MC agent struggles in these situations because both players are close to winning 
so instead of playing in column 3 to block the oponent, it plays in column 4. One way to fix
this could be to do some checks before running the monte carlo simulations:
1) Check if the MC agent has a move that will win this turn. If yes, do that
2) Check if the oponent has a move that will win on their turn. If yes, block that move.
If neither of the above cases hold then the MC agent should run the simulations for each column and 
pick the best move. However, incorporating those checks would probably be considered hueristics 
and are innapropriate to implement for a monte carlo AI homework assignment. 
'''
def singleThreadedMC(s):
    NUM_SIMULATIONS = 100 # I was able to go up to 200 in a reasonable amount of time with my optimizations
    best_col = -1
    best_win_rate = -1
    for col in range(game.columns): # For each col
        tmp = game.cpy(s)           # copy the baord
        r = game.makeMove(tmp, col) # go in the current col
        c = col  # r and c will be used to store the latest move for efficient checking of game over
        wins = 0 # Keep track of the number of times this column won
        for i in range(NUM_SIMULATIONS):
            tmp2 = game.cpy(tmp)
            while checkIfPieceEndedGame(tmp2, r, c) not in [game.TIE, game.VICTORY, game.LOSS]: # while game is not over
                r, c = inputTrueRandomAgentFast(tmp2) # player true random move
            if checkIfPieceEndedGame(tmp2, r, c) == game.VICTORY: # record if I won
                 wins += 1
        if wins > best_win_rate: 
            best_win_rate = wins
            best_col = col

    # This print statement was useful for debugging
    # print("Best col to pick: ", best_col, " with a win rate of: ", best_win_rate)
    
    game.makeMove(s, best_col) # Go in the col that had the best win rate
    return best_col


'''
The Monte Carlo sub routine to be used for the Parallel implementation
'''
def simulate_col(args):
    col, s = args
    NUM_SIMULATIONS = 300 # The paralel implementation outperforms the single threaded one when this number is large
    tmp = game.cpy(s)
    r = game.makeMove(tmp, col)
    c = col
    wins = 0
    for _ in range(NUM_SIMULATIONS):
        tmp2 = game.cpy(tmp)
        while checkIfPieceEndedGame(tmp2, r, c) not in [game.TIE, game.VICTORY, game.LOSS]:
            r, c = inputTrueRandomAgentFast(tmp2)
        if checkIfPieceEndedGame(tmp2, r, c) == game.VICTORY:
            wins += 1
    return col, wins


def inputMCParallel(s):
    best_col = -1
    best_win_rate = -1

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(simulate_col,  [(col, s) for col in range(game.columns)]))

    for col, wins in results:
        if wins > best_win_rate:
            best_win_rate = wins
            best_col = col

    game.makeMove(s, best_col)
    return best_col