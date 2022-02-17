import othello_imports
import time
import sys

def idnegamax(startboard, token):
    maxdepth = 1
    result = []
    # t1 = time.perf_counter()
    # t2 = time.perf_counter()
    while(maxdepth < 5):
    # while(t2 - t1 < 2):
        temp = (idnegamaxhelperval(startboard, maxdepth, 0, token))
        tempindex = idnegamaxhelperindex(startboard, token, maxdepth, temp)
        result.append(tempindex)
        print(tempindex)
        maxdepth+=1
        # t2 = time.perf_counter()
    return result[len(result)-1]

def idnegamaxhelperval(board, maxdepth, depth, token):
    if(maxdepth == depth):
        result = goal_test(board, token)
        return result
    
    opptoken = "o" if(token == "x") else "x"

    results = []
    if(depth < maxdepth):
        for child in othello_imports.possible_moves(board, token):
            newboard = othello_imports.make_move(board, token, child)
            temp = idnegamaxhelperval(newboard, maxdepth, depth+1, opptoken)
            n = temp * -1
            results.append(n)
    return max(results)
    

def idnegamaxhelperindex(startboard, token, maxdepth, value):
    opptoken = "x" if (token == "o") else "o"
    temp = othello_imports.possible_moves(startboard, token)
    for position in temp:
        next_board = othello_imports.make_move(startboard, token, position)
        if(idnegamaxhelperval(next_board, maxdepth, 1, opptoken) == value * -1):
            return position
    return None
        

def goal_test(board, token):
    opptoken = "x" if (token == "o") else "o"
    tokencounts = countTokens(board, token, opptoken)
    mytokencount = tokencounts[0]
    opptokencount = tokencounts[1]
    mypossiblemoves = len(othello_imports.possible_moves(board, token))
    opppossiblemoves = len(othello_imports.possible_moves(board, opptoken))
    score = 0
    if(token not in board):
        return opptokencount * -1
    elif(opptoken not in board):
        return mytokencount
    
    #favourable corner situations
    if(board[0:1] == token):
        score += 2
    if(board[7:8] == token):
        score += 2
    if(board[63:64] == token):
        score += 2
    if(board[56:57] == token):
        score += 2
    if((board[1:2] == opptoken or board[8:9] == opptoken 
    or board[9:10] == opptoken) and board[0:1] == "."):
        score +=2
    if((board[6:7] == opptoken or board[14:15] == opptoken 
    or board[15:16] == opptoken) and board[7:8] == "."):
        score +=2
    if((board[48:49] == opptoken or board[49:50] == opptoken
    or board[57:58] == opptoken) and board[56:57] == "."):
        score+=2
    if((board[54:55] == opptoken or board[55:56] == opptoken 
    or board[62:63] == opptoken) and board[63:64]):
        score+=2

    
    #unfavourable corner situations
    if(board[0:1] == opptoken):
        score += -2
    if(board[7:8] == opptoken):
        score += -2
    if(board[63:64] == opptoken):
        score += -2
    if(board[56:57] == opptoken):
        score += -2
    if((board[1:2] == token or board[8:9] == token 
    or board[9:10] == token) and board[0:1] == "."):
        score += -2
    if((board[6:7] == token or board[14:15] == token 
    or board[15:16] == token) and board[7:8] == "."):
        score +=-2
    if((board[48:49] == token or board[49:50] == token
    or board[57:58] == token) and board[56:57] == "."):
        score+=-2
    if((board[54:55] == token or board[55:56] == token 
    or board[62:63] == token) and board[63:64]):
        score+=-2
    

    #favorable and unfavorable wall situations (Will be O(n), but only 16 checks; negligible time
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
    

    if("." not in board):
        return mytokencount - opptokencount
    else:
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
# tem = idminimax(board, "x")
# newboard = othello_imports.make_move(board, "x", 19)
# tem2 = idminimax(newboard, "o")
# print(tem2)
# newboard2 = othello_imports.make_move(newboard, "o", 34)
# othello_imports.printBoard(newboard2)

board = sys.argv[1]
player = sys.argv[2]
# board = "...................x.......xx.....ooo..........................."
# player = "x"
idnegamax(board, player)

