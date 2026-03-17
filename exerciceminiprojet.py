#DataFrame à créer :

#produit	prix	quantité
#Pommes	2	50
#Bananes	1	100
#Oranges	3	80

import pandas as pd

data= {
  "produit":["Pomme","Bananes","Orange"],
   "prix": [2,1,3],
 "quantite":[50,100,80],
}
df = pd.DataFrame(data)
print ("DataFrame complet:")
print (df)
# 1 prix moyen
prix_moyen = df["prix"].mean()
print ("\nPrix moyen :",  prix_moyen)

#2 Total des quantité
total_quantité =df ["quantite"].sum() #faire attention au accent
print ("Total des quantites : ", total_quantité)
