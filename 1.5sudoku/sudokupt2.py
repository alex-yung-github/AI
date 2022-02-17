import sys
import time
from random import sample, choice
import math
import random
import copy


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
            if(x != i):
                tempset.add(x)
        for x in colcons[col]:
            if(x != i):
                tempset.add(x)
        for x in blockcons[block]:
            if(x != i):
                tempset.add(x)
        cons[i] = tempset
    return cons


def getSymbols(board, dimension):
    count = 0
    for i in board:
        if(i in alphabet):
            count+=1
    return count


def convertStringBoard(board, dimension, boardnum):
    toReturn = {}
    for i in range(len(board)):
        constrainers = set()
        if(board[i:i+1] == "."):
            for con in indexconstraints[i]:
                temp = board[con:con+1]
                if(temp != "."):
                    constrainers.add(temp)
            options = ""
            for kid in range(1, dimension+1):
                symbols = symbolset[boardnum]
                if(kid > 9 and symbols[kid-dimension] not in constrainers):
                    options = options + (symbols[kid - dimension])
                if(str(kid) not in constrainers and kid <= 9):
                    options = options + (str(kid))
            toReturn[i] = options
        else:
            temp = board[i:i+1]
            toReturn[i] = str(temp)


    return toReturn


def futureSight(board):
    indices = []
    for i in board.keys():
        if(len(board[i]) == 1):
            indices.append(i)
        if(len(board[i]) == 0):
            return None
    for i in indices:
        if(len(board[i]) == 0):
            return None 
        temporary = board[i]
        val = temporary[0:1]
        for neighbor in indexconstraints[i]:
            if(val in board[neighbor]):
                index = board[neighbor].index(val)
                string = board[neighbor]
                board[neighbor] = str(string[0:index] + string[index+1:len(string)])
                if(len(board[neighbor]) == 1):
                    indices.append(neighbor)
    return board


def futureSightSingle(board, indices):
    for i in indices:
        if(len(board[i]) == 0):
            return None 
        temporary = board[i]
        val = temporary[0:1]
        for neighbor in indexconstraints[i]:
            if(val in board[neighbor]):
                index = board[neighbor].index(val)
                string = board[neighbor]
                board[neighbor] = str(string[0:index] + string[index+1:len(string)])
                if(len(board[neighbor]) == 1):
                    indices.append(neighbor)
    return board


def assign(newboard, var, val):
    newboard[var] = str(val)
    for i in indexconstraints[var]:
        if(val in newboard[i]):
            index = newboard[i].index(val)
            string = newboard[i]
            newboard[i] = str(string[0:index] + string[index+1:len(string)])


def getStringBoard(board):
    toReturn = ""
    for i in range(len(board)):
        temp = board[i]
        toReturn += temp[0:1]
    return toReturn

def constraintprop(board, dimension, boardnum):
    solved = []
    for i in blockcons:
        temp = blockcons[i]
        allvals = ""
        numlist = []
        for index in temp:
            allvals = allvals + board[index]
        for num in range(1, dimension+1):
            if(num > 9):
                thissymbols = symbolset[boardnum]
                times = allvals.count(thissymbols[num-10])
            else:
                times = allvals.count(str(num))
            if(times == 1):
                if(num > 9):
                    tempsymbols = symbolset[boardnum]
                    numlist.append(tempsymbols[num-10])
                else:
                    numlist.append(num)
        for l in blockcons[i]:
            for n in numlist:
                if(str(n) in board[l]):
                    board[l] = str(n)
                    solved.append(l)
    for i in rowcons:
        temp = rowcons[i]
        allvals = ""
        numlist = []
        for index in temp:
            allvals = allvals + board[index]
        for num in range(1, dimension+1):
            if(num > 9):
                thissymbols = symbolset[boardnum]
                times = allvals.count(thissymbols[num-10])
            else:
                times = allvals.count(str(num))
            if(times == 1):
                if(num > 9):
                    tempsymbols = symbolset[boardnum]
                    numlist.append(tempsymbols[num-10])
                else:
                    numlist.append(num)
        for l in rowcons[i]:
            for n in numlist:
                if(str(n) in board[l]):
                    board[l] = str(n)
                    solved.append(l)
    for i in colcons:
        temp = colcons[i]
        allvals = ""
        numlist = []
        for index in temp:
            allvals = allvals + board[index]
        for num in range(1, dimension+1):
            if(num > 9):
                thissymbols = symbolset[boardnum]
                times = allvals.count(thissymbols[num-10])
            else:
                times = allvals.count(str(num))
            if(times == 1):
                if(num > 9):
                    tempsymbols = symbolset[boardnum]
                    numlist.append(tempsymbols[num-10])
                else:
                    numlist.append(num)
        for l in colcons[i]:
            for n in numlist:
                if(str(n) in board[l]):
                    board[l] = str(n)
                    solved.append(l)
    futureSightSingle(board, solved)


