import sys; args = sys.argv[1:]
import math
import random
#py crosswords.py 11x13 27 wordlist.txt H0x0begin V8x12end
#py crosswords.py 6x6 36 wordlist.txt
file = ""
d1 = 0 #rows
d2 = 0 #cols
blockingsquares = 0
dictionaryfile = ""
startingstrings = []
numbers = "1234567890"
# visitedboards = []
# visitedindexes = []
likemean = 0

def getInput(input):
    global d1, d2, blockingsquares, dictionaryfile, likemean
    size = (input[0])
    sizexindex = size.index("x")
    d1 = int(size[0:sizexindex])
    d2 = int(size[sizexindex+1:])
    blockingsquares = int(input[1])
    # dictionaryfile = input[2]
    # likemean = 7
    for i in range(2, len(input)):
        temp = input[i]
        orientation = temp[0:1]
        xindex = temp.index("x")
        firstdimension = temp[1:xindex]
        seconddimension = ""
        finalindex = xindex + 1
        for x in range(xindex+1, len(temp)):
            if(temp[x:x+1] not in numbers):
                break
            seconddimension += temp[x:x+1]
            finalindex+=1
        word = temp[finalindex:]
        startingstrings.append((orientation, int(firstdimension), int(seconddimension), word))

def getInputDebug():
    global d1, d2, blockingsquares, dictionaryfile, likemean
    # size = "11x13"
    size = "9x26"
    sizexindex = size.index("x")
    d1 = int(size[0:sizexindex])
    d2 = int(size[sizexindex+1:])
    # blockingsquares = 27
    blockingsquares = 42
    dictionaryfile = "wordlist.txt"
    # ss = ["H0x0Mute", "V0x0mule", "V10x13Hicks", "H7x5#", "V3x4#", "H6x7#", "V11x3#"]
    # likemean = ((d1 * d2)/blockingsquares)
    # print(likemean)
    #9x16 32 V5x0# V8x3# H3x12# V0x9Davenport
    #13x13 32 V2x4# V1x9# V3x2# h8x2#moo# v5x5#two# h6x4#ten# v3x7#own# h4x6#orb# H12x4Polo
    #13x13 27 H6x4no#on v5x5nor v0x0stride h0x4trip H0x9fall V0x12limp
    #9x26 42 h4x10q# h3x7s# h2x7# v2x0eat V5x1#m V8x22f
    #16x16 184 V3x2 H2x3 H4x4 V7x4
    # ss = ["H1x4#Toe#", "H9x2#", "V3x6#", "H10x0Scintillating", "V0x5stirrup", "H4x2##Ordained", "V0x1Baby", "V0x12Emp", "V5x0orb"]
    ss = ["h4x10q#", "h3x7s#", "h2x7#", "v2x0eat", "V5x1#m", "V8x22f"]
    # ss = ["V3x2", "H2x3", "H4x4", "V7x4"]
    # ss = []
    # ss = ["H6x4no#on", "v5x5nor", "v0x0stride", "h0x4trip", "H0x9fall", "V0x12limp"]
    # ss = ["V2x4#", "V1x9#", "V3x2#", "h8x2#moo#", "v5x5#two#", "h6x4#ten#", "v3x7#own#", "h4x6#orb#", "H12x4Polo"]
    # ss = ["V5x0#", "V8x3#", "H3x12#", "V0x9Davenport"]
    # ss = ["H0x0begin"]
    for temp in ss:
        orientation = temp[0:1]
        xindex = temp.index("x")
        firstdimension = temp[1:xindex]
        seconddimension = ""
        finalindex = xindex + 1
        for x in range(xindex+1, len(temp)):
            if(temp[x:x+1] not in numbers):
                break
            seconddimension += temp[x:x+1]
            finalindex+=1
        word = temp[finalindex:]
        startingstrings.append((orientation, int(firstdimension), int(seconddimension), word))

def findNeededInfo(board):
    stringboard = ""
    for i in board.keys():
        for x in range(len(board[i])):
            stringboard += board[i][x][0]
    number = stringboard.count("-")
    bs = stringboard.count("#")
    return(number, bs)


