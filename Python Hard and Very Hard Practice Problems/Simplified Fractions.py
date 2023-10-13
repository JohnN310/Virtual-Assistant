import math
def simp(string):
    lst=string.split("/")
    num1=int(lst[0])
    num2=int(lst[1])
    if num1%num2==0:
        return int(num1/num2)
    else:
        num3=int(int(num2)/math.gcd(num1,num2))
        num4=int(int(num1)/math.gcd(num1,num2))
        return str(num4)+'/'+str(num3)
print(simp("5/45"))
        