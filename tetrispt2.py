import sys
from  math  import  log
import string
import random
types = {"I0": " " * 12 + "####", "I1": "#" + "   " + "#" + "   " + "#" + "   " + "#" + "   ",
         "O0": " " * 8 + "##" + "  " + "##" + "  ", 
         "T0": " " * 8 + " #  " + "### ", "T1": " " * 4 + "#   " + "##  " + "#   ", "T2": " " * 8 + "### " + " #  ", "T3": " " * 4 + " #  " + "##  " + " #  ",
         "S0": " " * 8 + " ## " + "##  ", "S1": " " * 4 + "#   " + "##  " + " #  ",
         "Z0": " " * 8 + "##  " + " ## ", "Z1": " " * 4 + " #  " + "##  " + "#   ", 
         "J0": " " * 8 + "#   " + "### ", "J1": " " * 4 + "##  " + "#   " + "#   ", "J2": " " * 8 + "### " + "  # ", "J3": " " * 4 + " #  " + " #  " + "##  ",
         "L0": " " * 8 + "  # " + "### ", "L1": " " * 4 + "#   " + "#   " + "##  ", "L2": " " * 8 + "### " + "#   ", "L3": " " * 4 + "##  " + " #  " + " #  "}
lowestpoints = {}

def input():
    # strboard = sys.argv[1]
    strboard = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
    return strboard

def getFancyBoard(board):
    toPrintBoard = "========================\n"
    for h in range(0, 20):
        toPrintBoard += "| "
        for w in range(10):
            place = h*10+w
            toPrintBoard += board[place:place+1]
            toPrintBoard += " "
        toPrintBoard += "| " + "{}".format(20-h) + "\n"
    toPrintBoard += "========================\n\n"
    toPrintBoard += "  0 1 2 3 4 5 6 7 8 9"
    return toPrintBoard

def printFancyBoard(board):
    print(getFancyBoard(board))

def printTypes():
    for i in types:
        for x in range(1, len(types[i])+1):
            if(x%4 == 0):
                print(types[i][x-1:x])
            else:
                print(types[i][x-1:x], end = "")
        print()

def printPiece(i):
    for x in range(1, len(types[i])+1):
        if(x%4 == 0):
            print(types[i][x-1:x])
        else:
            print(types[i][x-1:x], end = "")

def getColHeights(board):
    cH = []
    for w in range(10):
        for h in range(20):
            index = w + (h*10)
            if(board[index:index+1] == "#"):
                cH.append(20-h)
                break
    return cH
        

def output(board):
    with open("tetrisout.txt", "a") as r:
        for i in types:
            colHeights = getColHeights(board)
            powsibilities = addPiece(board, i, colHeights)
            for b in powsibilities:
                if(b[0] == None):
                    r.write("GAME OVER\n")
                else:
                    r.write(b[0] + "\n")


def getHeight(piece): #returns maxblockH, then other heights relative
    block = types[piece]
    maxblockH = 0
    for x in range(4):
        if("#" in block[x*4:x*4+4]):
            maxblockH = 4-x
            break
    
    heightList = [maxblockH, 0]
    indicator = 0
    for h in reversed(range(4)):
        index = h*4
        if(block[index:index+1] == "#"):
            indicator = 4-h
            break

    for w in range(1, 4):
        for h in reversed(range(4)):
            index = w + (h*4)
            if(block[index:index+1] == "#"):
                bruh = 4-h
                heightList.append(bruh-indicator)
                break
    
    return heightList

def getLHeight(piece):
    block = types[piece]
    count = 0
    start = 0
    startreached = False
    for h in reversed(range(4)):
        index = (h*4)
        if(block[index:index+1] == "#"):
            count+=1
            if(startreached == False):
                start = 4-h-1
                startreached = True
    return [count, start]

def getTop(piece, startpoint):
    block = types[piece]
    tops = []
    # leftheight = 4 - leftmostheight
    for w in range(1, 4):
        temptop = 0
        for h in range(4):
            index = w + (h*4)
            if(block[index:index+1] == "#"):
                temptop = 4 - h - (startpoint+1)
                break
        tops.append(temptop)
    return tops