def loading():
    finalboard = {}
    count = 0
    for row in range(d1):
        finalboard[row] = []
        for col in range(d2):
            if(count < int((d1 * d2)/2)):
                finalboard[row].append(("-", True))
            else:
                finalboard[row].append(("-", False))
            count+=1

    for i in startingstrings:
        temp = i
        word = i[3]
        x = i[1]
        y = i[2]
        orientation = i[0]
        if(orientation.lower() == "h"):
            row = finalboard[x]
            for b in range(y, y+len(word)):
                finalboard[x][b] = (word[b-y:b-y+1], False)
                finalboard[d1-x-1][d2-b-1] = (finalboard[d1-x-1][d2-b-1][0], False)
        elif(orientation.lower() == "v"):
            count = x
            for l in word:
                finalboard[count][y] = (l, False)
                finalboard[d1-count-1][d2-y-1] = (finalboard[d1-count-1][d2-y-1][0], False)
                count += 1
    return finalboard
    
def printBoard(board):
    for i in board.keys():
        for x in board[i]:
            print(x[0], "",  end = "")
        print()

def addblockingsquares(board):
    rows = d1
    cols = d2
    newboard = {}
    if((rows * cols) == (blockingsquares)):
        for row in range(d1):
            newboard[row] = ""
            for col in range(d2):
                newboard[row] += "#"
        return (1, newboard)
    elif((rows * cols) % 2 == 0 and blockingsquares % 2 == 1):
        return None
    else:
        if(rows % 2 == 1 and cols % 2 == 1):
            if(blockingsquares % 2 == 1):
                # rr = int(rows/2)
                # cc = int(cols/2)
                temprow = list(board[int(rows/2)])
                temprow[int(cols/2)] = ("#", False)
                newrow = tuple(temprow)
                board[int(rows/2)] = newrow
        if(blockingsquares > int((d1 * d2)/2)):
            for beegrow in range(0, int(d1/4)):
                printBoard(board)
                for beegcol in range(len(board[beegrow])):
                    board = placeBlock(board, (beegrow, beegcol))
                # for nume in range(rr-2, rr - 4, -1):
                #     if(nume < 0):
                #         break
                #     trow = list(board[nume])
                #     trow[cc] = (board[nume][cc][0], False)
                #     board[nume] = tuple(trow)
                # temrow = list(board[rr])
                # for nume in range(cc-3, cc + 4):
                #     if(nume > d2):
                #         break
                #     elif(nume >= 0 and (nume-1) != cc and (nume+1) != cc):
                #         temrow[nume] = (board[rr][nume][0], False)
                # board[rr] = tuple(temrow)
        printBoard(board)
        print()
        board = flipBoard(board)
        printBoard(board)
        print()
        board = fillInImpossibles(board)
        blingbling = connectedCheck(board)
        if(blingbling[1] == False):
            board = connect(board, blingbling[0])
        printBoard(board)
        # printBoard(board)
        # printBoard(board)
        nextmove = csp_backtracking(board, set())
        # print(nextmove)
        # printBoard(nextmove[1])
        return nextmove

def connect(board, filedboard):
    counter = filedboard.count(".")
    indexes = []
    filedboard = filedboard.replace("?", "")
    if(counter > int((d1 * d2)/2)):
        for i in range(int(len(filedboard)/2)):
            if(filedboard[i:i+1] == "-"):
                indexes.append(i)
                
    else:
        for i in range(int(len(filedboard)/2)):
            if(filedboard[i:i+1] == "."):
                indexes.append(i)

    for ind in indexes:
        row = int(ind/d2)
        col = (ind%d2)
        temprow1 = list(board[row])
        temprow1[col] = ("#", temprow1[col][1])
        newrow1 = tuple(temprow1)
        board[row] = newrow1

        inverserow = d1 - row - 1
        inversecol = d2 - col - 1
        temprow2 = list(board[inverserow])
        temprow2[inversecol] = ("#", temprow2[inversecol][1])
        newrow2 = tuple(temprow2)
        board[inverserow] = newrow2


    return board
