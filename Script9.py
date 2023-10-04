# Ecrire un programme qui va trouver le plus grans nombre à partir de trois nombres saisis au clavier
a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxieme nombre : "))
c = int(input("entrer le troisieme nombre : "))
if a > b and a > c:
    print("Le plus grand nombre est : ", a)
elif b > c:
    print("Le plus grand nombre est : ", b)
else:
    print("Le plus grand nombre est : ", c)

