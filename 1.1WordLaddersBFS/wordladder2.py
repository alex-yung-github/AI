import sys
import time
from queue import Queue
bigv = []
holder = ""
def bfspath(parent, start, end):
    path = [end]
    while(path[-1] != start):
        path.append(parent[path[-1]])
    path = path[::-1]
    return path
def bfs(start, end, txt):
    parent = {}
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    for node in queue:
        if(node == end):
            return bfspath(parent, start, end)
        for adjacent in findChildren(node, txt):
            if adjacent not in visited:
                parent[adjacent] = node
                queue.append(adjacent)
                visited.add(adjacent)
 
    return []
def bfs2(start, txt):
    parent = {}
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    for node in queue:
        tem = findChildren(node, txt)
        if(len(tem) <= 0):
            return bfspath(parent, start, node)
        for adjacent in tem:
            if adjacent not in visited:
                parent[adjacent] = node
                queue.append(adjacent)
                visited.add(adjacent)
 
    return []
def issimilar(word1, word2):
    count = 0
    if(len(word1) != len(word2)):
        return False
    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            count = count + 1
    if(count > 1):
        return False
    return True
def findChildren(word, file):
    temp = []
    with open(file, "r") as f:
        for i in f:
            i2 = i.strip()
            if(i2 != word and issimilar(word, i2)):
                temp.append(i2)
    return temp
 
def getClump(line, txt):
    temp = findChildren(line, txt)
    if(line not in bigv):
        bigv.append(line)
    count = 0
    if(len(temp) == 0):
        return count
    else:
        for i in temp:
            if(i not in bigv):
                bigv.append(i)
                count = count + 1 + getClump(i, txt)
    if(count == 1624):
        print(bigv)
        print(len(bigv))
    return count
def findlongest():
    return True
 
 
#file = sys.argv[1]
# with open("puzzles_normal.txt", "r") as f:  
#  for line in f:  
#      list = line.split(" ")
 
# with open("words_06_letters.txt", "r") as f:
#     clumps = 0
#     maxsize = 0
#     for line in f:
#         holder = line.strip()
#         temmy = getClump(line.strip(), "words_06_letters.txt")
#         if(temmy > 0):
#             clumps = clumps + 1
#         if(temmy > maxsize):
#             maxsize = temmy
#     print(clumps)
#     print(maxsize + 1)
print(getClump("acorns","words_06_letters.txt"))
ssss = 0
wordy = ""
for i in bigv:
    print(i)
    toom = bfs(i, "scalps", "words_06_letters.txt")
    if(len(toom) > ssss):
        ssss = len(toom)
        wordy = i
print(len(toom), i)
# print(findChildren(line.strip(),"words_06_letters.txt"))

# start = time.perf_counter() 
# test = bfs("blinds", "molded", "words_06_letters.txt")
# end = time.perf_counter()
# print(test, "Length:", len(test), "Time:", "%s" % (end - start))
 
# print("Finding Shortest Path:")
# count = 0
# file1 = sys.argv[1]
# file2 = sys.argv[2]
# with open(file1, "r") as f:
#     for line in f:
#         temp = line.split()
#         start = time.perf_counter() 
#         tem2 = bfs(temp[0], temp[1], file2)
#         end = time.perf_counter()
#         if(tem2 != None):
#             print("Length: ", len(tem2), "Time:", "%s" % (end - start))
#         else:
#             print("No Solution!", "Time:", "%s" % (end - start))
 
# tem2 = bfs("acorns", "weaned", "words_06_letters.txt")
# print("Length: ", len(tem2), "Time:")
