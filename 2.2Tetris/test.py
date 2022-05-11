# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def run_length_decoder(in_list):
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    toReturn = ""
    i = 0
    while(i < len(in_list)):
        tempst = in_list[i]
        if(i < (len(in_list)-1) and tempst == in_list[i+1]):
            toReturn += (tempst * int(in_list[i+2]))
            i+=3
        else:
            toReturn += tempst
            i+=1
    return toReturn


print(run_length_decoder(['a', 'b', 'b', 4, 'd']))