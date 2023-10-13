def primiera(lst):
    i=0
    dia=0
    hea=0
    clu=0
    spa=0
    count_d=0
    count_h=0
    count_c=0
    count_s=0
    while i<len(lst):
        if lst[i][1]=='d':
            count_d+=1
            if lst[i][0]=='7'and 21>dia:
                dia=21
            elif lst[i][0]=='6'and 18>dia:
                dia=18
            elif lst[i][0]=='A'and 16>dia:
                dia=16
            elif (lst[i][0]=='J' or lst[i][0]=='Q' or lst[i][0]=='K') and 10>dia:
                dia=10
            elif (lst[i][0]=='2' or lst[i][0]=='3' or lst[i][0]=='4' or lst[i][0]=='5') and (int(lst[i][0])+10)>dia:
                dia=int(lst[i][0])+10
        if lst[i][1]=='h':
            count_h+=1
            if lst[i][0]=='7'and 21>hea:
                hea=21
            elif lst[i][0]=='6'and 18>hea:
                hea=18
            elif lst[i][0]=='A'and 16>hea:
                hea=16
            elif (lst[i][0]=='J' or lst[i][0]=='Q' or lst[i][0]=='K') and 10>hea:
                hea=10
            elif (lst[i][0]=='2' or lst[i][0]=='3' or lst[i][0]=='4' or lst[i][0]=='5') and (int(lst[i][0])+10)>hea:
                hea=int(lst[i][0])+10
        if lst[i][1]=='c':
            count_c+=1
            if lst[i][0]=='7'and 21>clu:
                clu=21
            elif lst[i][0]=='6'and 18>clu:
                clu=18
            elif lst[i][0]=='A'and 16>clu:
                clu=16
            elif (lst[i][0]=='J' or lst[i][0]=='Q' or lst[i][0]=='K') and 10>clu:
                clu=10
            elif (lst[i][0]=='2' or lst[i][0]=='3' or lst[i][0]=='4' or lst[i][0]=='5') and (int(lst[i][0])+10)>clu:
                clu=int(lst[i][0])+10
        if lst[i][1]=='s':
            count_s+=1
            if lst[i][0]=='7'and 21>spa:
                spa=21
            elif lst[i][0]=='6'and 18>spa:
                spa=18
            elif lst[i][0]=='A'and 16>spa:
                spa=16
            elif (lst[i][0]=='J' or lst[i][0]=='Q' or lst[i][0]=='K') and 10>spa:
                spa=10
            elif (lst[i][0]=='2' or lst[i][0]=='3' or lst[i][0]=='4' or lst[i][0]=='5') and (int(lst[i][0])+10)>spa:
                spa=int(lst[i][0])+10
        i+=1
    if count_c>=1 and count_d>=1 and count_h>=1 and count_s>=1:
        return dia+spa+hea+clu
    else:
        return 0
print(primiera(["3d", "7d", "Kd", "7h", "Qh", "Ah", "7s", "3c", "Jc"]))