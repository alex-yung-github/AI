import sys
import time
from random import sample, choice
import math
import random


sudokulist = []
symbolset = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dimensionslist = []
rowcons = {}
colcons = {}
blockcons = {}
indexconstraints = {}

def readFile(file):
    count = 0
    with open(file, "r") as f:
        for line in f:
            tempboard = line.strip()
            sudokulist.append(tempboard)
            dimension = int(math.sqrt(len(line.strip())))
            start = int(math.sqrt(dimension))
            subH = 0
            subW = 0
            for i in range(start, dimension):
                if(dimension % i == 0):
                    temp = dimension / i
                    temp2 = dimension / temp
                    if(temp > temp2):
                        subW = temp
                        subH = temp2
                    else:
                        subW = temp2
                        subH = temp
                    break
            symbolset[count] = []
            for i in range(dimension-9):
                symbolset[count].append(alphabet[i:i+1])
            count+=1
            dimensionslist.append([dimension, subH, subW])


def printBoard(board, dimension, subH, subW):
    count = 0
    for i in board:
        if((count+1) % dimension == 0):
            print(i)
            if((count+1) % (dimension * subH) == 0 and count+1 != len(board)):
                for i in range(dimension-1):
                    print("——", end = "-")
                print()
            count+=1
        else:
            print(i, end = " ")
            if((count+1) % subW == 0):
                print("|", end = " ")
            count+=1


def getNeighbors(board, dimension, subH, subW): #not used
    for col in range(dimension):
        for i in range(dimension):
            place = (i * dimension) + col
            temp = board[place:place+1]
            if(temp != "."):
                if(col not in colcons.keys()):
                    colcons[col] = []
                    colcons[col].append(temp)
                else:
                    colcons[col].append(temp)
    for row in range(dimension):
        for i in range(dimension):
            place = (row * dimension) + i
            temp = board[place:place+1]
            if(temp != "."):
                if(row not in rowcons.keys()):
                    rowcons[row] = []
                    rowcons[row].append(temp)
                else:
                    rowcons[row].append(temp)
    for i in range(dimension * dimension):
        row = int(i / dimension)
        col = i % dimension
        block = int(((int(row / subH)) * subH) + (int(col / subW)))
        temp = board[i:i+1]
        if(temp != "."):
            blockcons[block].append(temp)
    for i in range(dimension * dimension):
        row = int(i / dimension)
        col = int(i % dimension)
        block = int(((int(row / subH)) * subH) + (int(col / subW)))
        indexconstraints[i] = [row, col, block]


def getConstraints(board, dimension, subH, subW):
    for i in range(int(subH * subW)):
        blockcons[i] = []
    for col in range(dimension):
        for i in range(dimension):
            place = (i * dimension) + col
            if(col not in colcons.keys()):
                    colcons[col] = []
                    colcons[col].append(place)
            else:
                 colcons[col].append(place)
    for row in range(dimension):
        for i in range(dimension):
            place = (row * dimension) + i
            if(row not in rowcons.keys()):
                rowcons[row] = []
                rowcons[row].append(place)
            else:
                rowcons[row].append(place)
    for i in range(dimension * dimension):
        row = int(i / dimension)
        col = i % dimension
        block = int(((int(row / subH)) * subH) + (int(col / subW)))
        blockcons[block].append(i)
    # print(rowcons)
    # print("-----------------------------------")
    # print(colcons)
    # print("___________________________________")
    # print(blockcons)
    # print("-----------------------------------")
    cons = {}
    for i in range(dimension * dimension):
        row = int(i / dimension)
        col = int(i % dimension)
        block = int(((int(row / subH)) * subH) + (int(col / subW)))
        tempset = set()
        for x in rowcons[row]:
            tempset.add(x)
        for x in colcons[col]:
            tempset.add(x)
        for x in blockcons[block]:
            tempset.add(x)
        cons[i] = tempset
    return cons


def getSymbols(board, dimension):
    count = 0
    for i in board:
        if(i in alphabet):
            count+=1
    return count


def csp_backtracking(board, dimension, boardnum):
    if(goal_test(board)):
        return board
    var = get_next_unassigned_var(board)
    for val in get_sorted_values(board, dimension, boardnum, var):
        s = list(board)
        s[var] = val
        newboard = "".join(s)
        var_result = csp_backtracking(newboard, dimension, boardnum)
        if(var_result is not None):
            return var_result
    return None


def goal_test(board):
    if("." not in board):
        return True
    return False


def get_next_unassigned_var(board):
    return board.index(".")


def get_sorted_values(board, dimension, boardnum, var):
    randomizer = []
    constrainers = set()
    for i in indexconstraints[var]:
        temp = board[i:i+1]
        if(temp != "."):
            constrainers.add(temp)
    for i in range(1, dimension+1):
        symbols = symbolset[boardnum]
        if(i > 9 and symbols[i-dimension] not in constrainers):
                randomizer.append(symbols[i - dimension])
        if(str(i) not in constrainers and i <= 9):
            randomizer.append(str(i))
    toReturn = random.sample(randomizer, len(randomizer))
    return toReturn
    
#tem = readFile("puzzles_1_standard_easy.txt")
#tem = readFile("puzzles_2_variety_easy.txt")
#tem = readFile("puzzles_3_standard_medium.txt")
file = sys.argv[1]
tem = readFile(file)
count = 0
for i in range(len(sudokulist)):
    boardspecs = dimensionslist[i]
    dimension = int(boardspecs[0])
    subH = int(boardspecs[1])
    subW = int(boardspecs[2])
    rowcons = {} #reset constraints
    colcons = {}
    blockcons = {}
    indexconstraints = getConstraints(sudokulist[i], dimension, subH, subW)
    # tem3 = get_sorted_values(sudokulist[1], dimension, 0)
    # print(tem3)
    # t1 = time.perf_counter()
    tem2 = csp_backtracking(sudokulist[i], dimension, i)
    # t2 = time.perf_counter()
    #print("Line: ", count, "Puzzle:", tem2, "Time:", "%s" % (t2 - t1))
    print(tem2)
    count+=1 
    