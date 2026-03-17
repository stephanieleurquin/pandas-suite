legumes =  ["carottes", "tomates" , "navet" , "brocoli","radis"]
for legume in legumes:
    print(legume)
    if  len (legume) >6: #len est une fonction  qui calcule la longueur de quelque chose
        print (legume, "est long")
    else:
        print (legume, "est court")