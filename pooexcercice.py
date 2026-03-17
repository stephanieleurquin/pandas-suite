class Chien:
    def __init__(self , nom, race,age):
        self.nom = nom
        self.age =age
        self.race= race

    def aboyer(self):
        print(f"{self.nom} aboit! Je m'appelle  {self.nom} et je suis de race {self.race}.")

chien1= Chien("Max", "Berger Allemand", 5)
chien2 =Chien("Bella","Labrador",2)



chien1.aboyer()
chien2.aboyer()





