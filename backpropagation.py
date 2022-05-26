
from statistics import stdev
import sys
from  math  import  log
import string
import random
import itertools
import ast
import numpy as np
import math


def videonetwork():
    w1 = np.array([[-1, -.5], [1,.5]])
    w2 = np.array([[1, 2], [-1, -2]])
    b1 = np.array([1, -1])
    b2 = np.array([-.5, .5])

def f(n):
    asdf = 1 / (1+math.e**(-1 * n))
    return asdf

def backprop(epochs, trainset, wList, bList):
    values = []
    for i in range(epochs):
        vectorizedF = np.vectorize(f)
        for x, y in trainset:
            ai = np.array(x)
            ai = ai.transpose()
            for i in range(len(wList)):
                wi = wList[i]
                bi = bList[i]
                temp = ai@wi + bi
                ai = vectorizedF(temp)
            asdf = ai[0]
            if(asdf > .5):
                asdf = 1
            else:
                asdf = 0
            values.append((x, y), asdf)