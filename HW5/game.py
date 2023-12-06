import copy
import random
import concurrent.futures


VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board
random.seed()

rows=6
columns=7

class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    moves = 0

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
        s.moves = 0

def cpy(s1):
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        #print("board ", s2.board)
        return s2
       
def value(s):
#Returns the heuristic value of s
    dr=[-SIZE+1, -SIZE+1, 0, SIZE-1] #the next lines compute the heuristic val.
    dc=[0, SIZE-1, SIZE-1, SIZE-1]
    val=0.00001
    for row in range(rows):
        for col in range(columns):
            for i in range(len(dr)):
                t=checkSeq(s, row, col, row+dr[i], col+dc[i])
                if t in [LOSS,VICTORY]:
                   val=t
                   break
                else:
                   val+=t
    if s.size==0 and val not in [LOSS, VICTORY]:
       val=TIE
    s.val = val
    return val


def checkForWinnerFast(s):
    dr=[-SIZE+1, -SIZE+1, 0, SIZE-1] #the next lines compute the heuristic val.
    dc=[0, SIZE-1, SIZE-1, SIZE-1]
    val=0.00001
    for row in range(rows):
        for col in range(columns):
            if s.board[row][col] != 0:
                for i in range(len(dr)):
                    t=checkSeq(s, row, col, row+dr[i], col+dc[i])
                    if t in [LOSS,VICTORY]:
                        return t
    if s.size==0 and val not in [LOSS, VICTORY]:
       val=TIE
    s.val = val
    return val

def checkIfPieceEndedGame(s, r, c):
    dr=[-SIZE+1, -SIZE+1, 0, SIZE-1] 
    dc=[0, SIZE-1, SIZE-1, SIZE-1]
    for i in range(len(dr)):
        t=checkSeq(s, r, c, r+dr[i], c+dc[i])
        if t in [LOSS,VICTORY]:
            return t
        
def checkSeq(s, r1, c1, r2, c2):
#r1, c1 are in the board. if r2,c2 not on board returns 0.
#Checks the seq. from r1,c1 to r2,c2. If all X returns VICTORY. If all O returns LOSS.
#If empty returns 0.00001. If no Os returns 1. If no Xs returns -1.
    if r2<0 or c2<0 or r2>=rows or c2>=columns:
        return 0 #r2, c2 are illegal

    dr=(r2-r1)//(SIZE-1) #the horizontal step from cell to cell
    dc=(c2-c1)//(SIZE-1) #the vertical step from cell to cell

    sum=0

    for i in range(SIZE):#summing the values in the seq.
        sum += s.board[r1+i*dr][c1+i*dc]

    if sum == COMPUTER*SIZE:
        return VICTORY

    elif sum == HUMAN*SIZE:
        return LOSS
    elif sum > 0 and sum < COMPUTER:
        return -1

    elif sum > 0 and sum % COMPUTER==0:
        return 1
    return 0.00001 #not 0 because TIE is 0


def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        for r in range(rows):
            print("\n|",end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")
        print()

        for i in range(columns): #For numbers on the bottom
            print(" ",i,sep="",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")

def isFinished(s):
#Seturns True iff the game ended
    return value(s)  in [LOSS, VICTORY, TIE] or s.size==0

def isFinishedFast(s):
#Seturns True iff the game ended
    v = value(s)
    return v  in [LOSS, VICTORY, TIE] or s.size==0, v


def isHumTurn(s):
#Returns True iff it is the human's turn to play
        return s.playTurn==HUMAN
    

def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-MC / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN          
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for humaמ or computer) in col. c
#and switches turns.
#Assumes the move is legal.
        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER
        s.moves += 1
        return r-1
  
def inputMove(s):
#Reads, enforces legality and executes the user's move.
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")
            else:
                flag=False
                makeMove(s,c)

def inputRandom(s):
    # See if the agent can win block one move ahead
    for i in range(0, columns):  # this simple agent always plays min
        tmp = cpy(s)
        makeMove(tmp, i)
        if (value(tmp) == LOSS and s.board[0][i] == 0):  # if the agent should win
            makeMove(s, i)
            return
    # If no obvious move, then move random
    flag = True
    while flag:
        c = random.randrange(0, columns)
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")
            printState(s)
        else:
            flag = False
            makeMove(s, c)
            
def inputHeuristic(s):
    # See if the agent can win or get more than one in a row
    temp = 1000
    tmp_col= 0
    for i in range(0, columns):  # this simple agent always plays min
        tmp = cpy(s)
        makeMove(tmp, i)
        if (value(tmp) < temp and s.board[0][i] == 0):  # so a "loss" is a win for this side
            tmp_col=i
            temp=value(tmp)
    makeMove(s, tmp_col)
    
def inputMC(s):
    return singleThreadedMC(s)
    # if s.moves < 10:
    #     # print("short")
    #     return inputMCParallel(s)
    # else:
    #     # print("long")
    #     return singleThreadedMC(s)

def singleThreadedMC(s):
    NUM_SIMULATIONS = 100
    best_col = -1
    best_win_rate = -1
    for col in range(columns): # For each col
        tmp = cpy(s) # copy the baord
        r = makeMove(tmp, col) # go in the current col
        c = col
        wins = 0
        for i in range(NUM_SIMULATIONS):
            tmp2 = cpy(tmp)
            while not checkIfPieceEndedGame(tmp2, r, c): # while game is not over
                r, c = inputTrueRandomAgentFast(tmp2) # player true random move
            if value(tmp2) == VICTORY: # record if I won
                 wins += 1
        if wins > best_win_rate: 
            best_win_rate = wins
            best_col = col
    
    makeMove(s, best_col) # Go in the col that had the best win percentage
    return best_col

def simulate_col(args):
    col, s = args
    NUM_SIMULATIONS = 100
    tmp = cpy(s)
    makeMove(tmp, col)
    wins = 0
    for _ in range(NUM_SIMULATIONS):
        tmp2 = cpy(tmp)
        while not isFinished(tmp2):
            inputTrueRandomAgentFast(tmp2)
        if value(tmp2) == VICTORY:
            wins += 1
    return col, wins
        

def inputMCParallel(s):
    best_col = -1
    best_win_rate = -1

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(simulate_col,  [(col, s) for col in range(columns)]))

    for col, wins in results:
        if wins > best_win_rate:
            best_win_rate = wins
            best_col = col

    makeMove(s, best_col)
    return best_col

def inputTrueRandomAgentFast(s):
    valid_columns = [col for col in range(columns) if s.board[0][col] == 0]
    
    if not valid_columns:
        print("No valid moves.")
        return
    
    c = random.choice(valid_columns)
    r = makeMove(s, c)
    return r, c

def inputTrueRandomAgent(s):
    flag = True
    while flag:
        c = random.randrange(0, columns)
        if c < 0 or c >= columns or s.board[0][c] != 0:
            # print("Illegal move.")
            # printState(s)
            pass
        else:
            flag = False
            makeMove(s, c)