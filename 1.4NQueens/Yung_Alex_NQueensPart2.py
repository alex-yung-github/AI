import sys
import time
from random import sample, choice
import random

 
def generateflaw(dimension):
    temp = sample(range(0, dimension), dimension)
    return temp
 
 
def countConflicts(board, rownum, dimension):
    count = 0
    diagcol = []
    for i in range(len(board)):
        if i != rownum:
            temp = board[i] + (rownum-i)
            temp2 = board[i] - (rownum-i)
            diagcol.append(temp)
            diagcol.append(temp2)
    tempboard = board.copy()
    tempboard.pop(rownum)
    for i in diagcol:
        if(i == board[rownum]):
            count+=1
    for i in range(len(board)):
        if(board[i] == board[rownum] and i != rownum):
            count+=1
    return count


def printInfo(board, dimension):
    conflicts = 0
    for i in range(dimension):
        conflicts += countConflicts(board, i, dimension)
    print("Board:", board)
    print("Total Conflicts: ", conflicts)
 

def csp_backtracking(board, dimension):
    if(goal_test(board, dimension)):
        return board
    printInfo(board, dimension)
    row = getWorstRow(board, dimension)
    for val in get_sorted_values(board, dimension, row):
        board[row] = val
        var_result = csp_backtracking(board, dimension)
        if(var_result is not None):
            return var_result
    return None
 
 
def find_goal(board):
    temp = board.replace(".", "", 1)
    toReturn = "".join(sorted(temp))
    toReturn = toReturn + "."
    return toReturn
 
 
def goal_test(board, dimension):
    for i in range(len(board)):
        if(countConflicts(board, i, dimension) != 0):
            return False
    return True
 
 
def getWorstRow(board, dimension):
    randomizer = []
    conflictlist = []
    temp = 0
    for i in range(len(board)):
        num = countConflicts(board, i, dimension)
        conflictlist.append(num)
        if(num > temp):
            temp = num
    for i in range(len(board)):
        if(conflictlist[i] == temp):
            randomizer.append(i)
    toReturn = random.choice(randomizer)
    return toReturn
   
 
 
 
def get_sorted_values(board, dimension, row):
    toReturn = []
    conflictlist = []
    randomizer = []
    tempboard = board.copy()
    min = float('inf')
    for i in range(len(tempboard)):
        tempboard[row] = i
        num = countConflicts(tempboard, row, dimension)
        conflictlist.append(num)
        if(num < min and i != board[row]):
            min = num
    for i in range(len(conflictlist)):
        if(conflictlist[i] == min and i != board[row]):
            randomizer.append(i)
    toReturn = random.sample(randomizer, len(randomizer))
    return toReturn
   
def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True
 
totaltime1 = time.perf_counter()
for i in range(32, 37):
    board = []
    dimension = i
    startboard = generateflaw(i)
    print("Initial State:", startboard)
    # t1 = time.perf_counter()
    tem = csp_backtracking(startboard, dimension)
    # t2 = time.perf_counter()
    yes = test_solution(tem)
    # print("Length:", i, "Test: ", yes, "Time", "%s" % (t2 - t1))
    print("Length:", i, "Test Solution: ", yes)
    print()
totaltime2 = time.perf_counter()
print("Total Time", "%s" % (totaltime2 - totaltime1))
 
 
 

