import re
txt = "There are many malicious animals in the woods"
txtlist = txt.split(" ")

regularexpression = "ma.*"
tR0 = []
for i in txtlist:
    tR0.append(re.findall(regularexpression, i))
print(tR0)
tR1 = re.findall(regularexpression, txt)
print(tR1)

text = "eat the big treat and pat the big rat and sit on the big mat"
words = text.split(" ")
dict = {}
for i in words:
    temp = re.findall("...", i)
    if(len(temp) > 0 and temp[0] == i):
        temp2 = temp[0]
        if(temp2 not in dict.keys()):
            dict[temp2] = 1
        else:
            dict[temp2] += 1
print(dict)

teext = "i 9eat pies"
teext2 = "five"
x = re.findall("1|2|3|4|5|7|8|9|0", teext)
print("Has Number") if(len(x) > 0) else print("Has No Number")
y = re.findall("1|2|3|4|5|7|8|9|0", teext2)
print("Has Number") if(len(y) > 0) else print("Has No Number")

bigtext = "heeeeeeeeeeeeeeeeeeeeeeeeeeeello"
smalltext = "heeee"
ads = "hello"
adds = "helle"
beegtext = "hellle"
z = re.findall("^h.{3}.*e$", bigtext)
print(re.findall("^h.{3}.*e$", ads))
print(re.findall("^h.{3}.*e$", adds))

zz = re.findall("h.{5}", smalltext)
zzz = re.findall("h.{5}", beegtext)
print(z) #prints [heeeee]
print(zz) #none
print(zzz) #prints [hellle]

t1 = "i really like pie"
t2 = "black and murky water"
t3 = "fat and big cat"
gg = re.findall(".*b+.*", t1) #returns the string if it has a "b" in it
ggg = re.findall(".*b+.*", t2)
gggg = re.findall(".*b+.*", t3)
print(gg) #returns nothing
print(ggg) #returns ['black and murky water']
print(gggg) #returns ['fat and big cat']


strings = "sky can be red"
finalllly = re.findall("[a-z][a-z][a-z]", strings)
print(finalllly)