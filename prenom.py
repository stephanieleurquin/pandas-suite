noms = ["Lina","Alexandre" ,"Tom","Sophie", "Max", "Camille"]
for nom in noms: #est au singulier pour prendre chaque nom séparement
    if len(nom) > 5:
        print (nom, "prenom long")
    else:
        print (nom, "prenom court")