def nonetest(board):
    for i in board:
        if(len(board[i]) == 0):
            return True
    return False

def csp_backtracking(board, dimension, boardnum):
    if(goal_test(board)):
        return getStringBoard(board)
    constraintprop(board, dimension, boardnum)
    var = get_next_unassigned_var(board)
    for val in get_sorted_values(board, var):
        newboard = board.copy()
        assign(newboard, var, val)
        checkedboard = futureSight(newboard)
        if(checkedboard is not None):
            result = csp_backtracking(checkedboard, dimension, boardnum)
            if(result is not None):
                return result
    return None


def goal_test(board):
    for i in range(len(board)):
        if(len(board[i]) != 1):
            return False
    return True


def get_next_unassigned_var(board):
    min = float('inf')
    place = 0
    for i in board:
        if(len(board[i]) < min and len(board[i]) >= 2):
            min = len(board[i])
            place = i
    return place


def get_sorted_values(board, var):
    return board[var]

    
#tem = readFile("puzzles_1_standard_easy.txt")
#tem = readFile("puzzles_2_variety_easy.txt")
#tem = readFile("puzzles_3_standard_medium.txt")
#tem = readFile("puzzles_3_standard_medium_more.txt")
#tem = readFile("puzzles_4_variety_medium.txt")
#tem = readFile("puzzles_5_standard_hard.txt")
#tem = readFile("puzzles_6_variety_hard.txt")
file = sys.argv[1]
tem = readFile(file)
count = 0
#tfirst = time.perf_counter()
for i in range(0, len(sudokulist)):
    boardspecs = dimensionslist[i]
    dimension = int(boardspecs[0])
    subH = int(boardspecs[1])
    subW = int(boardspecs[2])
    rowcons = {} #reset constraints
    colcons = {}
    blockcons = {}
    indexconstraints = getConstraints(sudokulist[i], dimension, subH, subW)
    forwardboard = convertStringBoard(sudokulist[i], dimension, i)
    #t1 = time.perf_counter()
    tem2 = csp_backtracking(forwardboard, dimension, i)
    #t2 = time.perf_counter()
    #print("Line: ", count, "Puzzle:", tem2, "Time:", "%s" % (t2 - t1))
    print(tem2)
    count+=1 
# tlast = time.perf_counter()
# print("Time:", "%s" % (tlast - tfirst))

# boardspecs = dimensionslist[0]
# dimension = int(boardspecs[0])
# subH = int(boardspecs[1])
# subW = int(boardspecs[2])
# printBoard(sudokulist[0], dimension, subH, subW)
# rowcons = {} #reset constraints
# colcons = {}
# blockcons = {}
# indexconstraints = getConstraints(sudokulist[0], dimension, subH, subW)
# forwardboard = convertStringBoard(sudokulist[0], dimension, 0)
# constraintprop(forwardboard, dimension)
# t1 = time.perf_counter()
# tem2 = csp_backtracking(forwardboard, dimension, 0)
# t2 = time.perf_counter()
# print("Line: ", count, "Puzzle:", tem2, "Time:", "%s" % (t2 - t1))