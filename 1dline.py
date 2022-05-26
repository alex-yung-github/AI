from statistics import stdev
import sys
from  math  import  log
import string
import random
import itertools
import ast
import numpy as np
import math

def inputpt1():
    # var = sys.argv[1]
    var = "A"
    return var
    
def funcA(x, y):
    valx = (8 * x) + (-3 * y) + 24
    valy = (-3 * x) + (4 * y) - 20
    return (valx, valy)

# def funcAnormal(x, y):
#     valx = 4 * x**2 - (3 * x * y) + (2 * y**2) + (24 * x) - (20 * y)
#     return valx

# def funcAxDeriv(x, y):
#     valx = (8 * x) + (-3 * y) + 24
#     return valx

# def funcAyDeriv(x, y):
#     valy = (-3 * x) + (4 * y) - 20
#     return valy


def funcB(x, y):
    valx = 2*(x - (y**3))
    valy = 2*((-2 * x * y) + (2 * (y**3)) + y - 1)
    return (valx, valy)

def gradDescpt1(inp, lamb):
    start = (0, 0)
    if(inp == "A"):
        vals = funcA(start[0], start[1])
    elif(inp == "B"):
        vals = funcB(start[0], start[1])
    start = (start[0] - (lamb * vals[0]), start[1] - (lamb * vals[1]))
    changeMag = (math.sqrt(vals[1]**2 + vals[0]**2))
    while(vals[1] != 0 and orderOfMagnitude(changeMag) >-7):
        if(inp == "A"):
            vals = funcA(start[0], start[1])
        elif(inp == "B"):
            vals = funcB(start[0], start[1])
        start = (start[0] - (lamb * vals[0]), start[1] - (lamb * vals[1]))
        changeMag = (math.sqrt(vals[1]**2 + vals[0]**2))
    return (start, vals)

def fn(x):
    val = math.sin(𝑥) + math.sin(3*x) + math.sin(4*x)
    return val

def derivfn(x):
    val = math.cos(x) + 3*math.cos(3*x) + 4 * math.cos(4*x)
    return val

def orderOfMagnitude(number):
    return math.floor(math.log(number, 10))

def one_d_minimize(f, left, right, tolerance):
    difference = abs(left-right)
    # print(difference, left, right)
    if(difference <= tolerance):
        return (left+right)/2
    range = abs(right-left)
    newleft = left + (range/3)
    newright = right - (range/3)
    newleftval = f(newleft)
    newrightval = f(newright)
    if(newleftval > newrightval):
        return one_d_minimize(f, newleft, right, tolerance)
    else:
        return one_d_minimize(f, left, newright, tolerance)
    
def make_funct(a):
    def funct(lamb):
        return fn(a - (lamb * derivfn(a)))
    return funct

# print("1D pt1:", one_d_minimize(fn, -1, 0, 10**-8))
inputs = inputpt1()
if(inputs == "A"):
    value = one_d_minimize(make_funct(0), 0, 1, 10**-8)
    print(value)
    gradDescpt1(inputs, value)
elif(inputs == "B"):
    value = one_d_minimize(make_funct(0), 0, 1, 10**-8)
    print(value)
    gradDescpt1(inputs, value)


# value = one_d_minimize(make_funct(0), 0, .4, 10**-8)
# print(value)
# print(funcB(0, 0))