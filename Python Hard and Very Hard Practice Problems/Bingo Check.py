def bingo(lst):
    i=0
    j=0
    count=0
    if lst[0][0]==lst[1][1]==lst[2][2]==lst[3][3]==lst[4][4]=='x' or lst[0][4]==lst[1][3]==lst[2][2]==lst[3][1]==lst[4][0]:
        return True
    else:
        while i< len(lst):
            while j<len(lst[i]):
                if lst[i][j]=="x":
                    count+=1
                j+=1
            j=0
            i+=1
        if count==5:
            return True
        else:
            count=0
            i=0
            j=0
            while i<len(lst):
                while j<len(lst[i]):
                    if (lst[j][i]=='x'):
                        count+=1
                    j+=1
                i+=1
                j=0
            if count==5:
                return True
    return False
print(bingo([
	[45, 46, 31, 74, "x"],
	[64, 78, 80, "x", 90],
	[37, 81, "x", 55, 54],
	[67, "x", 98, 34, 77],
	["x", 33, 24, 30, 52]
]))
        