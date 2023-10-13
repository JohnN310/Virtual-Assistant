def secret(string):
    i=0
    str1=""
    count=0
    while i<len(string):
        if count==0 and string[i]=='.':
            string=string[i+1:]
            count+=1
            continue
        if (count==1 and string[i]=='.'):
            str1+=string.replace('.'," ")
            count+=1
        i+=1
    return  "<p class='"+str1+"'></p>"
print(secret("p.one.two.three"))