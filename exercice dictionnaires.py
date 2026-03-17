#excercice de dictionnaire
produit = {
    "nom": "ordinateur",
    "prix": 80,
    "stock": 10

}
#afficher le prix
print ("le prix est :",produit ["prix"])


# modifier le stock
produit["stock"] = 5
# ajouter une categorie
produit ["categorie"] = "informatique"

#afficher le dictionnaire final
print (produit)