def addPiece(board, piece, colHeights):
    pieceheights = getHeight(piece)
    indexes = []
    thiccc = 10 - (len(pieceheights)-2)
    pain = getLHeight(piece)
    leftmostheight = pain[0]
    startpoint = pain[1]
    tops = getTop(piece, startpoint)
    for w in range(thiccc):
        # if(max(tops) + leftmostheight + colHeights[w]> 20):
        #     indexes.append(-1)
        # else:
        if(len(pieceheights) < 3):
            tempind = colHeights[w]+1
            if(tempind + pieceheights[0] -1 > 20):
                indexes.append(-1)
            else:
                indexes.append(tempind)
        else:
            tempind = colHeights[w]-1
            for h in range(2, len(pieceheights)):
                newCand = 0
                if(pieceheights[1] < pieceheights[h]):
                    if(colHeights[w+h-1] > colHeights[w]):
                        if(colHeights[w] - colHeights[w+h-1] <= (pieceheights[h]* -1)):
                            newCand = colHeights[w+h-1] + 1 - pieceheights[h]
                        else:
                            newCand = colHeights[w+h-1]
                    else:
                        newCand = colHeights[w] + 1
                elif(pieceheights[1] > pieceheights[h]):
                    if(colHeights[w] > colHeights[w+h-1]):
                        if(colHeights[w] - colHeights[w+h-1] >= (pieceheights[h]*-1)):
                            newCand = colHeights[w] + 1 - (pieceheights[h]*-1)
                        else:
                            newCand = colHeights[w+h-1]
                    else:
                        newCand = colHeights[w+h-1] + 1
                else:
                    newCand = max(colHeights[w+h-1], colHeights[w]) + 1 - startpoint
                if(newCand > tempind):
                    tempind = newCand
            indexes.append(tempind)
    # print(indexes)
    boardsList = []
    for i in range(len(indexes)):
        tempboard = placePieces(board, indexes[i], i, piece)
        # printFancyBoard(tempboard)
        toReturnBoard = tempboard
        if(tempboard != "GAME OVER" and tempboard != None):
            toReturnBoard = removeLines(tempboard)
        # printFancyBoard(toReturnBoard)
        boardsList.append(toReturnBoard)
    return boardsList

def placePieces(board, indexR, indexC, piece):
    initR = 4
    initC = 1
    toReturnBoard = board
    piecestr = types[piece]
    if(indexR != -1):
        bigR = 20 - indexR
        boardPivInd = (bigR * 10) + indexC
        for r in reversed(range(4)):
            #use the bottom left corner as the pivot and go from there
            #go by row, botom to top.
            if(boardPivInd < 0 and "#" in piecestr[4*r:4*r + 3]):
                toReturnBoard = "GAME OVER"
                break
            else:
                for c in range(4):
                    piecePivInd = 4 * r
                    if(piecestr[piecePivInd+c:piecePivInd+c+1] == "#"):
                        toReturnBoard = toReturnBoard[:boardPivInd+c] + piecestr[piecePivInd+c:piecePivInd+c+1] + toReturnBoard[boardPivInd+c+1:]
                    # [boardPivInd+c:boardPivInd+c+1]
            boardPivInd -= 10
        return toReturnBoard
    else:
        return None

def removeLines(board):
    newboard = board
    linesRemoved = 0
    for r in range(0, len(newboard), 10):
        if(newboard[r:r+10] == "##########"):
            newboard = " " * 10 + newboard[0:r] + newboard[r+10:]
            r-=10
            linesRemoved+=1
    return (newboard, linesRemoved)

#reminder:  1  row  cleared  -->  40  points,  2  -->  100,  
#           3  -->  300,  4  -->  1200 return  points
def playGame(strategy):
    board = makeBoard()
    points = 0
    while(board != "GAME OVER"):
        piece = random.choice(list(types))
        possboards = placePieces(piece)
        boardScores = []
        for i in possboards:
            boardScores.append(heuristic(i, strategy))


    

def makeBoard():
    return " " * 200

def heuristic(board, strategy):
    a, b, c, d, e = strategy
    value = 0
    value += a * max(getColHeights(board))
    value += b * getMaxWell(board)
    value += c * getHoles(board)

def getMaxWell(board):
    wellDepths = []
    for w in range(10):
        wellDepth = 0
        for h in reversed(range(20)):
            index = w + (h*10)
            if(int((index-1)/10) != int(index/10) and board[index+1:index+2] == "#" and board[index:index+1] == " "):
                wellDepth += 1
            elif(int((index-1)/10) == int(index/10) and board[index-1:index] == "#" and board[index+1:index+2] == "#" and board[index:index+1] == " "):
                wellDepth += 1
            elif(board[index:index+1] == "#"):
                wellDepth = 0
        wellDepths.append(wellDepth)
    print(wellDepths)
    return max(wellDepths)

def getHoles(board):
    holes = 0
    for w in range(10):
        for h in reversed(range(1, 20)):
            index = w + (h*10)
            if(board[index:index+1] == " " and board[index-10:index-9] == "#"):
                holes += 1
    print(holes)
    return holes


strboard = input()


# printFancyBoard(strboard)
# colHeights = getColHeights(strboard)
# printPiece("L0")
# powsibilities = addPiece(strboard, "L0", colHeights)
# for board in powsibilities:
#         printFancyBoard(board)

# output(strboard)

printFancyBoard(strboard)
colHeights = getColHeights(strboard)
printPiece("L0")

getMaxWell(strboard)
getHoles(strboard)
