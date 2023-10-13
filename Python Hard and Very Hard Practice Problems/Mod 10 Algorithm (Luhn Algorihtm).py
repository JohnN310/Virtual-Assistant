def valid_credit_card(number):
    i=len(str(number))-1
    string= str(number)
    count=0
    total=0
    while i>=0:
        if count % 2!=0:
            if 2*(int(string[i])) <10:
                total+=2*(int(string[i]))
            else:
                for digit in str(2*(int(string[i]))):
                    total+=int(digit)
            count+=1
        else:
            total+=(int(string[i]))
            count+=1
        i-=1
    return total % 10==0
print (valid_credit_card(4111111111111111))