def identity(num):
    if num>0:
        lst=[[None for _ in range(num)] for _ in range(num)]
        i=0
        j=0
        while i<num and j<num:
            lst[i][j]=1
            i+=1
            j+=1
        i=0
        j=0
        while i<num:
            while j<num:
                if lst[i][j]==None:
                    lst[i][j]=0
                j+=1
            i+=1
            j=0
    else:
        lst=[[None for _ in range(-1*num)] for _ in range(-1*num)]
        i=0
        j=-1*num-1
        while i<-1*num and j>=0:
            lst[i][j]=1
            j-=1
            i+=1
        i=0
        j=0
        while i<-1*num:
            while j<-1*num:
                if lst[i][j]==None:
                    lst[i][j]=0
                j+=1
            i+=1
            j=0
    return lst
print(identity(5))
            


