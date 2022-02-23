import sys

if(sys.argv[1] == "A"):
    print(0 + int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))
elif(sys.argv[1] == "B"):
    count = 0
    for i in sys.argv[2:len(sys.argv)]:
        count = count + int(i)
    print(count)
elif(sys.argv[1] == "C"):
    temp = []
    for i in sys.argv[2:len(sys.argv)]:
        if(int(i) % 3 == 0):
            temp.append(int(i))
    print(temp)
elif(sys.argv[1] == "D"):
    n = int(sys.argv[2])
    prev1 = 1
    prev2 = 1
    if(n <= 0):
        print("nothing")
    elif(n == 1):
        print(prev1)
    elif(n == 2): 
        print(str(prev1) + " " + str(prev2))
    else:
        print(str(prev1) + " " + str(prev2), end = '')
        n = n - 2
        for i in range(n):
            new = prev1 + prev2 
            if(i % 2 == 0):
                prev1 = new
            else:
                prev2 = new
            print(" " + str(new), end = '')     
elif(sys.argv[1] == "E"):
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    for i in range(n1, n2 + 1):
        print((i ** 2) - (3 * i) + 2)
elif(sys.argv[1] == "F"):
    s1 = int(sys.argv[2])
    s2 = int(sys.argv[3])
    s3 = int(sys.argv[4])
    if(s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
        print("Error: Not a possible triangle")
    elif(s1 < 0 or s2 < 0 or s3 < 0):
        print("Error: Not a possible triangle")
    else:
        p = (s1 + s2 + s3)/2
        print("Area: " + str(((p) * (p-s1) * (p-s2) * (p-s3)) ** (1/2)))
elif(sys.argv[1] == "G"):
    str = sys.argv[2]
    print("a: {}".format(sum(str[i:i+1].lower() == "a" for i in range(len(str)))))
    print("e: {}".format(sum(str[i:i+1].lower() == "e" for i in range(len(str)))))
    print("i: {}".format(sum(str[i:i+1].lower() == "i" for i in range(len(str)))))
    print("o: {}".format(sum(str[i:i+1].lower() == "o" for i in range(len(str)))))
    print("u: {}".format(sum(str[i:i+1].lower() == "u" for i in range(len(str)))))
    
else:
    print("Doesn't fit any cases")