# def connectHelp(bb, startindex, visited):
#     visited.append(startindex)
#     if(bb[newindex:newindex+1] == "#" or qboard[newindex:newindex+1] == "?"):
#         return qboard
#     else:
#         qboard = qboard[0:newindex] + "." + qboard[newindex+1:]
#         if((newindex+1) not in visited):
#             qboard = checkHelper(qboard, newindex+1, visited)
#         if((newindex-1) not in visited):
#             qboard = checkHelper(qboard, newindex-1, visited)
#         if((newindex+d2+2) not in visited):
#             qboard = checkHelper(qboard, newindex+d2+2, visited)
#         if((newindex-d2-2) not in visited):
#             qboard = checkHelper(qboard, newindex-d2-2, visited)
#         return qboard

def fillInImpossibles(board):
    lenList = []
    for row in range(int(d1/2)+1):
        length = 0
        llind = 0
        bigr = (d2)
        for col in range(bigr):
            if(board[row][col][0] == "#"): 
                if(length > 0 and length < 3):
                    lenList.append((row,llind))
                length = 0
                llind = col
            else:
                length+=1
        if(length > 0 and length < 3):
            lenList.append((row, llind))

    for i in lenList:
        fixrow = i[0]
        fixcol = i[1]
        if(board[fixrow][fixcol][0] == "#"):
            tempfixcol = fixcol+1
        else:
            tempfixcol = fixcol
        while(tempfixcol < d2 and board[fixrow][tempfixcol][0] != "#"):
            if(board[fixrow][tempfixcol][0] != "-" or board[d1-fixrow-1][d2-tempfixcol-1][0] != "-"):
                return None
            temprow1 = list(board[fixrow])
            temprow1[tempfixcol] = ("#", temprow1[tempfixcol][1])
            newrow1 = tuple(temprow1)
            board[fixrow] = newrow1

            inverserow = d1 - fixrow - 1
            inversecol = d2 - tempfixcol - 1
            temprow2 = list(board[inverserow])
            temprow2[inversecol] = ("#", temprow2[inversecol][1])
            newrow2 = tuple(temprow2)
            board[inverserow] = newrow2

            tempfixcol +=1
    newfixList = []

    for c in range(int(d2/2)+1):
        length = 0
        blin = 0
        for r in range(int(d1)):
            temp = board[r]
            if(temp[c][0] == "#"):
                if(length > 0 and length < 3):
                    if(blin > int(d1/2)+1):
                        newfixList.append((d1 - blin - 1, d2 - c - 1, True))
                    else:
                        newfixList.append((blin, c, False))
                length = 0
                blin = r
            else:
                length+=1
        if(length > 0 and length < 3):
            if(blin > int(d1/2)+1):
                newfixList.append((d1 - blin - 1, d2 - c - 1, True))
            else:
                newfixList.append((blin, c, False))

    for i in newfixList:
        ffrow = i[0]
        ffcol = i[1]
        inverse = i[2]
        if(board[ffrow][ffcol][0] == "#"):
            if(inverse == False):
                tempffrow = ffrow+1
            else:
                tempffrow = ffrow-1
        else:
            tempffrow = ffrow
        while(tempffrow >= 0 and tempffrow < d1 and board[tempffrow][ffcol][0] != "#"):
            if(board[tempffrow][ffcol][0] != "-" or board[d1-tempffrow-1][d2-ffcol-1][0] != "-"):
                return None
            temprow1 = list(board[tempffrow])
            temprow1[ffcol] = ("#", temprow1[ffcol][1])
            newrow1 = tuple(temprow1)
            board[tempffrow] = newrow1

            inverserow = d1 - tempffrow - 1
            inversecol = d2 - ffcol - 1
            temprow2 = list(board[inverserow])
            temprow2[inversecol] = ("#", temprow1[ffcol][1])
            newrow2 = tuple(temprow2)
            board[inverserow] = newrow2
            
            if(inverse == False):
                tempffrow += 1
            else:
                tempffrow -=1
    # if(len(lenList) > 0 or len(newfixList) > 0):
    #     return fillInImpossibles(board)
    # else:
    return board

