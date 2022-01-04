import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsIAObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                     Tournoi IA vs IA (object)                    ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def tournoiIAvsIA(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    print("Début de la simulation ..\n")
    tempsD = time.time()

    listeWinrate = []
    listeLength = []
    listeName = []

    for i in range(len(choix)):
        choixModeleJ1 = choix[i]

        for j in range(len(prediction)):
            predictionModeleJ1 = prediction[j]

            for k in range(len(choix)):
                choixModeleJ2 = choix[k]

                for l in range(len(prediction)):
                    predictionModeleJ2 = prediction[l]

                    sommeRounds = 0
                    nbVictoireJ1 = 0

                    print("Simulation n°", i, j, k, l)

                    for m in range(nbGames):
                        [winner, round] = gameIAvsIAObjet(nbCaillouxJ1, nbCaillouxJ2, choixModeleJ1, predictionModeleJ1, choixModeleJ2, predictionModeleJ2)

                        if (round == -1):
                            break

                        if (winner == 1):
                            nbVictoireJ1 = nbVictoireJ1 + 1

                        sommeRounds = sommeRounds + round

                    if (round != -1):
                        dureeM = sommeRounds/nbGames
                        pourcentageV = nbVictoireJ1/nbGames*100

                        listeWinrate.append(pourcentageV)
                        listeLength.append(dureeM)
                        listeName.append([i, j])

                        print("Pourcentage de victoire du joueur 1 :", pourcentageV, "%")
                        print("La durée moyenne des parties est de", dureeM, "rounds.\n")
                    else:
                        listeWinrate.append(50)
                        listeLength.append(-1)
                        listeName.append([i, j])

                        print("Draw infini !!\n")

    tempsF = time.time()
    tempsS = tempsF - tempsD
    print("La simulation a durée", tempsS, "secondes.\n\n\n")

    stats = []
    stats.append(listeWinrate)
    stats.append(listeLength)
    stats.append(listeName)

    print("Les résultats du tournoi est :\n")

    for i in range(len(choix)):
        for j in range(len(prediction)):
            cpt = 0
            cpt2 = 0
            winrate = 0
            lenght = 0
            for k in range(len(stats[2])):
                if (stats[2][k] == [i, j]):
                    winrate = winrate + stats[0][k]
                    cpt = cpt + 1
                    if (stats[1][k] != -1):
                        lenght = lenght + stats[1][k]
                        cpt2 = cpt2 + 1
            print("Modele :", [i, j])
            print("Winrate :", winrate/cpt)
            if (cpt2 != 0):
                print("Durée :", lenght/cpt2)
            else:
                print("Durée : null")
            print("\n")


if (True):
    [choix, prediction] = loadModele()  # chargement des différents modèles

    nbGames = 100
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3

    tournoiIAvsIA(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)