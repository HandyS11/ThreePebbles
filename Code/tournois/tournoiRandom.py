import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsRandomObjet import *


[choix, prediction] = loadModele()

nbGames = 1000
nbCaillouxJ1 = 3
nbCaillouxJ2 = 3

print("Début de la simulation ..\n")
tempsD = time.time()

for i in range(4):
    choixModele = choix[i]

    for j in range(4):
        predictionModele = prediction[j]

        sommeRounds = 0
        nbVictoireIA = 0

        print("Simulation n°", i, j)

        for k in range(nbGames):
            [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)

            sommeRounds = sommeRounds + round

            if (winner == 1):
                nbVictoireIA = nbVictoireIA + 1

        dureeM = sommeRounds/nbGames
        pourcentageV = nbVictoireIA/nbGames*100

        print("Pourcentage de victoire de", pourcentageV, "%")
        print("La durée moyenne des parties est de", dureeM, "rounds.\n")


tempsF = time.time()
tempsS = tempsF - tempsD
print("La simulation a durée", tempsS, "secondes.\n")