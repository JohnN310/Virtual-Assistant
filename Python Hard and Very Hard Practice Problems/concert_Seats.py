def concert(lst):
    i=0
    j=0
    while i<len(lst[0]):
        while j<len(lst)-1:
            if lst[j][i] >= lst[j+1][i]:
                return (j, i)
            j+=1
        i+=1
        j=0
    return True

print(concert([[1, 1, 2], 
[5, 2, 3], 
[6, 4, 4]]
))