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


def getHeights(board):
    heights = []
    for w in range(10):
        for h in range(20):
            index = w + (h*10)
            if(board[index:index+1] == "#"):
                heights.append(20-h)
                break
    return heights
        

def output(strboard):
    with open("tetrisout.txt", "a") as r:
        r.write(printFancyBoard(strboard))


def addPiece(board, piece):
    block = types[piece]
    maxblockH = 0
    for x in range(4):
        if(block[x:x+1] == "#"):
            
    for i in range(10):

    return "Alan"


strboard = input()
printFancyBoard(strboard)
# printTypes()
print(getHeights(strboard))