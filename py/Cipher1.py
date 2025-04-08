def nettoyer_texte(texte):
    texte_nettoye = ''
    for caractere in texte:
        if caractere.isalpha():
            texte_nettoye += caractere.upper()
    return texte_nettoye


def chiffrement_affine(texte, a, b):
    texte = nettoyer_texte(texte)
    texte_chiffre = ''
    for lettre in texte:
        x = ord(lettre) - ord('A') 
        y = (a * x + b) % 26        
        lettre_chiffree = chr(y + ord('A'))  
        texte_chiffre += lettre_chiffree
    return texte_chiffre


texte = "Je ne suis pas assez sérieux pour donner des conseils et je le suis trop pour en recevoir"
a = 7  
b = 8  


texte_chiffre = chiffrement_affine(texte, a, b)


print("Texte chiffré :")
print(texte_chiffre)


