def dakti(a):
    words=a.rsplit(" ")
    arranged=['a']*len(words)
    i=0
    while i<len(words):
        j=0
        while j<len(words[i]):
            if words[i][j].isdigit():
                arranged[int(words[i][j])-1]=words[i]
            j+=1
        i+=1   
    k=0
    while k<len(arranged):
        l=0
        while l<len(arranged[k]):
            if arranged[k][l].isdigit():   
                arranged[k]=arranged[k].replace(arranged[k][l],"")
            l+=1
        k+=1    
    return arranged
print(dakti("yo2u cr3azy a1re"))
# instead of creating an empty list, create a list with a specified number of a's then replace a's with the correct words. 