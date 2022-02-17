import sys
s = sys.argv[1]

#1
print("1:", s[2:3])
#2
print("2:", s[4:5])
#3
print("3:", len(s))
#4
print("4:", s[0:1])
#5
print("5:", s[-1])
#6
print("6:", s[-2:-1])
#7
print("7:", s[3:8])
#8
print("8:", s[-5:])
#9
print("9:", s[2:])
#10
print("10:", s[::2])
#11
print("11:", s[1::3])
#12
print("12:", s[::-1])
#13
print("13:", s.index(" "))
#14
print("14:", s[0:-1])
#15
print("15:", s[1:])
#16
print("16:", s.lower())
#17
print("17:", ' '.join(s.split(" ")).split())
#18
print("18:", len(' '.join(s.split(" ")).split()))
#19
print("19:", [i for i in s])
#20
print("20:", "".join(sorted(s.replace(" ", ""))))
#21
print("21:", s[0:s.index(" ")])
#22
print("22:", True if(s[0:int(len(s)/2)] == "".join(reversed(s[int(len(s)/2):int(len(s))]))) else False )
