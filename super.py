#ajouter la methode super ( fonction integree)
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele =modele
        self.annee =annee
    def demarrer(self):
        print("la voiture demarre")


class Electrique(Voiture):
    def __init__(self, marque, modele, annee, batterie):
        super().__init__(marque, modele, annee)
        self.batterie = batterie

    def demarrer(self):
        print("la voiture demarre")

class Essence(Voiture):
    def demarrer (self):
        print("la voiture essence demarre avec du bruit")
#creation des objets
ma_tesla =Electrique("tesla", "modele 3" , 2022,75)
ma_fiat_essence = Essence("Fiat", "500", 1995)
#appel des methodes
ma_tesla.demarrer()
ma_fiat_essence.demarrer()
print("Batterie de la tesla :", ma_tesla.batterie,"Kwh")
