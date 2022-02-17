
def possible_moves(board, token):
    places = []
    for i in range(0, len(board)):
        if(board[i:i+1] == "."):
            adjacents = getAdjacents(board, i) #returns tuple of x, o, blank
            if(token == "x"):
                if(adjacents[1] > 0):
                    where = findToken(board, i, "o")
                    for place in where:
                        if(isCapable(board, i, place, token)):
                            if(i not in places):
                                places.append(i)
            elif(token == "o"):
                if(adjacents[0] > 0):
                    where = findToken(board, i, "x")
                    for place in where:
                        if(isCapable(board, i, place, token)):
                            if(i not in places):
                                places.append(i)
    return places
            

def isCapable(board, tokenindex, oppindex, token):
    qboard = makeQuestionBoard(board)
    qtokenindex = tokenindex + 9 + (2 * (int(tokenindex/8)+1))
    qoppindex = oppindex + 9 + (2 * (int(oppindex/8)+1))
    place = qoppindex-qtokenindex 
    i = qtokenindex + place
    # opptoken = "x" if (token == "o") else "o"
    see = qboard[i:i+1]
    while(qboard[i:i+1] != "?" and qboard[i:i+1] != "."):
        if(qboard[i:i+1] == token):
            return True
        i += place
    return False
    

def make_move(board, token, place):
    place = place 
    newboard = board[0:place] + token + board[place+1:]
    opptoken = "x" if (token == "o") else "o"
    where = findToken(newboard, place, opptoken)
    places = []
    for x in where:
        if(isCapable(newboard, place, x, token)):
            places.append(x-place)
    for i in places:
        count = place + i
        while(newboard[count:count+1] != token):
            newboard = newboard[0:count] + token + newboard[count+1:]
            count += i
    return newboard

def findToken(board, index, token):
    qboard = makeQuestionBoard(board)
    qtokenindex = index + 9 + (2 * (int(index/8)+1))
    indices = []
    for i in range(9, 12):
        indices.append((index+i-2, qtokenindex+i))
        indices.append((index-i+2, qtokenindex-i))
    indices.append((index+1, qtokenindex+1))
    indices.append((index-1,qtokenindex-1))
    final = []
    for i in indices:
        qindex = i[1]
        temp = qboard[qindex:qindex+1]
        if(temp == token):
            final.append(i[0])
    return final

def getAdjacents(board, index):
    adjIndices = []
    for i in range(7, 10):
        adjIndices.append(index+i)
        adjIndices.append(index-i)
    adjIndices.append(index+1)
    adjIndices.append(index-1)
    xcount = 0
    ocount = 0
    dotcount = 0
    for i in adjIndices:
        temp = board[i:i+1]
        if(temp == "x"):
            xcount += 1
        elif(temp == "o"):
            ocount +=1
        elif(temp == "."):
            dotcount +=1
    return (xcount, ocount, dotcount)


def makeQuestionBoard(board):
    newboard = "???????????" + board + "???????????"
    count = 1
    added = 0
    
    for i in range(10, len(newboard)):
        if(count == (10)):
            newboard = newboard[0:i] + "??" + newboard[i:]
            count = 0
        count+=1
    return newboard


def makeQuestionBoardNum(board, bareindex):
    board = "???????????" + board + "???????????"
    count = 1
    added = 0
    row = int(bareindex/7)
    add = 9
    for i in range(10, len(board)):
        if(count == (10)):
            board = board[0:i] + "??" + board[i:]
            count = 0
            if(int(i/10) <= row):
                add += 2
        count+=1
    return add


def printQBoard(board):
    for i in range(1, len(board)+1):
        print(board[i-1:i], "", end = '')
        if(i % 10 == 0):
            print(i-1)
        

def printBoard(board):
    tempboard = board.replace("?", '')
    for i in range(1, len(tempboard)+1):
        print(tempboard[i-1:i], "", end = '')
        if(i % 8 == 0):
            print()

            
def findPositionofToken(board, token):
    for i in range(len(board)):
        if(board[i:i+1] == token):
            print(i)


