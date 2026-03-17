legumes = ["carottes", "tomates", "navets", "brocoli" ,"radis", "poireaux"]
for  legume in legumes: # legume = chaque mot de la liste
    if len (legume) > 6:# longueur du mot
        print (legume, "est long")
    else:
        print(legume, "est court")
