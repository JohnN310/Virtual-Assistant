def loves_me(num):
    a=""
    i=1
    while i<num:
        if (i % 2!= 0):
            a+="Loves me, "
        else:
            a+="Loves me not, "
        i+=1
    if (num % 2==0):
        a+="LOVES ME NOT."
    else:
        a+="LOVES ME."
    return a
print (loves_me(15))