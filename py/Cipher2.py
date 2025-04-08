def mod_inverse(a, m):
    """Retourne l'inverse modulaire de a modulo m"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)

    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % 26
            decrypted_char = chr(x + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char 

    return decrypted_text


cipher_text = "YNJKG BHNGW ZEUCG RKOEH CGRLY LREEX NKUTE MGEHC GRSCG RYREX TERCW"
a = 5
b = 10


decrypted = affine_decrypt(cipher_text, a, b)
print("Texte déchiffré :")
print(decrypted)
