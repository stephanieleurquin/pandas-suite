#crer un dictionnaire vide


profil= {}

#ajouter ds informations

profil["nom"]= "Charlie"
profil ["age"] = 28
profil ["profession"]= "étudiant"
#afficher les informations

print("nom",profil["nom"])
print("age",profil["age"])
print("profession",profil["profession"])

#excercice optionnel
#ajouter un noubveklle personne dans un autre  dictionnaire
profil2={
    "nom" : "Emma",
    "age" : 25,
    "profession": "medecin"
}


  #modifier les valeurs

profil2 ["age"] = 26
profil2 ["profession"] = "chirurgien"
#supprimer  la clé profession du profil 2
profil2.pop("profession")

#afficher toutes les informations
#affiche toutes les informations restantes profil2

print("nom: ",profil2["nom"])
print("age: ",profil2["age"])









