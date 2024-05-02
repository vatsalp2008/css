import math

# Function to calculate gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate modular exponentiation (base^exp % mod)
def modExp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Function to generate public and private keys
def generateKeys():
    # Two random prime numbers
    p = 61
    q = 53

    # Calculate n and Euler's totient (phi)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 17  # Commonly used value
    
    # Calculate d, the modular multiplicative inverse of e (d * e ≡ 1 (mod phi))
    d = 1
    while (d * e) % phi != 1:
        d += 1

    return n, e, d

# Function to perform RSA encryption
def encrypt(message, e, n):
    return modExp(message, e, n)

# Function to perform RSA decryption
def decrypt(ciphertext, d, n):
    return modExp(ciphertext, d, n)

def main():
    n, e, d = generateKeys()
    
    # Message to be encrypted
    msg = 1103
    print("Message data =", msg)
    
    # Encryption c = (msg ^ e) % n
    encryptedData = encrypt(msg, e, n)
    print("Encrypted data =", encryptedData)
    
    # Decryption m = (c ^ d) % n
    decryptedMessage = decrypt(encryptedData, d, n)
    print("Original Message Sent =", decryptedMessage)

if __name__ == "__main__":
    main()





# The RSA algorithm, named after its inventors Ron Rivest, Adi Shamir, and Leonard Adleman, is a widely used cryptographic algorithm for secure communication over insecure channels. It relies on the mathematical complexity of factoring large prime numbers to provide security. Here's a concise explanation of how the RSA algorithm works:

# 1. **Key Generation**:
#    - Choose two distinct large prime numbers, \( p \) and \( q \).
#    - Compute their product, \( n = pq \), which is used as the modulus for both the public and private keys.
#    - Calculate the Euler's totient function of \( n \), denoted as \( \phi(n) = (p-1)(q-1) \).
#    - Choose an integer \( e \) such that \( 1 < e < \phi(n) \) and \( e \) is coprime with \( \phi(n) \). \( e \) will be the public exponent.
#    - Compute the private exponent \( d \) such that \( de \equiv 1 \mod \phi(n) \). This can be done using the Extended Euclidean Algorithm.

# 2. **Public and Private Keys**:
#    - The public key consists of \( (n, e) \) and is made available to anyone who wants to send encrypted messages.
#    - The private key consists of \( (n, d) \) and is kept secret by the receiver.

# 3. **Encryption**:
#    - To encrypt a message \( M \) into ciphertext \( C \), the sender uses the recipient's public key \( (n, e) \).
#    - The sender computes \( C \equiv M^e \mod n \) and sends \( C \) to the receiver.

# 4. **Decryption**:
#    - The recipient uses their private key \( (n, d) \) to decrypt the ciphertext \( C \) and recover the original message \( M \).
#    - The recipient computes \( M \equiv C^d \mod n \).

# 5. **Security**:
#    - The security of RSA relies on the difficulty of factoring the product of two large prime numbers \( n \) into its constituent primes \( p \) and \( q \). As of now, no efficient algorithm exists to factor large numbers into their primes, making RSA secure when sufficiently large keys are used.

# 6. **Usage**:
#    - RSA is widely used for secure communication, digital signatures, and key exchange protocols such as SSL/TLS.

# In summary, the RSA algorithm provides a method for secure communication by leveraging the mathematical properties of prime numbers and modular arithmetic. Its security relies on the computational complexity of factoring large integers, which forms the basis of its resistance to attacks.