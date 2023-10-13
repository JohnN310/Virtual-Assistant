def advanced_sort(lst):
    a=[]
    b=[]
    i=0
    j=i+1
    while i<len(lst):
        if (lst[i] is not None):
            b.append(lst[i])
            while j<len(lst):
                if (lst[i]==lst[j] and lst[i] is not None and lst[j] is not None):
                    b.append(lst[j])
                    lst[j]=None
                j+=1        
        a.insert(len(a),b)
        b=[]
        i+=1           
        j=i+1
    z=0
    while z<len(a): 
        if not a[z]:
            a.remove(a[z])
            z-=1
        z+=1
    return a
print(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]))
            
