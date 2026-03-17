import random
#nombre de tirages
n_tirages =10000

#generer  10 nombres aleatoires entre 1 et 20
tirages = [random.randint(1, 20) for _ in range(n_tirages)]
pairs = sum (1 for n in tirages if n % 2  == 0)
impairs = n_tirages -pairs
#calculer les probabilites
prob_pair = pairs/ n_tirages
prob_impairs = impairs/n_tirages

#afficher les reultat
print("tirages: ", tirages)
print("nombre de pairs: ", pairs)
print("nombres d'impairs: ", impairs)
print("probabilite de pair: ", prob_pair)
print("probabilite d'impair: ", prob_impairs)


