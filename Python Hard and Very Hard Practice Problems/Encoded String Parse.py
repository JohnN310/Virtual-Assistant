def parse_code(txt):
    fname=txt[0:txt.index('0')]
    txt=txt.replace("0","")
    remaining=txt[txt.index(fname[-1])+1:]
    digits=[1,2,3,4,5,6,7,8,9]
    i=0
    lname=""
    id=""
    while i<len(remaining):
        if remaining[i].isdigit():
            lname=remaining[0:i]
            id=remaining[i::]
            break
        i+=1
    dictionary={"first name":fname,
                "last name": lname,
                "id": id}
    return dictionary
print(parse_code("Thomas00LEE0000043"))