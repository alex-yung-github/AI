import othello_imports
import time
import sys


def idminimax(startboard, token, depth):
    maxdepth = 1
    result = []
    # t1 = time.perf_counter()
    # t2 = time.perf_counter()
    while(maxdepth < depth):
        val = idminimaxhelperval(startboard, maxdepth, 0, token, float("-inf"), float("inf"))
        tempindex = idminimaxhelperindex(startboard, token, maxdepth, val)
        print(tempindex)
        result.append(tempindex)
        maxdepth+=1
    return result[len(result)-1]

def idminimaxhelperval(board, maxdepth, depth, token, alpha, beta):
    if(maxdepth == depth):
        result = goal_test(board)
        return result
    
    opptoken = "x" if (token == "o") else "o"

    if(token == "x"):
        maxVal = float("-inf")
        for position in othello_imports.possible_moves(board, token):
            newboard = othello_imports.make_move(board, token, position)
            val = idminimaxhelperval(newboard, maxdepth, depth+1, opptoken, alpha, beta)
            maxVal = max(val, maxVal)
            alpha = max(alpha, val)
            if(beta <= alpha):
                break
        return maxVal

    else:
        minVal = float("inf")
        for position in othello_imports.possible_moves(board, token):
            newboard = othello_imports.make_move(board, token, position)
            val = idminimaxhelperval(newboard, maxdepth, depth+1, opptoken, alpha, beta)
            minVal = min(val, minVal)
            beta = min(beta, val)
            if(beta <= alpha):
                break
        return minVal
    

def idminimaxhelperindex(startboard, token, maxdepth, value):
    opptoken = "x" if (token == "o") else "o"
    temp = othello_imports.possible_moves(startboard, token)
    for position in temp:
        next_board = othello_imports.make_move(startboard, token, position)
        if(idminimaxhelperval(next_board, maxdepth, 1, opptoken, float("-inf"), float("inf")) == value):
            return position
    return None
        

