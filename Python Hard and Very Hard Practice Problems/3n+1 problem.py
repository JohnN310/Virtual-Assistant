def collatz(a, b):
    if (check(a)<check(b)):
        return a, check(a)
    else:
        return b, check(b)
def check(num):
    if (num==1):
        return 0
    if (num % 2==0):
        return 1+check(num/2)
    else:
        return 1+check(num*3+1)
print(collatz(13, 16))