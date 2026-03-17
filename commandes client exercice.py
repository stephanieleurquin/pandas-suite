
#creer un DATA FRAME  qui reprends la table comamnde dans sql lite
import pandas as pd
#creation du DATAFRAME
data= {
    'client_id' : [1, 2, 1, 4, 1, 3],
    'produit' : ['ordinateur', 'souris' , 'clavier', 'ecran','souris',' webcam'],

}
#chaque ligne correspond à une commande

commandes = pd.DataFrame(data)

#afficher les données
print (commandes) #verifier que le DATA FRAME corespond bien à la table sql

#etape 2 Compter le nombre  de commande par client

nb_commandes = commandes.groupby('client_id').size().reset_index(name='nb_commandes')
print (nb_commandes)

#etape 3 Filter les client avec plus d une commandes
clients_plus_1 = nb_commandes[nb_commandes['nb_commandes'] > 1]

print(clients_plus_1)

#etape 4 : ajouter un  classement
# Classement du client avec le plus de commandes
clients_plus_1['rang'] = clients_plus_1['nb_commandes'].rank(method='first', ascending=False).astype(int)

print(clients_plus_1)

