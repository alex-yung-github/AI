import sys
import time
from queue import Queue
def bfspath(parent1, parent2, start, end, intersection):
    path = [intersection]
    while(path[-1] != start):
        path.append(parent1[path[-1]])
    path = path[::-1]
    path2 = [intersection]
    if(intersection != end and intersection != start):
        while(path2[-1] != end):
            path2.append(parent2[path2[-1]])
        path2.pop(0)
    finalpath = path + path2
    return finalpath
def bfs(start, end, file):
    startq = []
    endq = []
    parent = {}
    parent2 = {}
    visited1 = set()
    visited2 = set()
    startq.append(start)
    endq.append(end)
    visited1.add(start)
    visited2.add(end)
    if(issimilar(start, end)):
        return [start, end]
    for node1, node2 in zip(startq, endq):
        for adjacent1 in findChildren(node1, file):
            if(adjacent1 not in visited1):
                parent[adjacent1] = node1
                startq.append(adjacent1)
                visited1.add(adjacent1)
        for adjacent2 in findChildren(node2, file):
            if(adjacent2 not in visited2):
                parent2[adjacent2] = node2
                endq.append(adjacent2)
                visited2.add(adjacent2)
        inter = set.intersection(set(visited1), set(visited2))
        if(len(inter) > 0):
            return bfspath(parent, parent2, start, end, inter.pop())          
    return None
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

        


#file = sys.argv[1]
# with open("puzzles_normal.txt", "r") as f:  
#  for line in f:  
#      list = line.split(" ")

# with open("words_06_letters.txt", "r") as f:
#     count = 0
#     for line in f:
#         if(count == 20):
#             break
#         print(findChildren(line.strip(),"words_06_letters.txt"))
#         count = count + 1

# start = time.perf_counter() 
# test = bfs("blinds", "molded", "words_06_letters.txt")
# end = time.perf_counter()
# print(test, "Length:", len(test), "Time:", "%s" % (end - start))

print("Finding Shortest Path:")
count = 0
file1 = sys.argv[1]
file2 = sys.argv[2]
with open(file1, "r") as f:
    for line in f:
        temp = line.split()
        start = time.perf_counter() 
        tem2 = bfs(temp[0], temp[1], file2)
        end = time.perf_counter()
        if(tem2 != None):
            print("Length: ", len(tem2), "Time:", "%s" % (end - start))
        else:
            print("No Solution!", "Time:", "%s" % (end - start))

