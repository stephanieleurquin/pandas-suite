# Classe de base Animal
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Je fais un bruit")  # Bruit générique pour un animal

# Classe Chien qui hérite de Animal
class Chien(Animal):
    def parler(self):
        print("Woof! Woof!")  # Son spécifique du chien

# Classe Chat qui hérite de Animal
class Chat(Animal):
    def parler(self):
        print("Miaouw")  # Son spécifique du chat

# Création des objets
mon_chien = Chien("Rex", 5)
mon_chat = Chat("Minou", 3)

# Appel des méthodes
mon_chien.parler()  # Affiche: Woof! Woof!
mon_chat.parler()   # Affiche: Miaouw