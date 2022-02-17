
import sys
import time
from random import sample

def csp_backtracking(board, dimension):
    if(goal_test(board, dimension)):
        return board
    var = get_next_unassigned_var(board)
    for val in get_sorted_values(board, dimension, var):
        var_result = csp_backtracking(board + [val], dimension)
        if(var_result is not None):
            return var_result
    return None


def find_goal(board):
    temp = board.replace(".", "", 1)
    toReturn = "".join(sorted(temp))
    toReturn = toReturn + "."
    return toReturn


def goal_test(board, dimension):
    return len(board) == dimension and checkAlignment(board)

    
def checkAlignment(board):
    return True


def get_next_unassigned_var(board):
    return len(board)


def get_sorted_values(board, dimension, var):
    toReturn = []
    diagcol = []
    for i in range(len(board)):
        temp = board[i] + (var-i)
        temp2 = board[i] - (var-i)
        diagcol.append(temp)
        diagcol.append(temp2)
    temp = sample(range(0, dimension), dimension)
    for i in temp:
        if (i not in diagcol) and (i not in board):
            toReturn.append(i)
    return toReturn
    
def test_solution(state):
    for var in range(len(state)): 
        left = state[var]
        middle = state[var] 
        right = state[var]
        for compare in range(var + 1, len(state)): 
            left -= 1
            right += 1
            if state[compare] == middle: 
                print(var, "middle", compare) 
                return False
            if left >= 0 and state[compare] == left: 
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right: 
                print(var, "right", compare)
                return False
    return True


board = []
for i in range(4,51):
    if(i == 1):
        t1 = time.perf_counter()
        tem = [1]
        t2 = time.perf_counter()
        yes = test_solution(tem)
    else:
        t1 = time.perf_counter()
        tem = csp_backtracking(board, i)
        t2 = time.perf_counter()
        yes = test_solution(tem)
    print("Length:", i, "Test: ", yes, "Time", "%s" % (t2 - t1))
