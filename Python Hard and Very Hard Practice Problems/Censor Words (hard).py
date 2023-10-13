def censor(string,lst,char):
    # i=0
    # temp=""
    # k=0
    # new_str=""

    # while i<len(string):  
    #     if (string[i]!=" "):
    #         temp+=string[i]
    #     else:
    #         temp=""
    #     if k<len(lst) and lst[k] == temp:  
    #         for x in lst[k]:
    #             new_str+=char  
    #         k+=1
    #         temp=""   
    #     else:
    #         new_str+=string[i]
    #     i+=1
    # return new_str

    i=0
    while i<len(lst):
        j=0
        new_str=""
        while j<len(lst[i]):
            new_str+=char
            j+=1
        string=string.replace(lst[i],new_str,1)
        i+=1
    return string
print(censor("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?"))
