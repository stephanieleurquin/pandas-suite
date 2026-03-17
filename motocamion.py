#exercice  de polymorphysme
# dans le polymorphisme , plusieurs classes utilisent la emme methodes ; demarrer ici dans l exercice mais
# les classes font toutes quelque chose de different.

class Vehicule:#le parent  de la classe moto et camion
    def __init__(self, marque): #sert à creer l'objet et stocker la marque
                 self.marque =marque

    def demarrer (self): #demmarrer est la methode qu on va definir dans les enfantrs
        print(f"Le vehicule{self.marque}demarre")

class Camion(Vehicule):#enfant de Vehicule
     def demarrer (self):
         print(f"Le camion{self.marque}demarre lentement")
class Moto (Vehicule):#enfant de Vehicule
    def demarrer(self):
        print(f"La moto{self.marque}demarre rapidement")

#creer des objets et  tester
c1=Camion("Volvo")#le camion Volvo demarre lentement
m1=Moto("Yamaha") #la moto Yamaha demarre rapidement

#appel des methodes
c1.demarrer()
m1.demarrer()


# test de polymorphisme
vehicule =[c1,m1]
for v in vehicule: #le polymorphisme est ici . Liste contennat camion et moto
    v.demarrer() #meme commande mais resultat different
