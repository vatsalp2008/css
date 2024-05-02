def encrypt(str1,key):
    str2 = ""
    key1 = [ord(x.lower()) - 97 for x in key ]
    z = len(key1)
    j = 0
    for i in range(0,len(str1)):
        if str1[i]== " ":
            str2+= str1[i]
        else:
            str2+= chr((ord(str1[i])- 97 + key1[j % z])%26  + 97)
            j +=1
    return str2

    
def decrypt(str1,key):
    str2 = ""
    key1 = [ord(x.lower()) - 97 for x in key ]
    z = len(key1)
    j = 0
    for i in range(0,len(str1)):
        if str1[i]== " ":
            str2+= str1[i]
        else:
            str2+= chr((ord(str1[i])- 97 - key1[j % z])%26  + 97)
            j +=1
    return str2
   


str1 = input("Enter the string : ")
key = input("enter the key : ")
cipherText = encrypt(str1,key)
print(cipherText)
plainText = decrypt(cipherText,key)
print(plainText)

