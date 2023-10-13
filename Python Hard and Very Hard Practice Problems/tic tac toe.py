def tic_tac_toe(lst):
    i=0
    j=0  
    while i<len(lst):
        countx=0
        counto=0
        while j<len(lst[0]):
            if lst[i][j]=='X':
                countx+=1
            if lst[i][j]=='O':
                counto+=1
            j+=1
        if counto==3:
            return "O"
        if countx==3:
            return "X"
        j=0
        i+=1
    i=0
    j=0
    while i<len(lst):
        countx=0
        counto=0
        while j<len(lst[0]):
            if lst[j][i]=='X':
                countx+=1
            if lst[j][i]=='O':
                counto+=1
            j+=1
        if counto==3:
            return "O"
        if countx==3:
            return "X"
        j=0
        i+=1
    if (lst[0][0]==lst[1][1]==lst[2][2]=="X") or (lst[0][2]==lst[1][1]==lst[2][0]=="X"):
        return "X"
    if (lst[0][0]==lst[1][1]==lst[2][2]=="O") or (lst[0][2]==lst[1][1]==lst[2][0]=="O"):
        return "O"
    return "Draw"
print(tic_tac_toe([
	["X", "O", "E"],
	["X", "O", "E"],
	["E", "O", "X"]
]))