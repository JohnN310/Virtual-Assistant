def prime_factors(num):
    i=2
    a=[]
    while num>1:
        if (num % i ==0):
            a.append(i)
            num=num/i
        else:
            i+=1
    return a
print(prime_factors(8912234))