from random import randint

# Génération d'un nombre aléatoire compris entre 1 et 100
solution = randint(1, 100)

# Initialisation des variables pour les while qui vont suivre
nombreEssais = 0
proposition = 0
difficulte=""

name = input("Quel est votre prénom ? ")

# Première façon d'inclure des variables dans les print ( ..." + var + ".... )
print("Bonjour " + name + ", devinez le nombre entre 1 et 100, vous avez 10 essais.")

while (difficulte != "oui" and difficulte != "non"):
    difficulte = input("Souhaitez-vous augmenter la difficulté en diminuant le nombre d'essais ? taper oui ou non ")

if difficulte == "oui":
    while (nombreEssais < 1  or nombreEssais > 10):
        nombreEssais = int(input("Choisissez un nombre d'essai entre 1 et 10 : "))
else :
    nombreEssais = 10

print("Vous aurez donc " + str(nombreEssais) + " essais, bonne chance !")

print("==================================================================")
print("Le jeu commence...")

for i in range(nombreEssais):

    while (proposition < 1  or proposition > 100):
        # Seconde façon d'inclure des variables dans les print ( {} puis ...".format(var)) )
        proposition = int(input("Entrez un nombre (essai {}): ".format(i + 1)))

    if proposition < solution:
        print("↑ Plus ↑")
    elif proposition > solution:
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

    # Je force cette var à zero afin d'invalider le while de la ligne 32 et lui permettre la vérification (proposition entre 1 et 100) lors de la prochaine poposition
    proposition = 0

# Le joueur n'a pas trouvé le nombre à deviner...
if proposition != solution:
    print("Perdu")
    print("Le nombre à deviner était: {}".format(solution))

print("Fin du jeu")