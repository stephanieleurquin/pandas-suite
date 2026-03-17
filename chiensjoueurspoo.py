class Chien:
    def __init__(self , nom, race,age):
        self.nom = nom
        self.age =age
        self.race= race

    def aboyer(self):
            print(f"{self.nom} aboit! Je m'appelle  {self.nom} et je suis de race {self.race}.")
    def jouer(self):
        print (f"{self.nom} joue avec moi! Je m'appelle {self.nom}")

    def veillir(self):
        self.age +=1 #on augmente l'age de 1
        print(f"{self.nom} a maintenant {self.age}ans.")

#creation des objets
chien1 = Chien("Bobby", "collie", 3)
chien2 = Chien("Grigny", "caniche", 6)

#appel des methodes
chien1.aboyer()
chien2.aboyer()

chien1.jouer()
chien2.jouer()

chien1.veillir()
chien2.veillir()