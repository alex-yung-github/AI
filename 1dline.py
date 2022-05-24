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

def fn(x):
    val = math.sin(𝑥) + math.sin(3*x) + math.sin(4*x)
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
    
def make_funct(a, b):
    vectorizedF = np.vectorize(fn)
    def funct(lamb):
        return fn(a - (lamb * vectorizedF(a)))
    return funct

print("1D pt1:", one_d_minimize(fn, -1, 0, 10**-8))

bruh1 = make_funct(2, 3)
bruh2 = make_funct(4, 5)
print(one_d_minimize(fn, bruh1(1), bruh2(1), 10**-8))