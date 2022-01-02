from modules import *
from loader import *
sys.path.append("./games")
from gameIAvsIAObjet import *


[choix, prediction] = loadModele()

nbGames = 10
nbCaillouxJ1 = 3
nbCaillouxJ2 = 3

print("Début de la simulation ..\n")
tempsD = time.time()

for i in range(4):
    choixModeleJ1 = choix[i]

    for j in range(4):
        predictionModeleJ1 = prediction[j]

        for k in range(4):
            choixModeleJ2 = choix[k]

            for l in range(4):
                predictionModeleJ2 = prediction[l]

                sommeRounds = 0
                nbVictoireJ1 = 0

                print("Simulation n°", i, j, k, l)

                for m in range(nbGames):
                    [winner, round, tab] = gameIAvsIAObjet(nbCaillouxJ1, nbCaillouxJ2, choixModeleJ1, predictionModeleJ1, choixModeleJ2, predictionModeleJ2)

                    sommeRounds = sommeRounds + round

                    if (winner == 1):
                        nbVictoireJ1 = nbVictoireJ1 + 1

                    dureeM = sommeRounds/nbGames
                    pourcentageV = nbVictoireJ1/nbGames*100

                    print("Pourcentage de victoire du joueur 1 :", pourcentageV, "%")
                    print("La durée moyenne des parties est de", dureeM, "rounds.\n")

tempsF = time.time()
tempsS = tempsF - tempsD
print("La simulation a durée", tempsS, "secondes.\n")