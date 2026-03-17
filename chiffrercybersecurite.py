def chiffrer(message, decalage):
    resultat = ""

    for lettre in message:
        if lettre.isalpha():
            base = ord('a')
            code = (ord(lettre) - base + decalage) % 26
            resultat += chr(base + code)
        else:
            resultat += lettre

    return resultat


message = input("Message à chiffrer : ")
decalage = int(input("Décalage : "))

print("Message chiffré :", chiffrer(message, decalage))