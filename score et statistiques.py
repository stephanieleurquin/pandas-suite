#fonction pour afficher les statistiques  d'une liste de scores
def statistiques (scores): #fonction encapsulee
    total = sum(scores)
    moyenne =total/len(scores)
    maximum = max (scores)
    minimum= min (scores)

    print("score :", scores)
    print("score total : ",total)
    print("score moyen: ", moyenne)
    print("score le plus élévé:",maximum)
    print("score le plus faible :",minimum)
    print() #juste pour espacer entre les tests

#liste de scores
score_maximum= [12,20,50,14,89]
#appeler la fonction
statistiques (score_maximum)