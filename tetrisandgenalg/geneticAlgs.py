from lib2to3.pytree import convert
import sys
from  math  import  log
import string
import random
n = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetlist = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
punctuation = string.punctuation
frequencydict = {}
usedciphers = set()
encodedText = ""
POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNEY_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_POINTS = 5
MUTATION_RATE = .8

def getInputFitness():
    global n
    texttype = sys.argv[1]
    n = int(sys.argv[2])
    encodedtext = sys.argv[3].lower()
    candidalph = sys.argv[4].lower()
    return (encodedtext, candidalph, texttype)

def getDebugInputFitness():
    global n
    n = 3
    texttype = "decoded"
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

def getInputGenAlg():
    global n, encodedText
    n = 4
    encodedText = sys.argv[1]
    return encodedText

def getInputGenAlgDebug():
    global n, encodedText
    n = 3
    encodedText = "PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ- SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT. GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVS GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR. SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR BHE CEVAPVCYRF CNTR.".lower()
    return encodedText

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

def fitnessSpecialized(cipher):
    dtext = decodeInit(encodedText, cipher)
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
    while(count < 1000):
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
    print()
    print("Cipher: ", initcipher)
    print()
    print("Decoded Text: ", dtext)
    print()
    print("Score: ", score)
    print()
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

def convertWithScores(listOfCiphers):
    toReturn = []
    for i in listOfCiphers:
        fitscore = fitnessSpecialized(i)
        toReturn.append([fitscore, i])
    return toReturn

def population(n):
    global usedciphers
    toReturn = []
    for i in range(n):
        temp = getRandomCipher()
        while(temp in usedciphers):
            temp = getRandomCipher()
        usedciphers.add(temp)
        toReturn.append(temp)
    return toReturn

def selection(orderedOrigin):
    nextGen = []
    #add some top current gen to nextgen
    orderedOrigin.sort(reverse = True)
    for i in range(0, NUM_CLONES):
        nextGen.append(orderedOrigin[i])
    
    tourney = random.sample(orderedOrigin, TOURNEY_SIZE*2)
    t1 = tourney[:len(tourney)//2]
    t2 = tourney[len(tourney)//2:]
    t1.sort(reverse = True)
    t2.sort(reverse = True)
    parents = []
    for i in t1:
        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            parents.append(i)
            break

    for i in t2:
        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            parents.append(i)
            break
    
    return parents



def breeding(parents):
    p1 = parents[0]
    p2 = parents[1]
    child = "--------------------------"
    crossovers = random.sample(p1[1], CROSSOVER_POINTS)
    for i in crossovers:
        tempindex = p1[1].index(i)
        child = child[0:tempindex] + i + child[tempindex+1:]
    
    index = 0
    for i in p2[1]:
        if(i not in child):
            while(child[index:index+1] != "-"):
                index+=1
            child = child[0:index] + i + child[index+1:]
    
    return child

def mutation(child):
    global usedciphers
    #random.select() automatically choozes 2 thingies 
    m = random.random()
    # print(m)
    if(m < MUTATION_RATE):
        toReturn = child
        tem = random.sample(alphabetlist, 2)
        # print(tem)
        randint1 = int(toReturn.index(tem[0]))
        randint2 = int(toReturn.index(tem[1]))
        # print(randint1, randint2)
        temp1 = toReturn[randint1:randint1+1]
        toReturn = toReturn[0:randint1] + toReturn[randint2:randint2+1]+ toReturn[randint1+1:]
        toReturn = toReturn[0:randint2] + temp1 + toReturn[randint2+1:]
        return toReturn
    else:
        return child

def getInitChildren(n):
    toReturn = []
    for i in range(n):
        pop = population(TOURNEY_SIZE*2)
        # print(pop)
        pop = convertWithScores(pop)
        # print(pop)
        par = selection(pop)
        # print(par)
        child = breeding(par)
        # print(child)
        mutantchild = mutation(child)
        # print(mutantchild)
        # print("same") if mutantchild == child else print("mutated")
        toReturn.append(mutantchild)
    return toReturn

def genAlg(etext):
    count = 1
    cInit = getInitChildren(500)
    cScoresInit = convertWithScores(cInit)
    cScoresInit.sort(reverse = True)
    # print(cScoresInit)
    bestcipher = cScoresInit[0][1]
    # print(bestcipher)

    while(count < 500):
        newgen = []
        for i in range(POPULATION_SIZE):
            newSel = selection(cScoresInit)
            newChild = breeding(newSel)
            newMutChild = mutation(newChild)
            newgen.append(newMutChild)
        cScoresInit = newgen
        cScoresInit = convertWithScores(cScoresInit)
        cScoresInit.sort(reverse = True)
        print(cScoresInit[0])
        print(decodeInit(etext, cScoresInit[0][1]))
        print()
        count+=1

    





fillFreqDict()

#fitness input: py fitness.py (encoded/decoded) (n) (text) (cipher)
# input = getDebugInputFitness()
# fit = fitness(input[2], input[0], input[1])
# print(fit)

#hillClimb input: py fitness.py (n) (encodedtext)
hill = hillClimb()
print()
print("Text: ", hill[1])
print()
print("Cipher: ", hill[2])
print()
print("Score: ", hill[0])
print()

# Genetic Alg input: py geneticAlg.py (n) (encodedtext)
# etext = getInputGenAlg()
# thing = genAlg(etext)