import sys
from queue import Queue
from heapq import heappop, heapify,heappush
 
import time
def BFSpath(parent, start, end):
    path = [end]
    while(path[-1] != start):
        path.append(parent[path[-1]])
    path = path[::-1]
    return path
def BFS(start, dimension):
    parent = {}
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    for node in queue:
        # print(node)
        # print(len(visited))
        if(goal_test(node, start)):
            return BFSpath(parent, start, find_goal(start))
        for adjacent in get_children(node, dimension):
            if adjacent not in visited:
                parent[adjacent] = node
                queue.append(adjacent)
                visited.add(adjacent)
    return []
def getNumber(x, y, board, dimen):
    place = 0
    place = place + ((y-1)*dimen) + (x-1)
    return board[place:place+1]
def print_puzzle(board, dimension):
    toPrint = ""
    for i in board:
        toPrint = toPrint + i + " "
        if((board.index(i)+1) % dimension == 0):
            toPrint = toPrint + "\n"
    print(toPrint)
def find_goal(board):
    temp = board.replace(".", "", 1)
    toReturn = "".join(sorted(temp))
    toReturn = toReturn + "."
    return toReturn
def goal_test(toTest, board):
    return find_goal(board) == toTest
 
# def swap(str, index1, index2):
#     temp = str[index1:index1+1]
#     newstr = str
#     newstr[index1] = newstr[index2]
#     newstr[index2] = temp
#     return newstr
def insamerow(index1, index2, dimension):
    row1 = int(index1/dimension)
    row2 = int(index2/dimension)
    if(index1 < 0 or index2 < 0):
        return False
    if(index1 > (dimension * dimension) or index2 > (dimension * dimension)):
        return False
    if(row1 == row2):
        return True
    return False
   
def up(board, dimension):
    temp = list(board)
    place = temp.index(".")
    if(place-dimension < 0):
        return board
    val = temp[place-dimension]
    temp[place-dimension] = "."
    temp[place] = val
    board = "".join(temp)
    return board
def down(board,dimension):
    temp = list(board)
    place = temp.index(".")
    if(place+dimension >= len(board)):
        return board
    val = temp[place+dimension]
    temp[place+dimension] = "."
    temp[place] = val
    board = "".join(temp)
    return board
def left(board, dimension):
    temp = list(board)
    place = temp.index(".")
    if(insamerow(place-1, place, dimension) == False):
        return board
    val = temp[place-1]
    temp[place-1] = "."
    temp[place] = val
    board = "".join(temp)
    return board
def right(board, dimension):
    temp = list(board)
    place = temp.index(".")
    if(insamerow(place, place+1, dimension) == False):
        return board
    val = temp[place+1]
    temp[place+1] = "."
    temp[place] = val
    board = "".join(temp)
    return board
def get_children(board, dimension):
    toReturn = []
    r = right(board, dimension)
    l = left(board, dimension)
    u = up(board, dimension)
    d = down(board, dimension)
    if(r != board):
        toReturn.append(r)
    if(l != board):
        toReturn.append(l)
    if(u != board):
        toReturn.append(u)
    if(d != board):
        toReturn.append(d)
 
    return toReturn
def parityCheck(board, dimension):
    boardlist = []
    boardlist[:0] = board.replace(".", "")
    temp = paritycounter(boardlist)
    if(dimension % 2 == 1):
        if(temp % 2 == 0):
            return True
        else:
            return False
    if(dimension % 2 == 0):
        row = int((board.index(".")) / dimension)
        if(row % 2 == 0):
            if(temp % 2 == 1):
                return True
            else:
                return False
        else:
            if(temp % 2 == 0):
                return True
            else:
                return False
def paritycounter(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)-i):
            if(array[i] > array[i+j]):
                count += 1
    return count
 
