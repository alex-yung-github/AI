from statistics import stdev
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
NUM_TRIALS = 5
STRATEGY_PARAM = 5
POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNEY_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_POINTS = 2
MUTATION_RATE = .8

def getInput():
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
        tempcH = 0
        for h in range(20):
            index = w + (h*10)
            if(board[index:index+1] == "#"):
                tempcH = 20-h
                break
        cH.append(tempcH)
    return cH
        

def output(board):
    with open("tetrisout.txt", "a") as r:
        for i in types:
            colHeights = getColHeights(board)
            powsibilities = addPiece(board, i, colHeights)
            for b in powsibilities:
                if(b[0] == None or b[0] == "GAME OVER"):
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
                            newCand = colHeights[w+h-2]
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
        toReturnBoard = (tempboard, 0)
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
    while(board != "GAME OVER" and board != None):
        piece = random.choice(list(types))
        colHeights = getColHeights(board)
        possboards = addPiece(board, piece, colHeights)
        boardScores = heuristicscoring(possboards, strategy)
        best = max(boardScores)
        if(best[1] == "GAME OVER" or best[1] == "None"):
            break
        points += getPoints(best[2])
        board = best[1]
    return (board, points)

def heuristicscoring(possboards, strategy):
    toReturn = []
    for i in possboards:
        # printFancyBoard(i[0])
        toReturn.append(heuristic(i, strategy))
    return toReturn

def sortFix(num):
    if(num < 0):
        num = -1 * (1+num)
    return num

def getPoints(removedLines):
    pts = 0
    if(removedLines == 1):    
        pts = 40
    elif(removedLines == 2):
        pts = 100
    elif(removedLines == 3):
        pts = 300
    elif(removedLines == 4):
        pts = 1200
    return pts

def makeBoard():
    return " " * 200

def heuristic(boardinfo, strategy):
    board = boardinfo[0]
    linesRemoved = boardinfo[1]
    if(board == "GAME OVER" or board == None):
        return (-10000, "GAME OVER", linesRemoved)
    else:
        a, b, c, d, e = strategy
        value = 0
        value += a * max(getColHeights(board))
        value += b * getMaxWell(board)
        value += c * getHoles(board)
        value += d * linesRemoved
        value += e * getFlatness(board)
        value = float(value)
        return (value, board, linesRemoved)

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
            elif(int((index+1)/10) != int(index/10) and board[index-1:index] == "#" and board[index:index+1] == " "):
                wellDepth +=1
            elif(board[index:index+1] == "#"):
                wellDepth = 0
        wellDepths.append(wellDepth)
    return max(wellDepths)

def getHoles(board):
    holes = 0
    for w in range(10):
        for h in reversed(range(1, 20)):
            index = w + (h*10)
            if(board[index:index+1] == " " and board[index-10:index-9] == "#"):
                holes += 1
    # print(holes)
    return holes

def getFlatness(board): #gets sample standard deviation, not population
    std = stdev(getColHeights(board))
    return std

def population(n):  #gets n number of strategies
    toReturn = []
    for x in range(n):
        randomlist = []
        for i in range(STRATEGY_PARAM):
            randomlist.append(random.uniform(-1, 1))
        toReturn.append(randomlist)
    return toReturn

def fitness(strategy): #returns score of board across 5 games
    game_scores = []
    for count in range(NUM_TRIALS):
        game = playGame(strategy)
        gamescore = game[1]
        game_scores.append(gamescore)
    return sum(game_scores)/len(game_scores)

