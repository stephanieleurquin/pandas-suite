import pandas  as pd
prenoms= ["Sophie", "Anne", "Michele", "Gilles","Claudine", "Tom", "Lina", "Sophie", "Anne" , "Gilles" ,"Anne"]
#supprimer les espaces autour des prenoms
prenoms = [p.strip() for p in prenoms]

           #creer une Dataforame
df = pd.DataFrame({"prenom" : prenoms})

 #compter combien de fois chaque prenom appararait
compteur = df ["prenom"].value_counts()
print(compteur)