def flipBoard(board):
    for row in board.keys():
        for col in range(len(board[row])):
            if(board[row][col][0] == "#"):
                inverserow = d1 - row - 1
                inversecol = d2 - col - 1
                temprow2 = list(board[inverserow])
                temprow2[inversecol] = ("#", False)
                newrow2 = tuple(temprow2)
                board[inverserow] = newrow2
    return board


def csp_backtracking(board, visitedindexes):
    tempvi = visitedindexes.copy()
    score = goalTest(board)
    if(score == -1):
        return None
    blonblon = connectedCheck(board)
    if(score != None and blonblon[1] == True):
        return (score, board)
    var = getVar()
    scoreslist = []
    posseebelplaces = possiblePlaces(board, var)
    random.shuffle(posseebelplaces)
    for val in posseebelplaces:
        if(val not in tempvi):
            newboard = placeBlock(board, val)
            newboard = fillInImpossibles(newboard)
            var_result = None
            if(newboard != None):
                var_result = csp_backtracking(newboard, tempvi)
            else:
                tempvi.add(val)
            if(var_result is not None):
                return var_result
    # if(len(scoreslist) == 0):
    #     return None
    # else:
    #     return findMin(scoreslist)


def findMin(list):
    min = float('inf')
    place = list[0][1]
    for t in list:
        if(t[0] < min):
            min = t[0]
            place = t[1]
    if(min == float('inf')):
        return None
    return (min, place)

def goalTest(board):
    stringboard = ""
    for r in board.keys():
        for c in board[r]:
            stringboard += c[0]
    count = stringboard.count("#")
    if(count == blockingsquares):
        # return getScore(board)
        return 0
    elif(count > blockingsquares):
        return -1
    else:
        return None

def connectedCheck(board):
    testboard = ""
    for i in board.keys():
        for x in board[i]:
            testboard += x[0]
    originalboard = testboard

    topandbot = ""
    for i in range(d2+1):
        topandbot += "?"
    qboard = topandbot + "??" + testboard + topandbot + "??"
    count = 1
    added = 0
    for i in range(d2+2, len(qboard)-1):
        if(count == (d2+2)):
            qboard = qboard[0:i] + "??" + qboard[i:]
            count = 0
        count+=1
    # printBoardFill2(qboard)
    dex = 0
    for i in range(len(qboard)):
        if(qboard[i:i+1] == "-"):
            dex=i
            break
    filedboard = checkHelper(qboard, dex, [])
    c1 = filedboard.count(".")
    c2 = (d1 * d2) - originalboard.count("#")
    if(c1 == c2):
        return (filedboard, True)
    else:
        return (filedboard, False)
                
def checkHelper(qboard, newindex, visited):
    visited.append(newindex)
    if(qboard[newindex:newindex+1] == "#" or qboard[newindex:newindex+1] == "?"):
        return qboard
    else:
        qboard = qboard[0:newindex] + "." + qboard[newindex+1:]
        if((newindex+1) not in visited):
            qboard = checkHelper(qboard, newindex+1, visited)
        if((newindex-1) not in visited):
            qboard = checkHelper(qboard, newindex-1, visited)
        if((newindex+d2+2) not in visited):
            qboard = checkHelper(qboard, newindex+d2+2, visited)
        if((newindex-d2-2) not in visited):
            qboard = checkHelper(qboard, newindex-d2-2, visited)
        return qboard

def printBoardFill(board):
    tempboard = board.replace("?", '')
    for i in range(1, len(tempboard)+1):
        print(tempboard[i-1:i], "", end = '')
        if(i % d2 == 0):
            print()

def printBoardFill2(board):
    for i in range(1, len(board)+1):
        print(board[i-1:i], "", end = '')
        if(i % (d2+2) == 0):
            print()

def getVar():
    return "#"