def goal_test(board):
    token = "x"
    opptoken = "o"
    mypossiblemoves = len(othello_imports.possible_moves(board, token))
    opppossiblemoves = len(othello_imports.possible_moves(board, opptoken))
    score = 0
    if(token not in board):
        return -420
    elif(opptoken not in board):
        return 420
    elif(opppossiblemoves <= 0 and mypossiblemoves <= 0):
        tokencounts = countTokens(board, "x", opptoken)
        mytokencount = tokencounts[0]
        opptokencount = tokencounts[1]
        return 100 * (mytokencount - opptokencount)

    #favourable corner situations
    if(board[0:1] == token):
        score += 5
    if(board[7:8] == token):
        score += 5
    if(board[63:64] == token):
        score += 5
    if(board[56:57] == token):
        score += 5
    if((board[1:2] == opptoken or board[8:9] == opptoken 
    or board[9:10] == opptoken) and board[0:1] == "."):
        score +=3
    if((board[6:7] == opptoken or board[14:15] == opptoken 
    or board[15:16] == opptoken) and board[7:8] == "."):
        score +=3
    if((board[48:49] == opptoken or board[49:50] == opptoken
    or board[57:58] == opptoken) and board[56:57] == "."):
        score+=3
    if((board[54:55] == opptoken or board[55:56] == opptoken 
    or board[62:63] == opptoken) and board[63:64] == "."):
        score+=3
    if(board[1:2] == token and board[0:1] != "."): #after corners taken
        score +=1
    if(board[8:9] == token and board[0:1] != "."):
        score+=1
    if(board[6:7] == token and board[7:8] != "."):
        score +=1
    if(board[15:16] == token and board[7:8] != "."):
        score+=1
    if(board[48:49] == token and board[56:57] != "."):
        score +=1
    if(board[57:58] == token and board[56:57] != "."):
        score+=1
    if(board[55:56] == token and board[63:64] != "."):
        score+=1
    if(board[62:63] == token and board[63:64] != "."):
        score+=1

    
    #unfavourable corner situations
    if(board[0:1] == opptoken):
        score += -5
    if(board[7:8] == opptoken):
        score += -5
    if(board[63:64] == opptoken):
        score += -5
    if(board[56:57] == opptoken):
        score += -5
    if((board[1:2] == token or board[8:9] == token 
    or board[9:10] == token) and board[0:1] == "."):
        score += -3
    if((board[6:7] == token or board[14:15] == token 
    or board[15:16] == token) and board[7:8] == "."):
        score +=-3
    if((board[48:49] == token or board[49:50] == token
    or board[57:58] == token) and board[56:57] == "."):
        score+=-3
    if((board[54:55] == token or board[55:56] == token 
    or board[62:63] == token) and board[63:64] == "."):
        score+=-3
    if(board[1:2] == opptoken and board[0:1] != "."): #after corner taken
        score +=-1
    if(board[8:9] == opptoken and board[0:1] != "."):
        score+=-1
    if(board[6:7] == opptoken and board[7:8] != "."):
        score +=-1
    if(board[15:16] == opptoken and board[7:8] != "."):
        score+=-1
    if(board[48:49] == opptoken and board[56:57] != "."):
        score +=-1
    if(board[57:58] == opptoken and board[56:57] != "."):
        score+=-1
    if(board[55:56] == opptoken and board[63:64] != "."):
        score+=-1
    if(board[62:63] == opptoken and board[63:64] != "."):
        score+=-1

    # favorable and unfavorable wall situations (Will be O(n), but only 16 checks; negligible time
    for i in range(2, 6): #top wall
        if(board[i:i+1] == token):
            score+=1
        elif(board[i:i+1] == opptoken):
            score+=-1
    for i in range(58, 62): #bottom wall
        if(board[i:i+1] == token):
            score+=1
        elif(board[i:i+1] == opptoken):
            score+=-1
    for i in range(16, 41, 8): #left wall
        if(board[i:i+1] == token):
            score+=1
        elif(board[i:i+1] == opptoken):
            score+=-1
    for i in range(23, 48, 8): #right wall
        if(board[i:i+1] == token):
            score+=1
        elif(board[i:i+1] == opptoken):
            score+=-1

    #stability checks, only runs late game after corners:
    # if(board[0:1] != "." and board[1:2] != "." and board[8:9] == "."
    # and board[6:7] != "." and board[7:8] != "." and board[15:16] != "."
    # and board[48:49] != "." and board[56:57] != "." and board[57:58] != "."
    # and board[55:56] != "." and board[62:63] != "." and board[63:64] != "."):

    if(board[0:1] != "."):
        stablecount = 0
        temptoken = board[0:1]
        torightlen = 1
        for i in range(1, 8):
            if(board[i:i+1] != temptoken):
                break
            else:
                torightlen+=1
                stablecount+=1
        prevrowlen = torightlen
        limit = prevrowlen
        for i in range(8, 49, 8):
            for col in range(i, i+limit):
                if(board[col:col+1] != temptoken):
                    break
                else:
                    prevrowlen +=1
                    stablecount+=1
            if(prevrowlen == 0):
                break
            limit = prevrowlen
            prevrowlen = 0
        if(temptoken == opptoken):
            score -= (2 * stablecount)
        elif(temptoken == token):
            score += (2 * stablecount)

    if(board[7:8] != "."): #second corner stability (top right)
        stablecount = 0
        temptoken = board[7:8]
        toleftlen = 0
        for i in range(6, 0, -1):
            if(board[i:i+1] != temptoken):
                break
            else:
                toleftlen+=1
                stablecount+=1
        limit = toleftlen
        for i in range(15, 56, 8):
            prevrowlen = 0
            for col in range(i, i-limit, -1):
                if(board[col:col+1] != temptoken):
                    break
                else:
                    prevrowlen +=1
                    stablecount+=1
            if(prevrowlen == 0):
                break
            limit = prevrowlen
        if(temptoken == opptoken):
            score -= (2 * stablecount)
        elif(temptoken == token):
            score += (2 * stablecount)

    if(board[56:57] != "."): #third, or bottom left, corner
        stablecount = 0
        temptoken = board[56:57]
        torightlen = 1
        for i in range(57, 63):
            if(board[i:i+1] != temptoken):
                break
            else:
                torightlen+=1
                stablecount+=1
        prevrowlen = torightlen
        limit = prevrowlen
        for i in range(48, 7, -8):
            for col in range(i, i+limit):
                if(board[col:col+1] != temptoken):
                    break
                else:
                    prevrowlen +=1
                    stablecount+=1
            if(prevrowlen == 0):
                break
            limit = prevrowlen
            prevrowlen = 0
        if(temptoken == opptoken):
            score -= (2 * stablecount)
        elif(temptoken == token):
            score += (2 * stablecount)
    
    if(board[63:64] != "."): #fourth, or bottom right, corner
        stablecount = 0
        temptoken = board[63:64]
        toleftlen = 0
        for i in range(62, 56, -1):
            if(board[i:i+1] != temptoken):
                break
            else:
                toleftlen+=1
                stablecount+=1
        prevrowlen = toleftlen
        limit = prevrowlen
        for i in range(55, 8, -8):
            for col in range(i, i-limit, -1):
                if(board[col:col+1] != temptoken):
                    break
                else:
                    prevrowlen +=1
                    stablecount+=1
            if(prevrowlen == 0):
                break
            limit = prevrowlen
            prevrowlen = 0
        if(temptoken == opptoken):
            score -= (2 * stablecount)
        elif(temptoken == token):
            score += (2 * stablecount)
        
    
    return mypossiblemoves - opppossiblemoves + score


def countTokens(board, mytoken, opptoken):
    mytokencount = 0
    opptokencount = 0
    for i in range(len(board)):
        if(board[i:i+1] == mytoken):
            mytokencount+=1
        elif(board[i:i+1] == opptoken):
            opptokencount+=1
        
    return (mytokencount, opptokencount)

def checkdifferent(board, endboard):
    for i in range(len(board)):
        if(board[i] != endboard[i]):
            return i

# board = "...........................ox......xo..........................."
# # tem = idminimax(board, "x")
# newboard = othello_imports.make_move(board, "x", 19)
# othello_imports.printBoard(newboard)
# tem2 = idminimax(newboard, "o")
# print(tem2)
# newboard2 = othello_imports.make_move(newboard, "o", 34)
# othello_imports.printBoard(newboard2)

board = sys.argv[1]
player = sys.argv[2]
# board = "...................x.......xx.....ooo..........................."
# player = "x"
idminimax(board, player, 10)
# board = "ooxo....oxo....oo.o...o.xoo.ox.ooxxox..o.xxx..ooxx.oxoooooxo..oo"
# print(isStable(board, 38, "o"))
