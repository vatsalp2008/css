x = int(input("enter private key of A : "))
y = int(input("enter private key of B : "))
z = int(input("enter private key of middleMan : "))
p = int(input("Enter modulus : "))
g = int(input("enter primitive root : "))
print("-----------------------man in middle------------------------------")

r1 = g**x % p
r2 = g**z % p  
r3 = g**y % p  
print("public key of A is :",r1)
print("public key of middleMan is :",r2)
print("public key of B is :",r3)

k1 = (r2)**x % p
k2 = (r2)**y % p
print("session key with A Ka is :",k1)
print("session key with B Kb is :",k2)
km1 = (r1)**z % p
km2 = (r3)**z % p
print(f"session keys with middleMan Ka is {km1} and kb is {km2} :")


kam =  g**(x*z) % p
kmb =  g**(z*y) % p
print(f"session key between A and M is {kam} & between M and B is {km2} :")
