import sys
from  math  import  log
n = int
candidalph = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"


def getInput():
    global n, candidalph
    n = sys.argv[1]
    encodedtext = sys.argv[2].lower()
    candidalph = sys.argv[3].lower()
    print(encodedtext, candidalph)
    return encodedtext

def decodeInit(encodedtext):
    newstring = ""
    for i in range(len(encodedtext)):
        oldletter = encodedtext[i:i+1].lower()
        if(oldletter in candidalph):
            ind = alphabet.index(oldletter)
            newstring += candidalph[ind:ind+1]
        else:
            newstring += oldletter
    return newstring


etext = getInput()
decodedtext = decodeInit(etext)
print(decodedtext)

