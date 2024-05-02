def generalcipher(str1,key):
    str2 = [x for x in str1 if x.isalpha() or x ==" "]
    str3 = ""
    for i in str2:
        if i == " ":
            str3 += i
        else:
            if(i.islower()):
                str3 += chr(((ord(i) -97 + key) %26) + 97) 
            else :
                str3 += chr(((ord(i) -ord("A") + key) %26) + ord("A") ) 
 
    return str3
def decryptGeneralcipher(str1,key):
    str2 = [x for x in str1 if x.isalpha() or x ==" "]
    str3 = ""
    for i in str2:
        if i == " ":
            str3 += i
        else:
            if(i.islower()):
                str3 += chr(((ord(i) -97 - key) %26) + 97) 
            else :
                str3 += chr(((ord(i) -ord("A") - key) %26) + ord("A") )  
 
    return str3


str1 = input("Enter the string : ")
key = int(input("enter the key : "))
cipherText = generalcipher(str1,key)
print(cipherText)
plainText = decryptGeneralcipher(cipherText,key)
print(plainText)