def selection(sortedStrats): #selects 2 of the population of strategies based on score
    nextGen = []
    #add some top current gen to nextgen
    for i in range(0, NUM_CLONES):
        nextGen.append(sortedStrats[i])
    
    tourney = random.sample(sortedStrats, TOURNEY_SIZE*2)
    t1 = tourney[:len(tourney)//2]
    t2 = tourney[len(tourney)//2:]
    t1.sort(reverse = True)
    t2.sort(reverse = True)
    parents = []
    for i in t1:
        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            parents.append(i[1])
            break

    for i in t2:
        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            parents.append(i[1])
            break
    
    return parents

def breeding(parents):
    p1 = parents[0]
    p2 = parents[1]
    child = []
    indices = list(range(0, len(p1)))
    crossovers = random.sample(indices, CROSSOVER_POINTS)
    for i in range(len(p1)):
        if(i in crossovers):
            child.append(p1[i])
        else:
            child.append(p2[i])
    
    return child

def mutation(child):
    m = random.random()
    # print(m)
    mutatedchild = child.copy()
    if(m < MUTATION_RATE):
        indices = list(range(0, len(child)))
        crossovers = random.sample(indices, 1)
        num = crossovers[0]
        mutatedchild[num] = random.uniform(-1, 1)
    return mutatedchild


def dotheprocess():
    cInit = population(500)
    cScoresInit = []
    netscores = []
    for i in range(len(cInit)):
        score = fitness(cInit[i])
        cScoresInit.append((score, cInit[i]))
        netscores.append(score)
        print("Evaluating Strategy Number", i + 1, "-->", score)
    best = max(cScoresInit)
    print("Average Score: ", sum(netscores)/len(netscores), )
    print("Best Strategy and Score: ", best[1], "with", best[0], "points")

    return cScoresInit
    # return cInit

def dotheprocesspt2(cInit):
    cScoresInit = []
    netscores = []
    for i in range(len(cInit)):
        score = fitness(cInit[i])
        cScoresInit.append((score, cInit[i]))
        netscores.append(score)
        print("Evaluating Strategy Number", i + 1, "-->", score)
    best = max(cScoresInit)
    print("Average Score: ", sum(netscores)/len(netscores), )
    print("Best Strategy and Score: ", best[1], "with", best[0], "points")
    # print(cScoresInit)
    # bestcipher = cScoresInit[0][1]
    # print(bestcipher)
    return cScoresInit

def genAlg(cScoresInit):
    cScoresInit.sort(reverse = True)
    newgen = []
    for i in range(POPULATION_SIZE):
        newSel = selection(cScoresInit)
        newChild = breeding(newSel)
        newMutChild = mutation(newChild)
        newgen.append(newMutChild)
    cScoresInit = newgen
    return cScoresInit

def stowaway(thing, filename):
    print(thing)
    with open(filename, "a") as r:
        for i in thing:
            score = i[0]
            strategee = i[1]
            r.write(str(score) + " ")
            for strat in strategee:
                r.write(str(strat) + " ")
            r.write("\n")
            
def creak(file):
    toReturn = []
    with open(file, "r") as r:
        for line in r:
            temp = line.strip()
            thing = temp.split(" ")
            score = thing[0]
            strat = thing[1:len(thing)]
            toReturn.append((score, strat))
    return toReturn


def userInput():
    decision = input("Start (N)ew or (L)oad Saved: ")
    if(decision == "N"):
        end = dotheprocess()
        newdecision = "C"
        while(newdecision == "C"):
            newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")
            if(newdecision == "S"):
                filename = input("What filename? ")
                stowaway(end, filename)
                break
            elif(newdecision == "P"):
                playGame(end[0][1])
                newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")
            elif(newdecision == "C"):
                end = genAlg(end)
                dotheprocesspt2(end)
    elif(decision == "L"):
        file = input("What filename? ")
        end = creak(file)
        newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")
        if(newdecision == "S"):
            filename = input("What filename? ")
            stowaway(end, filename)
            return
        elif(newdecision == "C" or newdecision == "P"):
            end = genAlg(end)
            end = dotheprocesspt2(end)
            newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")
            while(newdecision == "C" or newdecision == "P"):
                if(newdecision == "S"):
                    filename = input("What filename? ")
                    stowaway(end, filename)
                    break
                elif(newdecision == "P"):
                    playGame(end[0][1])
                    newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")
                elif(newdecision == "C"):
                    end = genAlg(end)
                    end = dotheprocesspt2(end)
                    newdecision = input("(P)lay game with current strategy, (S)ave current progress, or (C)ontinue?: ")


        
        



# strboard = getInput()

# printFancyBoard(strboard)
# colHeights = getColHeights(strboard)
# printPiece("L0")
# powsibilities = addPiece(strboard, "L0", colHeights)
# for board in powsibilities:
#         printFancyBoard(board)

# output(strboard)

userInput()
