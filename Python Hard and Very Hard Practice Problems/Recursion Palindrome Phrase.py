import re
def clean(string):
    string=string.strip()
    string=string.lower()
    string=re.sub('[^A-Za-z0-9]+', '',string) ##removes all the speical characters
    if len(string)%2!=0:
        string=string.replace(string[int(len(string)/2)],"")
    return string

def recursion(string):
    new_str=clean(string)
    if (len(new_str)==0):
        return True
    elif (len(new_str)%2==0):
        if (new_str[0]==new_str[-1]):
            return recursion(new_str[1:-1])
        else:
            return False
    return False
print(recursion("HannannaH"))
