# input s = "hai" , expected out = "jck" 
# we can store complete alpha.. in an array
# lopp through the string and  replace each character with next one.
# O(n) ts

import string
def encodeString(str, count):
    alp = string.ascii_letters
    res=[]

    # Calculate the actual shift
    shift = count % 26 

    for  i in range(len(str)):
        word = str[i]
        alphaIndex = alp.index(word)
        res.append(alp[alphaIndex + shift])
        
    return "".join(res)


print(encodeString("hai", 2))