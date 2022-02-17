from othello_imports import printBoard


board = "ooxo.ooooxo..oooo.o...ooxoo.ox.ooxxox..o.xxx..ooxx.oxoooooxo..oo"
printBoard(board)
stablecount = 0
# if(board[0:1] != "."):
#     stablecount = 0
#     temptoken = board[0:1]
#     torightlen = 1
#     for i in range(1, 8):
#         if(board[i:i+1] != temptoken):
#             break
#         else:
#             torightlen+=1
#             stablecount+=1
#     prevrowlen = torightlen
#     limit = prevrowlen
#     for i in range(8, 49, 8):
#         for col in range(i, i+limit):
#             if(board[col:col+1] != temptoken):
#                 break
#             else:
#                 prevrowlen +=1
#                 stablecount+=1
#         if(prevrowlen == 0):
#             break
#         limit = prevrowlen
#         prevrowlen = 0
# print("TL: ", stablecount)

# if(board[63:64] != "."):
#     stablecount = 0
#     temptoken = board[63:64]
#     toleftlen = 0
#     for i in range(62, 56, -1):
#         if(board[i:i+1] != temptoken):
#             break
#         else:
#             toleftlen+=1
#             stablecount+=1
#     prevrowlen = toleftlen
#     limit = prevrowlen
#     for i in range(55, 8, -8):
#         for col in range(i, i-limit, -1):
#             if(board[col:col+1] != temptoken):
#                 break
#             else:
#                 prevrowlen +=1
#                 stablecount+=1
#         if(prevrowlen == 0):
#             break
#         limit = prevrowlen
#         prevrowlen = 0
# print("BR: ", stablecount)

# if(board[56:57] != "."):
#     stablecount = 0
#     temptoken = board[56:57]
#     torightlen = 1
#     for i in range(57, 63):
#         if(board[i:i+1] != temptoken):
#             break
#         else:
#             torightlen+=1
#             stablecount+=1
#     prevrowlen = torightlen
#     limit = prevrowlen
#     for i in range(48, 7, -8):
#         for col in range(i, i+limit):
#             if(board[col:col+1] != temptoken):
#                 break
#             else:
#                 prevrowlen +=1
#                 stablecount+=1
#         if(prevrowlen == 0):
#             break
#         limit = prevrowlen
#         prevrowlen = 0
# print("BL: ", stablecount)
if(board[0:1] != "."):
    stablecount = 0
    temptoken = board[0:1]
    torightlen = 1
    downlen = 0
    for i in range(1, 7):
        if(board[i:i+1] != temptoken):
            break
        else:
            torightlen+=1
            stablecount+=1
    for i in range(8, 49, 8):
        if(board[i:i+1] != temptoken):
            break
        else:
            downlen += 1
    limit = torightlen
    prevrowlen = 0
    row = 1
    for i in range(8, 49, 8):
        row = int(i/8)
        for col in range(i, i+limit):
            diff = abs(col - i)
            if(board[col:col+1] != temptoken):
                break
            elif(diff > abs(row-downlen)):
                break
            else:
                prevrowlen +=1
                stablecount+=1
        if(prevrowlen == 0):
            break
        limit = prevrowlen
        prevrowlen = 0
        row+=1
print("TL: ", stablecount)

if(board[7:8] != "."):
    stablecount = 0
    temptoken = board[7:8]
    toleftlen = 1
    downlen = 0
    for i in range(6, 0, -1):
        if(board[i:i+1] != temptoken):
            break
        else:
            toleftlen+=1
            stablecount+=1
    for i in range(15, 56, 8):
        if(board[i:i+1] != temptoken):
            break
        else:
            downlen += 1
    limit = toleftlen
    prevrowlen = 0
    row = 1
    for i in range(15, 56, 8):
        for col in range(i, i-limit, -1):
            diff = abs(col - i)
            if(board[col:col+1] != temptoken):
                break
            elif(diff > abs(row-downlen)):
                break
            else:
                prevrowlen +=1
                stablecount+=1
        if(prevrowlen == 0):
            break
        limit = prevrowlen
        prevrowlen = 0
        row+=1
print("TR:", stablecount)

if(board[56:57] != "."):
    stablecount = 0
    temptoken = board[56:57]
    torightlen = 1
    downlen = 0
    for i in range(57, 63):
        if(board[i:i+1] != temptoken):
            break
        else:
            torightlen+=1
            stablecount+=1
    for i in range(48, 7, -8):
        if(board[i:i+1] != temptoken):
            break
        else:
            downlen += 1
    limit = torightlen
    prevrowlen = 0
    row = 1
    for i in range(48, 7, -8):
        for col in range(i, i-limit, -1):
            diff = abs(col - i)
            if(board[col:col+1] != temptoken):
                break
            elif(diff > abs(row-downlen)):
                break
            else:
                prevrowlen +=1
                stablecount+=1
        if(prevrowlen == 0):
            break
        limit = prevrowlen
        prevrowlen = 0
        row+=1
print("BL: ", stablecount)

if(board[63:64] != "."):
    stablecount = 0
    temptoken = board[63:64]
    toleftlen = 1
    downlen = 0
    for i in range(62, 56, -1):
        if(board[i:i+1] != temptoken):
            break
        else:
            toleftlen+=1
            stablecount+=1
    for i in range(55, 14, -8):
        if(board[i:i+1] != temptoken):
            break
        else:
            downlen += 1
    limit = toleftlen
    prevrowlen = 0
    row = 1
    for i in range(55, 14, -8):
        for col in range(i, i-limit, -1):
            diff = abs(col - i)
            if(board[col:col+1] != temptoken):
                break
            elif(diff > abs(row-downlen)):
                break
            else:
                prevrowlen +=1
                stablecount+=1
        if(prevrowlen == 0):
            break
        limit = prevrowlen
        prevrowlen = 0
        row+=1
print("BR: ", stablecount)
    # if(temptoken == "o"):
    #     stablecount = (-3 * stablecount)
    # elif(temptoken == "x"):
    #     stablecount = (3 * stablecount)
