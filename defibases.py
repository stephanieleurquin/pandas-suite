#mon sac de fruits special

fruits=["ananas","gingembre","melon", "fraise","cassis","menthe"]
#creer une fonction qui parcourt les fruits : si le fruit est fraise, affiche j adore les fraises
#sinon , affiche ; ce n est pas ma fraise
fruits.append ("noix de coco")#j ajoute un fruit
def manger_fruits (fruits): # on declare la fonction ici
    for fruit in fruits:#
        if fruit == "fraise":
            print("j'adore  les fraise")
        else:
            print("ce n 'est pas ma fraise")

#j appelle la fonction pour python affiche le resultat des fruits
manger_fruits(fruits)