def possiblePlaces(board, var):
    toReturn = []
    for row in range(int(len(board.keys())/2)+1):
        colrange = 0
        if(d1 % 2 == 0):
            colrange = int(len(board[row])/2)
        else:
            colrange = len(board[row])
        for col in range(colrange):
            if(board[row][col][1] == True and board[row][col][0] == "-"):
                toReturn.append((row, col))
    return toReturn

def placeBlock(board, place):
    newboard = {}
    for i in board.keys():
        newboard[i] = (board[i])
    row = place[0]
    col = place[1]
    temprow1 = list(newboard[row])
    temprow1[col] = ("#", temprow1[col][1])
    newrow1 = tuple(temprow1)
    newboard[row] = newrow1
    #making it not possible to have # 3 in all directions
    # for nume in range(row+1, row + 4):
    #     if(nume >= d1):
    #         break
    #     trow = list(newboard[nume])
    #     if(nume != row+3  and  nume <= int(d1/2)):
    #         trow[col] = (newboard[nume][col][0], True)
    #     else:
    #         trow[col] = (newboard[nume][col][0], False)
    #     newboard[nume] = tuple(trow)
    # for nume in range(row-1, row - 4, -1):
    #     if(nume < 0):
    #         break
    #     trow = list(newboard[nume])
    #     if(nume != row-3 and nume <= int(d1/2)):
    #         trow[col] = (newboard[nume][col][0], True)
    #     else:
    #         trow[col] = (newboard[nume][col][0], False)
    #     newboard[nume] = tuple(trow)
    # temrow = list(newboard[row])
    # tc = col
    # tr = row
    # for nume in range(col-3, col + 4):
    #     if(nume >= d2):
    #         break
    #     elif(nume < 0):
    #         continue
    #     elif(nume != col-3 and nume != col+3):
    #         temrow[nume] = (newboard[row][nume][0], True)
    #     elif(nume >= 0 and (nume-1) != tc and (nume+1) != tc):
    #         temrow[nume] = (newboard[row][nume][0], False)
    # newboard[row] = tuple(temrow)

    # newboard[row][col] = ("#", newboard[row][col][1])
    # newboard[d1-row-1][d2-col-1] = ("#", newboard[d1-row-1][d2-col-1][1])
    inverserow = d1 - row - 1
    inversecol = d2 - col - 1
    temprow2 = list(newboard[inverserow])
    temprow2[inversecol] = ("#", temprow2[inversecol][1])
    newrow2 = tuple(temprow2)
    newboard[inverserow] = newrow2
    # if(inverserow - (d1/2) < 3):
    #     for nume in range(inverserow-3, inverserow - 4, -1):
    #         if(nume < 0):
    #             break
    #         trow = list(newboard[nume])
    #         trow[inversecol] = (newboard[nume][inversecol][0], False)
    #         newboard[nume] = tuple(trow)
    return newboard

def getScore(board):
    #horizontal
    lenList = []
    for row in board.keys():
        length = 0
        for col in board[row]:
            if(col[0] == "#"): 
                if(length > 0):
                    lenList.append(length)
                    length = 0
            else:
                length+=1
        if(length > 0):
            lenList.append(length)

    for i in lenList:
        if(i < 3):
            return float("inf")

    for c in range(d2):
        length = 0
        for r in board.keys():
            temp = board[r]
            if(temp[c][0] == "#"):
                if(length > 0):
                    lenList.append(length)
                    length = 0
            else:
                length+=1
        if(length > 0):
            lenList.append(length)

    for i in lenList:
        if(i < 3):
            return float("inf")
    
    #find standard deviation of list
    total = sum(lenList)
    mean = (total / len(lenList))
    return mean




# getInputDebug()
# myLines = open(args[0],'r').read().splitlines()
getInputDebug()
# getInput(args)
startboard = loading()

# print()
blockedboard = addblockingsquares(startboard)
if(blockedboard != None):
    printBoard(blockedboard[1])
else:
    print("Impossible Board")


# Alex Yung, 1, 2023


