def rubik(lst):
    max=0
    min=9223372036854775807
    col=0
    max_count=0
    min_count=0
    actual_max_count=0
    actual_min_count=0
    while col<len(lst):
        if len(lst[col])>max and max_count==0:
            max_count+=1
            max=len(lst[col])
        if len(lst[col])<min and min_count==0:
            min_count+=1
            min=len(lst[col])
        if max_count>0 and len(lst[col])>max:
            actual_max_count+=1
            max=len(lst[col])
        elif min_count>0 and len(lst[col])<min:
            actual_min_count+=1
            min=len(lst[col])
        col+=1
    if actual_max_count!=0:
        i=0
        max_total=0
        while i<len(lst):
            max_total+=max-len(lst[i])
            i+=1
        return "Missing " + str(max_total)
    if actual_min_count!=0:
        i=0
        min_total=0
        fixed=0
        while i<len(lst):
            if fixed!=len(lst[i]) and len(lst[i])!=min:
                min_total+=len(lst[i])-min
                fixed=len(lst[i])
            i+=1
        return "Missing " + str(min_total)
    elif len(lst)==len(lst[0]):
        return "Full"
    else:
        return "Non-full"
print(rubik([["O", "O"],["O", "O"],
	["O", "O", "O"]
	]))
## Doesnt work for the up-side down staircase case with 2 rows of the same min len but works for the other cases