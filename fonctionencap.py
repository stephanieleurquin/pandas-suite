#fonction pair  et impair
def est_pair(x):# fonction appelle  est_pair qui prend un parametre X
    #une fonction  est un morceau de code que tu peux reutiliser pour faire un calcul ou une action

    return x % 2 == 0 # Le symbole % en Python signifie modulo, c’est-à-dire le reste de la division de x par 2.
print((est_pair(4))) #true
print((est_pair(7))) #false