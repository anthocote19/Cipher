# Affine Cipher - Encryption and Decryption using Hugo Pratt quotes

This project demonstrates two cryptographic operations using the **affine cipher**:
1. Encrypting a message with key (a=7, b=8)
2. Decrypting a message with key (a=5, b=10)

---

## 1. Encryption

### Key used: a = 7, b = 8

### Original text:
"Je ne suis pas assez sérieux pour donner des conseils et je le suis trop pour en recevoir"

### Steps:
- Use the alphabet without accents or punctuation.
- Convert each letter to its position in the alphabet (A=0, B=1, ..., Z=25).
- Apply the encryption formula:  
  **E(x) = (a * x + b) mod 26**
- Convert the result back to letters.

### Encrypted text:
----------------------------------------------------------------------------------------

---

## 2. Decryption

### Encrypted text:
"YNJKG BHNGW ZEUCG RKOEH CGRLY LREEX NKUTE MGEHC GRSCG RYREX TERCW"

### Key used: a = 5, b = 10

### Decryption steps:
- Find the modular inverse of `a=5` modulo 26.  
  **a⁻¹ mod 26 = 21**, because (5 × 21) mod 26 = 1.
- Apply the decryption formula:  
  **D(x) = a⁻¹ * (x - b) mod 26**
  → **D(x) = 21 * (x - 10) mod 26**

### Decrypted text:
--------------------------------------------------------------------------------------

---

## References:
- Quote 1: "Sous le signe du Capricorne" by Hugo Pratt.
- Quote 2: "Corto toujours un peu plus loin" by Hugo Pratt.

---

## Notes:
- The alphabet used does not include accents; punctuation and spacing were removed or adapted for encryption.
- The affine cipher is easy to implement but vulnerable to frequency analysis and not considered secure.

 
