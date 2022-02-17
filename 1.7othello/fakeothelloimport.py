


def possible_moves(board, token):
    places = []
    for i in range(29, len(board)):
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
    place = oppindex - tokenindex
    i = tokenindex + place
    # opptoken = "x" if (token == "o") else "o"
    while(board[i:i+1] != "?" and board[i:i+1] != "."):
        if(board[i:i+1] == token):
            return True
        
        i += place
    return False
    

def make_move(bareboard, token, place):
    board = makeQuestionBoard(bareboard)
    num1 = makeQuestionBoardNum(bareboard, place)
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
            i += place
    return newboard

def findToken(board, index, token):
    indices = []
    for i in range(9, 12):
        indices.append(index+i)
        indices.append(index-i)
    indices.append(index+1)
    indices.append(index-1)
    final = []
    for i in indices:
        if(i > 0):
            temp = board[i:i+1]
            if(temp == token):
                final.append(i)
    return final

def getAdjacents(board, index):
    adjIndices = []
    for i in range(9, 12):
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

def printBoard(board):
    tempboard = board.replace("?", '')
    for i in range(1, len(tempboard)+1):
        print(tempboard[i-1:i], "", end = '')
        if(i % 8 == 0):
            print()

def printQBoard(board):
    for i in range(1, len(board)+1):
        print(board[i-1:i], "", end = '')
        if(i % 10 == 0):
            print(i-1)
            
def findPositionofToken(board, token):
    for i in range(len(board)):
        if(board[i:i+1] == token):
            print(i)
board = "...........................ox......xo..........................."

newboard = makeQuestionBoard(board)
adjacencies = getAdjacents(newboard, 46)

print(adjacencies)
printQBoard(newboard)

#code to play a game
while("." in board):
    availablemoves = possible_moves(newboard, "x")
    print("Possible moves:", availablemoves)
    user = ""
    while(user not in availablemoves):
        user = int(input("P1 Choice? "))
        print()
    newboard = make_move(newboard, "x", user)
    printQBoard(newboard)


    availablemoves = possible_moves(newboard, "o")
    print("Possible moves:", availablemoves)
    user = ""
    while(user not in availablemoves):
        user = int(input("P2 Choice? "))
        print()
    newboard = make_move(newboard, "o", user)
    printQBoard(newboard)