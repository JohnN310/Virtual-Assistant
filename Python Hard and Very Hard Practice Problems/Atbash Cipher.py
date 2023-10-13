def atbash(string):
  temp=string
  string=string.lower()
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  i=0
  new_str=''
  while i<len(string):
    if (string[i] in alphabet):
      new_str+=string[i].replace(string[i], alphabet[25-alphabet.index(string[i])],1)
    else:
        new_str+=string[i]
    i+=1
  j=0
  final_str=''
  while j<len(string):
    if (temp[j].isupper()):
      final_str+=new_str[j].upper()
    else:
        final_str+=new_str[j]
    j+=1
  return final_str
print(atbash('applE'))