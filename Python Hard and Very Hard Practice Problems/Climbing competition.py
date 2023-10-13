import math
def climb(num, lst):
    count=0
    i=0
    height=0
    tired=0
    while i<len(lst)-1:
        height=abs(lst[i]-lst[i+1])
        if lst[i]>lst[i+1] and num>math.ceil(height):
            num-=math.ceil(height)
            count+=1
        elif num>(2*(math.ceil(height))) and lst[i]<lst[i+1]:
            num-=(2*(math.ceil(height)))
            count+=1
        else:
            tired+=1
        if tired>0:
            break
        i+=1
    return count
print(climb(20,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]))