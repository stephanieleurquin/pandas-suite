#afficher tous les fruits un par un
nom = "David"
age= 23
fruits = ["bananes","fraises","framboise"]
fruits.append("ananas")
print (nom, "a",age,"ans", "et aime ces fruits")
#parcourir  la liste avec for fruits in fruits
for fruit in fruits:
    print(fruit)
for i in range(len (fruits)):
    print (i +1,fruits[i])



