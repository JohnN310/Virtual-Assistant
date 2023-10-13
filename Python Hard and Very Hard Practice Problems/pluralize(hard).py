def pluralize(lst):
    i=0
    j=0
    count=1
    lst1=[]
    lst2=[]
    while i<len(lst):
        if lst[i] not in lst1:
            while (j<len(lst)):
                if lst[i]==lst[j] and i!=j:
                    count+=1
                    lst1.append(lst[i])
                j+=1
            if count>1:
                lst2.append(lst[i]+"s")
            else:
                lst2.append(lst[i])
        i+=1
        j=0
        count=1
    return set(lst2)
print(pluralize(["set", "set", "tuple", "tuple", "string", "string", "string", "string", "integer"]))