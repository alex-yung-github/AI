import sys
from  math  import  log
import string
import random
n = int
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = string.punctuation
frequencydict = {}
usedciphers = ()

def getInputFitness():
    global n
    texttype = sys.argv[1]
    n = int(sys.argv[2])
    encodedtext = sys.argv[3].lower()
    candidalph = sys.argv[4].lower()
    return (encodedtext, candidalph, texttype)

def getDebugInputFitness():
    global n
    n = 4
    texttype = "encoded"
    encodedtext = "XMTP  CGPQR  BWEKNJB  GQ  OTGRB  EL  BEQX  BWEKNJB,  G  RFGLI.	GR  GQ  BEQX ABSETQB  RFGQ  QBLRBLSB  TQBQ  EJJ  RBL  KMQR  SMKKML  VMPYQ  GL  BLDJGQF: ‘G  FEUB  RM  AB  E  DMMY  QRTYBLR  GL  RFER  SJEQQ  GL  RFB  PMMK  MC  RFER RBESFBP.’".lower()
    candidalph = "XRPHIWGSONFQDZEYVJKMATUCLB".lower()
    return (encodedtext, candidalph, texttype)

def getInputHill():
    global n
    n = int(sys.argv[1])
    encodedtext = sys.argv[2].lower()
    return encodedtext

def getInputHillDebug():
    global n
    n = 3
    # encodedtext = "XMTP  CGPQR  BWEKNJB  GQ  OTGRB  EL  BEQX  BWEKNJB,  G  RFGLI.   GR  GQ  BEQX ABSETQB  RFGQ  QBLRBLSB  TQBQ  EJJ  RBL  KMQR  SMKKML  VMPYQ  GL  BLDJGQF: G  FEUB  RM  AB  E  DMMY  QRTYBLR  GL  RFER  SJEQQ  GL  RFB  PMMK  MC  RFER RBESFBP.'".lower()
    encodedtext = "PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ- SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVS GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR.".lower()
    return encodedtext

def fillFreqDict():
    with open("ngrams.txt", "r") as f:
        for line in f:
            temp = line.split(" ")
            frequencydict[temp[0].strip().lower()] = int(temp[1].strip())

def decodeInit(encodedtext, cipher):
    newstring = ""
    for i in range(len(encodedtext)):
        oldletter = encodedtext[i:i+1].lower()
        if(oldletter in cipher):
            ind = alphabet.index(oldletter)
            newstring += cipher[ind:ind+1]
        else:
            newstring += oldletter
    return newstring

def getNGrams(decodedtext):
    grams = []
    words = decodedtext.split()

    for word in words:
        for i in range(len(word)-n+1):
            t = word[i:i+n]
            if(len(word) >= n):
                grams.append(t)

    newgrams = []
    for w in grams:
        if(isWord(w) == True):
            newgrams.append(w)

    return newgrams

def isWord(w):
    for i in w:
        if(i not in alphabet):
            return False
    return True

def calcumalations(grams):
    total = 0
    for i in grams:
        if(i in frequencydict.keys()):
            num = frequencydict[i]
            total += log(num, 2)
    return total

def fitness(texttype, etext, cipher):
    if(texttype == "encoded"):
        dtext = decodeInit(etext, cipher)
    else:
        dtext = etext
    grams = getNGrams(dtext)
    calc = calcumalations(grams)
    return calc

def getRandomCipher():
    temp = alphabet
    temp = ''.join(random.sample(temp, len(temp)))
    return temp

def hillClimb():
    etext = getInputHillDebug()
    count = 0
    cipher = getRandomCipher()
    best = hillClimbHelper(etext, cipher)
    while(count < 5000):
        tempcipher = swap(cipher)
        newtext = hillClimbHelper(etext, tempcipher)
        if(newtext[0] > best[0]):
            best = newtext
            cipher = tempcipher
            count = 0
        else:
            count+=1
    return (best[0], best[1], cipher)

def hillClimbHelper(etext, initcipher):
    dtext = decodeInit(etext, initcipher)
    # grams = getNGrams(dtext)
    # score = calcumalations(grams)
    score = fitness("decoded", dtext, initcipher)
    # print()
    # print("Cipher: ", initcipher)
    # print()
    # print("Decoded Text: ", dtext)
    # print()
    # print("Score: ", score)
    # print()
    return (score, dtext)

def swap(text):
    toReturn = text
    range = len(toReturn)-1
    randint1 = random.randint(0, range)
    randint2 = random.randint(0, range)
    while(randint2 == randint1):
        randint2 = random.randrange(0, range)
    temp1 = toReturn[randint1:randint1+1]
    toReturn = toReturn[0:randint1] + toReturn[randint2:randint2+1]+ toReturn[randint1+1:]
    toReturn = toReturn[0:randint2] + temp1 + toReturn[randint2+1:]
    return toReturn

def population(n):
    global usedciphers
    toReturn = []
    for i in range(n):
        temp = getRandomCipher()
        while(temp in usedciphers):
            temp = getRandomCipher()
        usedciphers = usedciphers + (temp)
        toReturn.append(temp)
    return toReturn

def selection():
    return 0

def breeding():
    return 0

fillFreqDict()

#fitness input: py fitness.py (encoded/decoded) (n) (text) (cipher)
# input = getDebugInputFitness()
# fit = fitness(input[2], input[0], input[1])
# print(fit)

#hillClimb input: py fitness.py (n) (encodedtext)
# hill = hillClimb()
# print()
# print("Text: ", hill[1])
# print()
# print("Cipher: ", hill[2])
# print()
# print("Score: ", hill[0])
# print()

#Genetic Alg
