def find_next_move(startboard, token, depth):
    # t1 = time.perf_counter()
    # t2 = time.perf_counter()
    val = idminimaxhelperval(startboard, depth, 0, token, float("-inf"), float("inf"))
    tempindex = idminimaxhelperindex(startboard, token, depth, val)
    return tempindex

def idminimaxhelperval(board, maxdepth, depth, token, alpha, beta):
    if(maxdepth == depth):
        result = goal_test(board)
        return result
    
    opptoken = "x" if (token == "o") else "o"

    if(token == "x"):
        maxVal = float("-inf")
        for position in possible_moves(board, token):
            newboard = make_move(board, token, position)
            val = idminimaxhelperval(newboard, maxdepth, depth+1, opptoken, alpha, beta)
            maxVal = max(val, maxVal)
            alpha = max(alpha, val)
            if(beta <= alpha):
                break
        return maxVal

    else:
        minVal = float("inf")
        for position in possible_moves(board, token):
            newboard = make_move(board, token, position)
            val = idminimaxhelperval(newboard, maxdepth, depth+1, opptoken, alpha, beta)
            minVal = min(val, minVal)
            beta = min(beta, val)
            if(beta <= alpha):
                break
        return minVal
    

def idminimaxhelperindex(startboard, token, maxdepth, value):
    opptoken = "x" if (token == "o") else "o"
    temp = possible_moves(startboard, token)
    for position in temp:
        next_board = make_move(startboard, token, position)
        if(idminimaxhelperval(next_board, maxdepth, 1, opptoken, float("-inf"), float("inf")) == value):
            return position
    return None
        

def goal_test(board):
    token = "x"
    opptoken = "o"
    mypossiblemoves = len(possible_moves(board, token))
    opppossiblemoves = len(possible_moves(board, opptoken))
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
    if(board[1:2] == opptoken and board[0:1] == "."): #firstcorneradjacents (topleft)
        score +=1
    if((board[8:9] == opptoken and board[0:1] == ".")):
        score+=1
    if((board[9:10] == opptoken and board[0:1] == ".")):
        score+=1
    if(board[6:7] == opptoken and board[7:8] == "."): #seconddcorneradjacents (topright)
        score+=1
    if(board[14:15] == opptoken and board[7:8] == "."):
        score+=1
    if(board[15:16] == opptoken and board[7:8] == "."):
        score+=1
    if(board[48:49] == opptoken and board[56:57] == "."): #thirdcorneradjacents (bottomleft)
        score+=1
    if(board[49:50] == opptoken and board[56:57] == "."):
        score+=1
    if(board[57:58] == opptoken and board[56:57] == "."):
        score+=1
    if(board[54:55] == opptoken and board[63:64] == "."): #fourthcorneradjacents (bottomright)
        score+=1
    if(board[55:56] == opptoken and board[63:64] == "."):
        score+=1
    if(board[62:63] == opptoken and board[63:64] == "."):
        score+=1
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
    if(board[1:2] == token and board[0:1] == "."): #firstcorneradjacents (topleft)
        score +=-1
    if((board[8:9] == token and board[0:1] == ".")):
        score+=-1
    if((board[9:10] == token and board[0:1] == ".")):
        score+=-1
    if(board[6:7] == token and board[7:8] == "."): #seconddcorneradjacents (topright)
        score+=-1
    if(board[14:15] == token and board[7:8] == "."):
        score+=-1
    if(board[15:16] == token and board[7:8] == "."):
        score+=-1
    if(board[48:49] == token and board[56:57] == "."): #thirdcorneradjacents (bottomleft)
        score+=-1
    if(board[49:50] == token and board[56:57] == "."):
        score+=-1
    if(board[57:58] == token and board[56:57] == "."):
        score+=-1
    if(board[54:55] == token and board[63:64] == "."): #fourthcorneradjacents (bottomright)
        score+=-1
    if(board[55:56] == token and board[63:64] == "."):
        score+=-1
    if(board[62:63] == token and board[63:64] == "."):
        score+=-1
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

    # favorable and unfavorable wall situations 
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

class Strategy():
  logging = True  # Optional
  def best_strategy(self, board, player, best_move, still_running):
      depth = 1
      for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
          best_move.value = find_next_move(board, player, depth)
          depth += 1
