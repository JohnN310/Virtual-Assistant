import math
def nearest(dic, target):
    min=2**15
    tar=""
    for x in dic:
        if abs(target-dic[x])<min:
            min=abs(target-dic[x])
            tar=x
        elif abs(target-dic[x])==min and x>tar:
            tar=x
    return tar
print(nearest({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5,
	"Chapter 1c" : 50,
	"Chapter 1d" : 100,
	"Chapter 1e" : 200,
	"Chapter 1f" : 400
}, 300))
