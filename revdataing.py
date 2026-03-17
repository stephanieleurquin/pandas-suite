#creer des listes
fruits = ["pomme", "banane","cerise", "kiwi","fraise"]

# afficher le premier et le dernier fruits
print("premier: ", fruits[0])
print ("dernier:", fruits[1])
#ajouter un nouveau fruit
fruits.append ("orange")
#afficher la liste entiere apres ajout
print("nouvelle liste :",fruits)
# afficher  tous les fruits un par un
for fruit in fruits:
    print(fruit)