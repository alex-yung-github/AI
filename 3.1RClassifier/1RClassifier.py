from statistics import stdev
import sys
from  math  import  log
import string
import random
import math as Math

from numpy import double
import numpy
from collections import Counter

values = []
attributes = []
thingies = {}
testvals = []
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
                for i in range(5, 7):
                    val = thing[i].strip()
                    val = val.strip("'")
                    val = val.replace(" ", "")
                    val = val.replace("-", "")
                    val = val.lower()
                    new.append(val)
                new.append(int(thing[4]))
                values.append(tuple(new))
            else:
                temp = line.strip()
                thing = tuple(temp.split(","))
                for i in range(5, 7):
                    attributes.append(thing[i])
                count += 1

def getTestData(file):
    toReturn = []
    count = 0
    with open(file, "r") as r:
        for line in r:
            if(count > 0):
                temp = line.strip()
                thing = tuple(temp.split(","))
                new = []
                for i in range(5, 7):
                    val = thing[i].strip()
                    val = val.strip("'")
                    val = val.replace(" ", "")
                    # val = val.replace("-", "")
                    val = val.lower()
                    new.append(val)
                new.append(int(thing[4]))
                testvals.append(tuple(new))
            else:
                count += 1
            


def classifierAlg():
    beeglist = []
    for i in range(len(attributes)):
        assigning = {}
        dd = {}
        for star in values:
            attr = star[i]
            if(attr not in dd):
                dd[attr] = []
            dd[attr].append(star[2])
        totalerrornum = 0
        totalerrordenom = 0
        for trait in dd:
            see = Counter(dd[trait])
            val = see.most_common(1)[0][0]
            specificval = see[val]
            errorRate = (len(dd[trait]) - specificval)/(len(dd[trait]))
            frac = (errorRate).as_integer_ratio()
            totalerrornum += frac[0]
            totalerrordenom += frac[1]
            assigning[trait] = val
        beeglist.append((totalerrornum/totalerrordenom, assigning, attributes[i]))

    bestalg = min(beeglist)
    return bestalg
            
def classify(vals, alg):
    attr = attributes.index(alg[2])
    truealg = alg[1]
    classification = {}
    for i in range(K):
        classification[i] = []
    for i in vals:
        trait = i[attr]
        place = truealg[trait]
        classification[place].append(i[2])
    return classification


getStarData("star_data_training.csv")
c = classifierAlg()
b = c[1]
for i in b:
    print(i, ":", b[i])
getTestData("star_data_test.csv")
d = classify(values, c)
for i in d:
    print(i, ":", d[i])