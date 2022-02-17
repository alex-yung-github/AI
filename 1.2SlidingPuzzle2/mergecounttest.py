def parityCheck(board, dimension):
    boardlist = []
    boardlist[:0] = board.replace(".", "")
    temp = inversioncount(boardlist)
    if(dimension % 2 == 1):
        if(temp % 2 == 0):
            return True
        else:
            return False
    if(dimension % 2 == 0):
        row = (board.index(".") % dimension)
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
    return True
def inversioncount(board):
    leftInv = 0
    rightInv = 0
    mergeInv = 0
    if(len(board) >=2 ):
        c = int(len(board) / 2)
        leftArr = [c]
        rightArr = [int(len(board)) - c]
        rightCount = 0
        for i in range(len(board)):
            if(i < c):
                leftArr[i] = board[i]
            else:
                rightArr[rightCount] = board[i]
                rightCount = rightCount+1
        leftInv = inversioncount(leftArr)
        rightInv = inversioncount(rightArr)
        mergeInv = mergeinversioncount(board, leftArr, rightArr)
    return leftInv + rightInv + mergeInv
def mergeinversioncount(board, l, r):
    i = 0
    j = 0
    count = 0
    while(r < len(l) and l < len(l)):
        if(j == len(r)):
            board[i+j] = l[j]
            j= j+1
        elif(i == len(l)):
            board[i+j] = r[i]
            i=i+1
        elif(l[i] > r[j]):
            board[i+j] = r[j]
            count = count + len(l) - i
            j = j + 1
        else:
            board[i+j] = l[i]
            i = i + 1
    return count
    
    return 20202020