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

def inp1():
    epochs = 3
    trainfile = "data.txt"
    return (epochs, trainfile)

def getTrainSet(file):
    toReturn = []
    with open(file, "r") as r:
        for line in r:
            temp = line.strip()
            toReturn.append(temp)
    return toReturn

def videonetwork():
    w1 = np.array([[1, -.5], [1,.5]])
    w2 = np.array([[1, 2], [-1, -2]])
    b1 = np.array([1, -1])
    b2 = np.array([-.5, .5])
    return ([w1, w2], [b1, b2])

def f(n):
    asdf = 1 / (1+math.e**(-1 * n))
    return asdf

def fprime(n):
    asdf = (math.e**(-1*n))/(1+(math.e**(-1 * n))**2)
    return asdf

def findError(x, y, wList, bList):
    vectorizedF = np.vectorize(f)
    ai = np.array(x)
    for i in range(len(wList)):
        ai = ai.transpose()
        # print(ai)
        wi = wList[i]
        bi = bList[i]
        temp = ai@wi + bi
        ai = vectorizedF(temp)
        # print(ai)
        # print("temp: ", temp)
    asdf = 0
    for i in range(len(y)):
        asdf += ((1/2) * (y[i]-ai[i])**2)
    yes = []
    vecX = np.array(x)
    vecY = np.array(y)
    for w in range(len(wList)):
        val = (vecX - vecY) * fprime(wList[w]@x+bList[w])
        yes.append(val)

    newWList = []
    for i in range(len(wList)):
        partialderiv = yes[i]
        newweight = wList[i] + (yes[i] * LAMBDA)
        newWList.append(newweight)

    newBList = []
    for i in range(len(bList)):
        newB = bList[i] + (yes[i] * LAMBDA)
        newBList.append(newB)

    return (asdf, newWList, newBList)


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
    return values

# inputs = inp1()
vals1 = [2, 3]
vals2 = [.8, 1]
stuff = videonetwork()
wL = stuff[0]
bL = stuff[1]
sheesh = findError(vals1, vals2, wL, bL)
print(sheesh)
temp = sheesh[1]
temp2 = sheesh[2]
sheesh2 = findError(vals1, vals2, temp, temp2)
print(sheesh2)
