class AutoKey:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def main():
        msg = input("Enter the plaintext: ").upper()
        key = input("Enter the key: ").upper()

        if key.isdigit():
            key = AutoKey.alphabet[int(key)]

        enc = AutoKey.auto_encryption(msg, key)

        print("Plaintext:", msg)
        print("Encrypted:", enc)
        print("Decrypted:", AutoKey.auto_decryption(enc, key))

    @staticmethod
    def auto_encryption(msg, key):
        new_key = key + msg
        new_key = new_key[:len(new_key) - len(key)]
        encrypt_msg = ""

        for x in range(len(msg)):
            first = AutoKey.alphabet.index(msg[x])
            second = AutoKey.alphabet.index(new_key[x])
            total = (first + second) % 26
            encrypt_msg += AutoKey.alphabet[total]

        return encrypt_msg

    @staticmethod
    def auto_decryption(msg, key):
        current_key = key
        decrypt_msg = ""

        for x in range(len(msg)):
            get1 = AutoKey.alphabet.index(msg[x])
            get2 = AutoKey.alphabet.index(current_key[x])
            total = (get1 - get2) % 26
            total = total + 26 if total < 0 else total
            decrypt_msg += AutoKey.alphabet[total]
            current_key += AutoKey.alphabet[total]

        return decrypt_msg

AutoKey.main()
