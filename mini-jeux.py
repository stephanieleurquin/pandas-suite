import random
nombre = random.randint(0,11)
devine= -1
while devine != nombre:
    devine = int(input("devine le nombre entier entre 0 et 11 "))
if devine == nombre:
        print("Bravo, tu as deviné !!")


