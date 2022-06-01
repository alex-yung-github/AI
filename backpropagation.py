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
    return ([0, w1, w2], [0, b1, b2])

def f(n):
    asdf = 1 / (1+math.e**(-1 * n))
    return asdf

def fprimo(n):
    asdf = (math.e**(-1*n))/((1+(math.e**(-1 * n)))**2)
    return asdf

def findError(x, y, wList, bList):
    vectorizedF = np.vectorize(f)
    ai = np.array(x)
    outputs = []
    dotList = []
    alist = []
    outputs.append(ai)
    for i in range(1, len(wList)):
        # ai = ai.transpose()
        # print(ai)
        wi = wList[i]
        bi = bList[i]
        temp = ai@wi + bi
        dotList.append(temp)
        ai = vectorizedF(temp)
        outputs.append(ai)
        # print(ai)
        # print("temp: ", temp)

    fprime = np.vectorize(fprimo)
    vecX = np.array(x)
    vecY = np.array(y)
    deltaN = fprime(outputs[-1]) * (vecY - outputs[-1])

    asdf = 0
    for i in range(len(y)):
        asdf += ((1/2) * (y[i]-ai[i])**2)

    deltas = [0] * len(wList)
    deltas[-1] = deltaN
    newWList = []
    newBList = []
    for w in range(len(wList)-2, 0, -1):
        deltaTemp = fprime(dotList[w]) * (deltas[w+1]@(wList[w+1].T))
        # deltaTemp = fprime(ai) * (vecY - ai)
        deltas[w] = deltaTemp

    newBList.append(0)
    newWList.append(0)
    for l in range(1, len(wList)):
        bNew = bList[l] + (LAMBDA*deltas[l])
        wNew = wList[l] + (LAMBDA*((outputs[l-1].T)@deltas[l]))
        newWList.append(wNew)
        newBList.append(bNew)
        

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
print()
print("Run 1: ")
print(sheesh)
print()
temp = sheesh[1]
temp2 = sheesh[2]
sheesh2 = findError(vals1, vals2, temp, temp2)
print("Run 2: ")
print(sheesh2)
print()
