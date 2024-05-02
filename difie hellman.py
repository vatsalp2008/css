x = int(input("enter private key of A : "))
y = int(input("enter private key of B : "))
p = int(input("Enter modulus : "))
g = int(input("enter primitive root : "))

r1 = g**x % p
r2 = g**y % p 
print("public key of A is :",r1)
print("public key of B is :",r2)

k1 = (r2)**x % p
k2 = (r1)**y % p
print("session key with A Ka is :",k1)
print("session key with B Kb is :",k2)

k = g**(x*y) % p
print("session key K is :",k)