class Camion:
    def __init__(self, marque, vitesse_max):
        self.__marque = marque          # attribut privé
        self.__vitesse = 0              # attribut privé
        self._vitesse_max = vitesse_max # attribut protégé

    # Méthode publique pour démarrer le camion
    def demarrer(self):
        print(f"Le camion {self.__marque} démarre.")

    # Méthode pour accélérer
    def accelerer(self, val):
        if self.__vitesse + val < self._vitesse_max:
            self.__vitesse += val
        else:
            self.__vitesse = self._vitesse_max
        print(f"Vitesse actuelle: {self.__vitesse} km/h")

    # Getter pour accéder à l'attribut privé
    def get_marque(self):
        return self.__marque

    # Setter pour modifier un attribut privé
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque


# Bloc principal hors de la classe
if __name__ == "__main__":
    camion1 = Camion("Volvo", 120)
    camion1.demarrer()
    camion1.accelerer(50)
    print(camion1.get_marque())
    camion1.set_marque("Scania")
    print(camion1.get_marque())
