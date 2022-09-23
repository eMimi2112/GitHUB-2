# Ecrivez un programme qui :
# Demande à l’utilisateur un nombre, et qui continue à demander tant 
# que le nombre n’est pas entre 1 et 5

from random import randint
number = input("Entrez un nombre svp:")
number = int(number)
# Génère un nombre aléatoire (entre 1 et 5)
C = randint(1, 5)

# Ensuite le programme affiche le nombre généré avec entre parenthèses
#la différence entre les deux nombres
while not (1 <= number <= 5) :
    number = int(input("Entrez un nombre : "))
    number = int(number)

print(str(C) + "-" + (str(number)) + "=" + str(C -number))


# Exemple:
# Si le nombre aléatoire est 3 et le nombre donnée par l’utilisateur 
# est 5 l’affichage sera:"3 (-2)"
# ici, j'ai oublié de mettre le "number=int(number)" 