def iddfshelper(start, k, dimension):
    fringe = []
    depth = 0
    tem = set()
    tem.add(start)
    fringe.append((start, depth, tem))
    while(len(fringe) > 0):
        v = fringe.pop()
        if(goal_test(v[0], start)):
            return v[1]
        if(v[1] < k):
            for i in get_children(v[0], dimension):
                if(i not in v[2]):
                    newset = v[2].copy()
                    newset.add(i)
                    temp = (i, v[1] + 1, newset)
                    fringe.append(temp)
    return None

    
def iddfs(start, dimension):
    maxdepth = 0
    result = None
    while(result is None):
        result = iddfshelper(start, maxdepth, dimension)
        maxdepth += 1
    return result
   
def taxidistance(board, dimension):
    count = 0
    for i in board:
        if(i != "."):
            index = board.index(i) + 1
            place = find_goal(board).index(i) + 1
            row = int((index-1)/dimension)
            placerow = int((place-1)/dimension)
            while(row < placerow):
                index += dimension
                count += 1
                row += 1
            while(placerow < row):
                index -= dimension
                count += 1
                row -= 1
            p1 = (index-1) % dimension
            p2 = (place-1) % dimension
            hormove = abs(p1-p2)
            count += hormove
    return count
def astar(start, dimension):
    depth = 0
    visited = set()
    startf = (taxidistance(start, dimension), start, depth)
    fringe = []
    heappush(fringe, startf)
    while(len(fringe) > 0):
        v = heappop(fringe)
        if(goal_test(v[1], start)):
            return (v)
        if(v not in visited):
            visited.add(v[1])
            for i in get_children(v[1], dimension):
                if i not in visited:
                    newdepth = v[2] + 1
                    heuristic = taxidistance(i, dimension) + newdepth
                    heappush(fringe, (heuristic, i, newdepth))
    return None
 
 
 
#parity test
file = sys.argv[1]
count = 0
with open(file, "r") as f:  
 for line in f:  
     temp = line.split(" ")
     dimension = int(temp[0])
     board = temp[1].strip()
     symbol = temp[2].strip()
     paritytime = time.perf_counter()
     possibility = parityCheck(board, dimension)
     paritytime2 = time.perf_counter()
     if(possibility != False):
         if(symbol == "!"):
             start = time.perf_counter()
             tem = BFS(board, dimension)
             end = time.perf_counter()
             print("Line", count, "BFS - ", "Length", len(tem)-1, "Time", "%s" % (end - start))
             start2 = time.perf_counter()
             tem = iddfs(board, dimension)
             end2 = time.perf_counter()
             print("Line", count, "IDDFS - ", "Length", tem, "Time", "%s" % (end2 - start2))
             start3 = time.perf_counter()
             tem = astar(board, dimension)
             end3 = time.perf_counter()
             print("Line", count, "A* - ", "Length", tem[2], "Time", "%s" % (end3 - start3))
         elif(symbol == "B"):
             start = time.perf_counter()
             tem = BFS(board, dimension)
             end = time.perf_counter()
             print("Line", count, "BFS - ", "Length", len(tem)-1, "Time", "%s" % (end - start))
         elif(symbol == "I"):
             start2 = time.perf_counter()
             tem = iddfs(board, dimension)
             end2 = time.perf_counter()
             print("Line", count, "IDDFS - ", "Length", tem, "Time", "%s" % (end2 - start2))
         elif (symbol == "A"):
             start3 = time.perf_counter()
             tem = astar(board, dimension)
             end3 = time.perf_counter()
             print("Line", count, "A* - ", "Length", tem[2], "Time", "%s" % (end3 - start3))
     else:
         print("Line", count, "No Solution", "Time", "%s" % (paritytime2 - paritytime))
     count += 1
   
     
     
     
     
    #  start = time.perf_counter()
    #  tem2 = BFS(board, find_goal(board), dimension)
    #  end = time.perf_counter()
    #  if(tem2 != None):
    #      print("Line", count, board, "Length: ", len(tem2)-1, "Time", "%s" % (end - start))
    #  else:
    #      print("No Solution")