#statistiques excercices
notes = [12,15,18,10,14,17,9]

# 1 crer la fonction
def calcul_stats(notes):
    #calculer la moyenne
    moyenne = sum (notes)/len (notes)

    #trouver la note la plus haute

    notes_max = max(notes)
    #trouver la note la plus faible
    notes_min =min (notes)
    #retourner les resultats
    return moyenne,notes_max, notes_min

# 2 appeler la fonction
moyenne, note_max, note_min=calcul_stats (notes)
print("moyenne :", moyenne)
print("notes max :",note_max)
print("notes min:", note_min)



