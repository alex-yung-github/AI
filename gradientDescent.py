from multiprocessing.managers import ValueProxy
from statistics import stdev
import sys
from  math  import  log
import string
import random
import itertools
import ast
import numpy as np
import math

LAMBDA = .1

def inputpt1():
    var = sys.argv[1]
    # var = "A"
    return var
    
def funcA(x, y):
    valx = (8 * x) + (-3 * y) + 24
    valy = (-3 * x) + (4 * y) - 20
    return (valx, valy)

def funcB(x, y):
    valx = 2*(x - (y**3))
    valy = 2*((-2 * x * y) + (2 * (y**3)) + y - 1)
    return (valx, valy)

def gradDescpt1(inp):
    start = (0, 0)
    if(inp == "A"):
        vals = funcA(start[0], start[1])
    elif(inp == "B"):
        vals = funcB(start[0], start[1])
    start = (start[0] - (LAMBDA * vals[0]), start[1] - (LAMBDA * vals[1]))
    changeMag = (math.sqrt(vals[1]**2 + vals[0]**2))
    while(vals[1] != 0 and orderOfMagnitude(changeMag) >-7):
        if(inp == "A"):
            vals = funcA(start[0], start[1])
        elif(inp == "B"):
            vals = funcB(start[0], start[1])
        start = (start[0] - (LAMBDA * vals[0]), start[1] - (LAMBDA * vals[1]))
        changeMag = (math.sqrt(vals[1]**2 + vals[0]**2))
    return (start, vals)
    
def orderOfMagnitude(number):
    return math.floor(math.log(number, 10))

# inputLetter = inputpt1()
# # testnum = .0000001
# # print(orderOfMagnitude(testnum))
# beeg = gradDescpt1(inputLetter)
# print("Final Vals: ", beeg[0])
# print("Final Change:", beeg[1])