import sys
import time
from random import sample, choice
import math
import random
import copy


def max_step(board):
    score = goal_test(board)
    if(score != None):
        return score
    results = list()
    for next_board in get_children(board, "X"):
        results.append(min_step(next_board))
    return max(results)


def min_step(board):
    score = goal_test(board)
    if(score != None):
        return score
    results = list()
    for next_board in get_children(board, "O"):
        results.append(max_step(next_board))
    return min(results)


def max_move(board, value):
    temp = get_children(board,"X")
    for next_board in temp:
        if(min_step(next_board) == value):
            print("I choose space", checkDifference(board, next_board))
            return next_board
    return None


def min_move(board, value):
    temp = get_children(board,"O")
    for next_board in temp:
        if(max_step(next_board) == value):
            print("I choose space", checkDifference(board, next_board))
            return next_board
    return None


def minimax(board, current_player):
    if(current_player):
        max = max_step(board)
        return max_move(board, max)
    else:
        min = min_step(board)
        return min_move(board, min)
    

def checkDifference(board, newboard):
    for i in range(len(board)):
        if(board[i:i+1] != newboard[i:i+1]):
            return i

def goal_test(board):
    for i in range(3):
        if(board[(i*3)] == board[(i*3)+1] == board[(i*3)+2] and (board[i*3] == "X" or board[i*3] == "O")):
            if("X" == board[i*3]):
                return 1
            else:
                return -1
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] and (board[i] == "X" or board[i] == "O")):
            if("X" == board[i]):
                return 1
            else:
                return -1
    if(board[0] == board[4] == board[8] and (board[0] == "X" or board[0] == "O")):
        if("X" == board[0]):
            return 1
        else:
            return -1
    if(board[2] == board[4] == board[6] and (board[2] == "X" or board[2] == "O")):
        if("X" == board[2]):
            return 1
        else:
            return -1
    if("." not in board):
        return 0
    return None


def goal_test2(board, comp):
    for i in range(3):
        if(board[(i*3)] == board[(i*3)+1] == board[(i*3)+2] and (board[i*3] == "X" or board[i*3] == "O")):
            if(comp == board[i*3]):
                return 1
            else:
                return -1
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] and (board[i] == "X" or board[i] == "O")):
            if(comp == board[i]):
                return 1
            else:
                return -1
    if(board[0] == board[4] == board[8] and (board[0] == "X" or board[0] == "O")):
        if(comp == board[0]):
            return 1
        else:
            return -1
    if(board[2] == board[4] == board[6] and (board[2] == "X" or board[2] == "O")):
        if(comp == board[2]):
            return 1
        else:
            return -1
    if("." not in board):
        return 0
    return None


def get_children(board, current_player):
    toReturn = []
    for i in range(len(board)):
        if(board[i:i+1] == "."):
            newstring = board[0:i] + current_player + board[i+1:]
            toReturn.append(newstring)
    return toReturn


def printboard(board):
    for i in range(len(board)):
        print(board[i:i+1], end = '')
        if(i == 2 or i == 5):
            print()
            print("—————")
        elif(i == 8):
            print()
        else:
            print("|", end = '')


def printcurrentboard(board):
    print("Current Board: ")
    for i in range(len(board)):
        print(board[i:i+1], end = '')
        if(i == 2 or i == 5):
            if(i == 2):
                print("   012")
            else:
                print("   345")
            print("—————")
        elif(i == 8):
            print("   678")
        else:
            print("|", end = '')


def isEmpty(board):
    for i in board:
        if (i != "."):
            return False
    return True


def isAvailable(board, place):
    if(board[place:place+1] == "."):
        return True
    return False


def getAvailable(board):
    toReturn = []
    for i in range(len(board)):
        if(board[i:i+1] == "."):
            toReturn.append(i)
    return toReturn


def userPlace(board, place, val):
    newstring = board[0:place] + val + board[place+1:]
    return newstring


def gameIsOver(board):
    end = goal_test2(board, computer)
    if(end == -1):
        print("You win!")
        return True
    elif(end == 1):
        print("I win!")
        return True
    elif(end == 0):
        print("It's a tie!")
        return True
    return False

board = sys.argv[1]
# board = "........."
temp = ""
countX = 0
countO = 0
if(isEmpty(board)):
    temp = input("Choose X or O: ")
    while(temp != "O" and temp != "X"):
        temp = input("Not X or O. Choose X or O: ")
else:
    for i in board:
        if(i == "X"):
            countX += 1
        elif(i == "O"):
            countO += 1
    if(countX == countO):
        temp = "O"
    elif(countX > countO):
        temp = "X"
    elif(countX < countO):
        temp = "O"
    
computer = ""
if(temp == "X"):
    computer = "O"
    print("I am O")
else:
    computer = "X"
    print("I am X")

printcurrentboard(board)
print()
while("." in board):
    if(countX > countO and computer == "O"):

        board = minimax(board, False)
        printcurrentboard(board)
        print()
        if(gameIsOver(board)):
            break

        available = getAvailable(board)
        print("Available Spots:", available)
        user = ""
        while(user not in available):
            user = int(input("Your Choice? "))
            print()
        board = userPlace(board, int(user), "X")

        printcurrentboard(board)
        print()
        if(gameIsOver(board)):
            break
    elif(computer == "O"):
        available = getAvailable(board)
        print("Available Spots:", available)
        user = ""
        while(user not in available):
            user = int(input("Your Choice? "))
            print()
        board = userPlace(board, int(user), "X")
        printcurrentboard(board)
        print()

        if(gameIsOver(board)):
            break

        board = minimax(board, False)
        printcurrentboard(board)
        print()
        if(gameIsOver(board)):
            break
    else:
        board = minimax(board, True)
        printcurrentboard(board)
        print()
        if(gameIsOver(board)):
            break

        available = getAvailable(board)
        print("Available Spots:", available)
        user = ""
        while(user not in available):
            user = int(input("Your Choice? "))
            print()
        board = userPlace(board, int(user), "O")

        printcurrentboard(board)
        print()
        if(gameIsOver(board)):
            break
        
    






        