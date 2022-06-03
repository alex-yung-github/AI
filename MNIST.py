import sys
import numpy as np
import math
import pickle

# # write python dict to a file
# mydict = {'a': 1, 'b': 2, 'c': 3}
# output = open('myfile.pkl', 'wb')
# pickle.dump(mydict, output)
# output.close()

# # read python dict back from the file
# pkl_file = open('myfile.pkl', 'rb')
# mydict2 = pickle.load(pkl_file)
# pkl_file.close()

LAMBDA = 1.5
mDataX = []
mDataY = []

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
    b1 = np.array([[1, -1]])
    b2 = np.array([[-.5, .5]])
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
    alist = []
    dotList = []
    alist.append(ai)
    dotList.append(ai)
    for i in range(1, len(wList)):
        # ai = ai.transpose()
        # print(ai)
        wi = wList[i]
        bi = bList[i]
        dot = ai@wi + bi
        dotList.append(dot)
        ai = vectorizedF(dot)
        alist.append(ai)
        # print(ai)
        # print("temp: ", temp)

    fprime = np.vectorize(fprimo)
    vecX = np.array(x)
    vecY = np.array(y)
    deltaN = fprime(dotList[-1]) * (vecY - alist[-1])

    v1 = np.linalg.norm(vecY-ai)
    asdf = (1/2) * (v1**2)
    # for i in range(len(y[0])):
    #     asdf += ((1/2) * (y[0][i]-ai[0][i])**2)

    deltas = [0] * len(wList)
    deltas[-1] = deltaN
    newWList = []
    newBList = []
    for w in range(len(wList)-2, 0, -1):
        deltaL = fprime(dotList[w]) * (deltas[w+1]@(wList[w+1].T))
        # deltaTemp = fprime(ai) * (vecY - ai)
        deltas[w] = deltaL

    newBList.append(0)
    newWList.append(0)
    for l in range(1, len(wList)):
        bNew = bList[l] + (LAMBDA*deltas[l])
        wNew = wList[l] + (LAMBDA*((alist[l-1].T)@deltas[l]))
        newWList.append(wNew)
        newBList.append(bNew)
        
    return (asdf, newWList, newBList)

def realbackprop(epochs, x, y, wList, bList):
    newW = wList
    newB = bList
    print()
    for i in range(32, epochs):
        print("Epoch ", i+1)
        for l in range(len(x)):
            sheesh = findError([x[l]], [y[l]], newW, newB)
            # print(sheesh[0])
            newW = sheesh[1]
            newB = sheesh[2]
        print("Saving epoch...")
        output = open('myfile.pkl', 'wb')
        pickle.dump((newW, newB), output)
        output.close()

        # print()
    return (newW, newB)

def getMNISTData(file):
    global mDataX, mDataY
    with open(file, "r") as r:
        count = 0
        for line in r:
            temp = line.strip()
            data = temp.split(",")
            trueval = [int(data[0])]
            datalist = data[1:]
            datalist = np.array(np.float_(datalist))/255
            mDataX.append(datalist)
            # distance = getDistance(val1, val2)
            mDataY.append(trueval)
            count+=1

def mnistWandB():
    w1 = 2 * np.random.rand(784, 300) - 1
    w2 = 2 * np.random.rand(300, 100) - 1
    w3 = 2 * np.random.rand(100, 10) - 1

    b1 = 2 * np.random.rand(1, 300) - 1
    b2 = 2 * np.random.rand(1, 100) - 1
    b3 = 2 * np.random.rand(1, 10) - 1

    return ([0, w1, w2, w3], [0, b1, b2, b3])

getMNISTData("mnist_train.csv")
mstuff = mnistWandB()
wCircle = mstuff[0]
bCircle = mstuff[1]
finalvals = realbackprop(50, mDataX, mDataY, wCircle, bCircle)
print(finalvals)