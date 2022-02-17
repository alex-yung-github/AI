# 2 A.CB
# 2 .132
# 3 87436.152
# 3 .25187643
# 3 863.54217
# 4 AB.CEFGDIJKHMNOL
# 4 .BCDAEGHIFJLMNKO
# 5 ABCDEF.HIJKGMNOPLRSTUQVWX
# 5 FABCE.HIDJKGMNOPLRSTUQVWX
# 3 87436.152
# 3 .25187643
# 3 863.54217
import sys
from queue import Queue
import time
def BFSpath(parent, start, end):
    path = [end]
    while(path[-1] != start):
        path.append(parent[path[-1]])
    path = path[::-1]
    return path
def BFS(start, end, dimension):
    parent = {}
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    for node in queue:
        # print(node)
        # print(len(visited))
        if(node == end):
            return BFSpath(parent, start, end)
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
    # row1 = dimension
    # row2 = dimension * 2
    # row3 = dimension * 3
    # row4 = dimension * 4
    # row5 = dimension * 5
    # #issamerow method for only 5x5 maximum, but can change it for larger dimensions if needed
    # if(index1 < 0 or index2 < 0):
    #     return False
    # if(index1 < row1 and index2 < row1):
    #     return True
    # elif((index1 < row2 and index1 >= row1) and (index2 < row2 and index2 >= row1)):
    #     return True
    # elif((index1 < row3 and index1 >= row2) and (index2 < row3 and index2 >= row2)):
    #     return True
    # elif((index1 < row4 and index1 >= row3) and (index2 < row4 and index2 >= row3)):
    #     return True
    # elif((index1 < row5 and index1 >= row4) and (index2 < row5 and index2 >= row4)):
    #     return True
    # else:
    #     return False
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

file = sys.argv[1]
# print("Printing all puzzles with possibilities and solutions in the text file: ")
count = 0
with open(file, "r") as f:  
 for line in f:  
     temp = line.split(" ")
     dimension = int(temp[0])
     board = temp[1].strip()
     
    #  print("Puzzle: ")
    #  print_puzzle(board, dimension)
    #  print("Solved Puzzle: ")
    #  print_puzzle(find_goal(board), dimension)
    #  print("Possible Outcomes (R, L, U, D)")
    #  tem = get_children(board, dimension)
    #  for i in tem:
    #      print_puzzle(i, dimension)
    #  start = time.perf_counter()  
    # # Whatever code you want to benchmark goes here  
    #  end = time.perf_counter()  
    #  print("Seconds to run: %s" % (end - start))  
     start = time.perf_counter() 
     tem2 = BFS(board, find_goal(board), dimension)
     end = time.perf_counter()
     if(tem2 != None):
         print("Line", count, board, "Length: ", len(tem2)-1, "Time", "%s" % (end - start))
     else:
         print("No Solution")




# dimension = int(sys.argv[1])
# board = sys.argv[2]
# place = board.index(".")
# print_puzzle(board, dimension)
# print("right", insamerow(place, place + 1, dimension))
# print("left", insamerow(place-1, place, dimension))
# print_puzzle(board, dimension)
# print("Moving Space Up")
# board = up(board, dimension)
# print_puzzle(board, dimension)
# print("Moving Space Down Twice")
# board = down(board, dimension)
# print_puzzle(board,dimension)
# board = down(board, dimension)
# print_puzzle(board,dimension)
# print("Moving Space Left")
# board = left(board, dimension)
# print_puzzle(board, dimension)
# print("Moving Space Right Twice")
# board = right(board, dimension)
# print_puzzle(board, dimension)
# board = right(board, dimension)
# print_puzzle(board, dimension)


# for i in get_children(board, dimension):
#     print_puzzle(i)

