def only_5_and_3(n):
    try:
        if n==3 or n==5:
            return True
        elif n<0:
            return False
        else:
            return only_5_and_3(n-5) or only_5_and_3(n//3)
    except:
        return False
print (only_5_and_3(7))
