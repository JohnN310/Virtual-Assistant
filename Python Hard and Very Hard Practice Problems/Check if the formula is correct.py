def check(string):
    lst=string.split('=')
    i=0
    lst2=[]
    while i<len(string):
        if string[i]=='/':
            lst2=lst[0].split('/')
            return int(lst2[0])/int(lst2[1])==int(lst[1])
        if string[i]=='*':
            lst2=lst[0].split('*')
            return int(lst2[0])*int(lst2[1])==int(lst[1])
        if string[i]=='-':
            lst2=lst[0].split('-')
            return int(lst2[0])-int(lst2[1])==int(lst[1])
        if string[i]=='+':
            lst2=lst[0].split('+')
            return int(lst2[0])+int(lst2[1])==int(lst[1])
        i+=1
    return None
print(check("8+4=12"))