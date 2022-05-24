from statistics import stdev
import sys
from  math  import  log
import string
import random
import itertools
import ast


def input():
    rep = int(sys.argv[1])
    weight = sys.argv[2]
    bias = sys.argv[3]
    weight = ast.literal_eval(weight) 
    bias = ast.literal_eval(bias)
    return (rep, weight, bias)

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

def perceptron(A, w, b, x):
    wx = 0
    for i, j in zip(w, x):
            wx += i * j
    wxb = wx+b
    return A(wxb)

def step(num):
    if(num > 0):
        return 1
    else:
        return 0

def check(n, w, b):
    truth = truthT(len(w), n)
    # printFancyT(truth)
    inp = list(itertools.product([0, 1], repeat=len(w)))
    inp.sort(reverse = True)
    end = []
    for i in inp:
        val = perceptron(step, w, b, i)
        end.append(val)
    correct = 0
    for i in range(len(truth)):
        vals = truth[i]
        trueval = vals[1]
        if(trueval == end[i]):
            correct+=1
    return correct / len(truth)



param = input()
# param = (50101, (3, 2, 3, 1), -4)
final = check(param[0], param[1], param[2])
print(final)
