def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

def affine_decrypt(cipher, key):
    mod_inverse = modinv(key[0], 26)
    if mod_inverse is None:
        return "Modular inverse does not exist"
    return ''.join([chr(((mod_inverse * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])

def main():
    text = input("Enter the plaintext: ").upper()
    key_a = int(input("Enter the first key (a): "))
    key_b = int(input("Enter the second key (b): "))
    key = [key_a, key_b]

    affine_encrypted_text = affine_encrypt(text, key)
    print('Encrypted Text: {}'.format(affine_encrypted_text))

    decrypted_text = affine_decrypt(affine_encrypted_text, key)
    print('Decrypted Text: {}'.format(decrypted_text))

if __name__ == '__main__':
    main()
