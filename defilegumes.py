legumes= ["carottes", "poireaux","endive","pommes de terre","navets"] #on cree une liste
def verifier_poireaux(legumes):   #on cree un fonction verifier_poireaux
    for legume in legumes:
        if legume == ("endive"):
            print("j'adore les endives comme plat principal")
        else:
            print("ce n'est pas mon endive")
verifier_poireaux(legumes)

