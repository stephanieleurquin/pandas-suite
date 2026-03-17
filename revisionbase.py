#verifier si un nombre est premier
nombre= int(input("donnes moi un nombre : "))
premier= True
if nombre <=1:
    premier= False
else :#tester  tous les  diviseurs possible
    for i in range(2, nombre):
        if nombre % i ==0 :
            premier =False
            break
if premier:
    print(nombre , "est premier")

else:
    print(nombre, "n'est pas premier")





