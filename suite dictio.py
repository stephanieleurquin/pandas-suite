produit= {
    "nom" : "prima",
    "prix":"80",
    "stock": 12000

}
#afficher le nom et le prix du produit
print ("le prix est :", produit["prix"])
print ("le nom est :", produit["nom"])

#reduire le stock de 1
produit["stock"] -=1

#ajouter une categorie
produit["categorie"] ="informatique"

# afficher le dictionnaire finale
print("\nDictionnaire final:") # tu as un texte explicatif avant le dictionnaire.
print (produit)

