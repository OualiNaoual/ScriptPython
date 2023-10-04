# Ecrire un programme qui choisi le plus grand nombre parmi deux nombre saisi a partir du clavier
a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxieme nombre : "))
if a < b:
    print("Le plus grand nombre est : ", b)
elif a == b:
    print("Les deux nombres sont égaux")
else:
    print("Le plus grand nombre est : ", a)
