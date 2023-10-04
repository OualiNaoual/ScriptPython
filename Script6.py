# Ecrire un programme qui va lire les données d'un employé à partir du clavier
# les données demandées sont: id, nom, salaire, adresse, marié
id = int(input("Veuillez saisir votre ID: "))
nom = input("Veuillez saisir votre nom : ")
salaire = float(input("Veuillez saisir votre salaire : "))
adresse = input("Veuillez saisir votre adresse : ")
marie = bool(input("etes vous marié : [True/False]"))
print("l'employé numéro",id,"s'appelle ", nom, "a un salaire de ", salaire,"habite à ", adresse,'marié: ', marie)

