from statistics import stdev
import sys
from  math  import  log
import string
import random
import itertools
import ast
import numpy as np
import math

LAMBDA = 1



def inputperp4():
    point = sys.argv[1]
    point = ast.literal_eval(point) 
    return point

def f(n): 
    return 1 if n > 0 else 0 

def p_net(A, x, w_list, b_list):
    vectorizedF = np.vectorize(A)
    ai = np.array(x)
    ai.transpose()
    for i in range(len(w_list)):
        wi = w_list[i]
        bi = b_list[i]
        temp = ai@wi + bi
        ai = vectorizedF(temp)
    return ai[0]

def configureXOR():
    b1 = np.array([-10, 30])
    b2 = np.array([-30])

    w1 = np.array([[20, -20], [20, -20]])
    w2 = np.array([[20], [20]])
    weightList = []
    weightList.append(w1)
    weightList.append(w2)
    biasList = []
    biasList.append(b1)
    biasList.append(b2)
    return (weightList, biasList)

def truthT(bits, n):
    tempN = bin(n)
    binaryNum = tempN[2:]
    while(len(binaryNum) < 2**bits):
        binaryNum = "0" + binaryNum
    # print(binaryNum)
    toReturn = []
    zeTruth = list(itertools.product([0, 1], repeat=bits))
    zeTruth.sort(reverse = True)

    for i in range(len(binaryNum)):
        val = binaryNum[i:i+1]
        bigman = zeTruth[i]
        toReturn.append((bigman, int(val)))
    return toReturn

def printFancyT(table):
    bruh = table[0]
    bruh1 = bruh[0]
    print(" ", end = "")
    for i in range(len(bruh1)):
        print("In", i, end = " ")
    print(" | Output ")

    for i in range(len(table)):
        temp = table[i]
        bigmen = temp[0]
        val = temp[1]
        print("  ", end = "")
        for i in bigmen:
            print(i, "   ", end = "")
        print("| ", val, end = "")
        print()

def getInput(bits):
    zeTruth = list(itertools.product([0, 1], repeat=bits))
    zeTruth.sort(reverse = True)
    return zeTruth

def runXOR(wL, bL):
    inps = getInput(2)
    print("Perceptrons XOR Values: ")
    #XOR HAPPENS HERE
    for i in inps:
        v = p_net(f, i, wL, bL)
        print(i, v)

def configureDiamond():
    b1 = np.array([1, 1, 1, 1])
    b2 = np.array([-3.5])

    w1 = np.array([[-1, 1, -1, 1], [1,-1,-1,1]])
    w2 = np.array([1,1,1,1])
    weightList = []
    weightList.append(w1)
    weightList.append(w2)
    biasList = []
    biasList.append(b1)
    biasList.append(b2)
    return (weightList, biasList)

def configureCircle():
    # b1 = np.array([-1, -1, -1, -1])
    b1 = np.array([2, 2, 2, 2])
    b2 = np.array([-3.5])

    w1 = np.array([[-1, 1, -1, 1], [1,-1,-1,1]])
    w2 = np.array([1,1,1,1])
    weightList = []
    weightList.append(w1)
    weightList.append(w2)
    biasList = []
    biasList.append(b1)
    biasList.append(b2)
    return (weightList, biasList)

def runDiamond(inputs, wL, bL):
    print("Perceptrons Diamond Values: ")
    for i in inputs:
        v = p_net(f, i, wL, bL)
        print(i, v)

def runCircle(wL, bL):
    print("Perceptrons Circle Values: ")
    inpoots = getCircInputs()
    actual = False
    totalTrue=0
    for i in inpoots:
        v = p_net_sigmoid(f2, i, wL, bL)
        if(i[0]**2+i[1]**2 <1):
            actual = True
        else:
            actual = False
        
        if(actual == True and v == 1):
            totalTrue+=1
        elif(actual == False and v==0):
            totalTrue+=1
        else:
            totalTrue+=0
        print(i, v, "Actual", actual)
    print("Accuracy: ", totalTrue/500)

def f2(n): 
    asdf = 1 / (1+math.e**(-1 * n))
    print(asdf)
    if(asdf > .5):
        asdf = 1
    else:
        asdf = 0
    return asdf

def p_net_sigmoid(A, x, w_list, b_list):
    vectorizedF = np.vectorize(A)
    ai = np.array(x)
    ai = ai.transpose()
    for i in range(len(w_list)):
        wi = w_list[i]
        bi = b_list[i]
        temp = ai@wi + bi
        ai = vectorizedF(temp)
    return ai[0]

def getCircInputs():
    toReturn = []
    for i in range(500):
        toReturn.append((random.uniform(0, 1), random.uniform(0, 1)))

    return toReturn
t = configureXOR()
wL = t[0]
bL = t[1]
runXOR(wL, bL)

vb = configureDiamond()
wLD = vb[0]
bLD = vb[1]
runDiamond([(1, 1), (1, 0), (0, 1), (0,0)], wLD, bLD) #not inclusive
# runNetwork([(0,0)], wLD, bLD)

c = configureCircle()
cc = vb[0]
ccc = vb[1]
runCircle(cc, ccc)
