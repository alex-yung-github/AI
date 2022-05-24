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
    if(difference <= tolerance):
        return (left+right)/2
    range = right-left
    newleft = left + (range/3)
    newright = left + ((2 * range)/3)
    newleftval = f(newleft)
    newrightval = f(newright)
    if(newleftval > newrightval):
        return one_d_minimize(f, newleft, right, tolerance)
    elif(newrightval > newleftval):
        return one_d_minimize(f, left, newright, tolerance)

print(one_d_minimize(fn, -1, 0, 10**-8))