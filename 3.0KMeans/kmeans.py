from statistics import stdev
import sys
from  math  import  log
import string
import random
import math as Math

from numpy import double

values = []
K = 6

def getStarData(file):
    toReturn = []
    count = 0
    with open(file, "r") as r:
        for line in r:
            if(count > 0):
                temp = line.strip()
                thing = tuple(temp.split(","))
                new = []
                for i in range(3):
                    val = log(float(thing[i]))
                    new.append(val)
                new.append(float(thing[3]))
                new.append(int(thing[4]))
                values.append(tuple(new))
            else:
                count += 1


def distance(x1, x2, y1, y2):
    dist = Math.sqrt((x2 - x1)**2+(y2-y1)**2)
    return dist

def initmeans():
    centroidsDict = getCentroids()
    for i in values:
        errorlist = []
        for cent in centroidsDict:
            err = error(i, cent)
            errorlist.append((err, cent))
        best = min(errorlist)
        bestcent = best[1]
        centroidsDict[bestcent].append(i)
    return centroidsDict

def kmeans(prevDict):
    oldmeans = []
    for i in prevDict.keys():
        oldmeans.append(i)
    newmeans = []
    newDict = {}
    while(newmeans != oldmeans):
        oldmeans = newmeans
        newmeans = []
        for i in prevDict.keys():
            nwm = getMeans(prevDict[i])
            newmeans.append(tuple(nwm))
        for i in newmeans:
            newDict[i] = []
        for i in values:
            errorlist = []
            for cent in newmeans:
                err = error(i, cent)
                errorlist.append((err, cent))
            best = min(errorlist)
            bestcent = best[1]
            newDict[bestcent].append(i)
        prevDict = newDict
        newDict = {}

    finalDict = {}
    for i in newmeans:
        finalDict[i] = []
    for i in values:
        errorlist = []
        for cent in newmeans:
            err = error(i, cent)
            errorlist.append((err, cent))
        best = min(errorlist)
        bestcent = best[1]
        finalDict[bestcent].append(i)

    return finalDict
        

def getMeans(lst):
    totalvals = [0,0,0,0]
    for v in range(len(lst)):
        cent = lst[v]
        for i in range(len(cent)-1):
            totalvals[i] += cent[i]
    newcents = []
    for i in totalvals:
        newcents.append(i/len(lst))
    return newcents
        
        
def error(s1, s2):
    total = 0
    for i in range(len(s1)-1):
        total += abs(float(s1[i]) - float(s2[i]))
    total = total**2
    return total

def getCentroids():
    cent = random.sample(values, K)
    toReturn = {}
    for i in cent:
        toReturn[i] = []
    return toReturn

def printStars(d):
    count = 0
    for i in d.values():
        print(count, ":", end = '')
        for x in i:
            print(x[4], "", end = '')
        print()
        count+=1
            

getStarData("star_data.csv")
# print(values)
d = kmeans(initmeans())
printStars(d)