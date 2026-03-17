class Voiture:
    def __init__(self,marque, modele,annee):
        self.marque= marque
        self.modele =modele
        self.annee= annee
    def demarrer(self):
        print (f"la voiture demarre")

class electrique (Voiture):

    def demarrer(self):
        print(f"La voiture electrique demarre silencieusement")
#creation
ma_tesla = Electrique("Tesla,")



class essence(Voiture):
    def demarrer(self):
        print(f"La voiture essence demarre  avec du bruit")

#creation des objets
ma_tesla =electrique("tesla","electrique", 2020)
ma_fiat_essence=essence ("fiat", "essence", 1995)



#les methodes en application

ma_tesla.demarrer()
ma_fiat_essence.demarrer()