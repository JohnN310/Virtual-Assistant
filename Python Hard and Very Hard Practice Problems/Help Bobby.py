def help_bobby(size):  
    # array=[[None for _ in range(size)] for _ in range(size)]
    # row=0
    # col=0
    # while col<len(array) and row<len(array[0]):
    #     array[col][row]=1
    #     row+=1
    #     col+=1
    # row=0
    # col=size-1
    # while row<size and col>=0:
    #     array[row][col]=1
    #     row+=1
    #     col-=1
    # i=0
    # j=0
    # while i<size:
    #     while j<size:
    #         if array[i][j]==None:
    #             array[i][j]=0
    #         j+=1
    #     j=0
    #     i+=1 
    array=[[0 for _ in range(size)] for _ in range(size)]
    for i in array:print(i)
    row=0
    col=0
    for col in range(size):
        array[col][row]=1
        array[row][size-1-col]=1
        row+=1
    return array
print(help_bobby(8))