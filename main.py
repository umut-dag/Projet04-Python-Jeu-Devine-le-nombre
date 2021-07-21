from random import randint

# Génération d'un nombre aléatoire compris entre 1 et 100
solution = randint(1, 100)

# Initialisation des variables
nombreEssais = 0
proposition = 0
difficulte=""

print("Quel est votre prénom ?")
name = input()

print("Bonjour " + name + ", devinez le nombre entre 1 et 100, vous avez 10 essais.")

while (difficulte != "oui" and difficulte != "non"):
    difficulte = input("Souhaitez-vous augmenter la difficulté en diminuant le nombre d'essais ? taper oui ou non ")

if difficulte == "oui":
    while (nombreEssais < 1  or nombreEssais > 7):
        nombreEssais = int(input("Choisissez un nombre d'essai entre 1 et 7 : "))
else :
    nombreEssais = 10

print("Vous aurez donc " + str(nombreEssais) + " essais, bonne chance !")

print("==================================================================")
print("Le jeu commence...")

for i in range(nombreEssais):

    while (proposition < 1  or proposition > 100):
        proposition = int(input("Entrez un nombre (essai {}): ".format(i + 1)))

    if proposition < solution:
        # print("Le nombre a deviner est plus grand que {}".format(essai))
        print("↑ Plus ↑")
    elif proposition > solution:
        # print("Le nombre a deviner est plus petit que {}".format(essai))
        print("↓ Moins ↓")
    elif proposition == solution:
        if i + 1 < 5:
            print("==================================================================")
            print("   Waaaooooow, c'est génial. Vous avez trouvé le nombre {} en seulement {} essais, BRAVO !".format(solution, i + 1))
            print("==================================================================")
        else:
            print("==================================================================")
            print("   Bravo, vous avez trouvé le nombre {} en {} essais".format(solution, i + 1))
            print("==================================================================")
        break

    # Je force cette var à zero afin d'invalider le while de la ligne 32 et lui permettre la vérification (1-100) de la prochaine poposition
    proposition = 0

# Le joueur n'a pas trouvé le nombre à deviner...
if proposition != solution:
    print("Perdu")
    print("Le nombre à deviner était: {}".format(solution))

print("Fin du jeu")