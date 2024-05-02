def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")
    print(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=key.index))
    print(key)
    key += ''.join(sorted(set(alphabet) - set(key)))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def get_char_positions(matrix, char):
    return next((i, row.index(char)) for i, row in enumerate(matrix) if char in row)

def playfair_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "").replace("J", "I")
    matrix = generate_playfair_matrix(key)
    pairs = [(plain_text[i], plain_text[i + 1] if i + 1 < len(plain_text) else 'X') for i in range(0, len(plain_text), 2)]
    encrypted_text = ""
    for pair in pairs:  
        pos1, pos2 = [get_char_positions(matrix, char) for char in pair]
        if pos1[0] == pos2[0]:  # Same row
            encrypted_text += matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5]
        elif pos1[1] == pos2[1]:  # Same column
            encrypted_text += matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]]
        else:  # Rectangle
            encrypted_text += matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
    return encrypted_text

# Example usage:
plaintext = "HELLO WORLD"
key = "PLAYFAIREXAMPLE"
encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)