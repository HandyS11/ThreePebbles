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

    tabStats = []

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

                        tabT = [pourcentageV, dureeM, [i, j]]
                        tabStats.append(tabT)

                        print("Pourcentage de victoire du joueur 1 :", pourcentageV, "%")
                        print("La durée moyenne des parties est de", dureeM, "rounds.\n")
                    else:
                        tabT = [50, -1, [i, j]]
                        tabStats.append(tabT)

                        print("Draw infini !!\n")
                    
    tempsF = time.time()
    tempsS = tempsF - tempsD
    print("La simulation a durée", tempsS, "secondes.\n\n\n")

    graphWinrate = []
    graphLenght = []
    etalon = list(range(1,(len(choix) * len(prediction) +1)))
    print("Les résultats du tournoi sont :\n")

    for i in range(len(choix)):
        for j in range(len(prediction)):
            winrateT = []
            lenghtT = []
            for k in range((len(choix) * len(prediction))**2):
                if (tabStats[k][2] == [i, j]):
                    winrateT.append(tabStats[k][0])
                    if (tabStats[k][1] != -1):
                        lenghtT.append(tabStats[k][1])

            print("Modele :", [i, j])

            if (len(winrateT) != 0):
                winrateG = sum(winrateT)/len(winrateT)
            else:
                winrateG = 0
            print("Winrate :", winrateG) 

            if (len(lenghtT) != 0):
                lenghtG = sum(lenghtT)/len(lenghtT)
            else:
                lenghtG = 0
            print("Durée :", lenghtG)
            print("\n")

            graphWinrate.append(winrateG)
            graphLenght.append(lenghtG)

    plt.bar(etalon, graphWinrate, align = 'center')
    plt.title('Taux de victoire par combinaison de modèle')
    plt.ylabel('Taux de victoire `%`')
    plt.xlabel('Numéro de la combinaison de modèle')
    plt.show()

    plt.bar(etalon, graphLenght, align = 'center')
    plt.title('Durée moyenne des parties par combinaison de modèle')
    plt.ylabel('Durée des parties`')
    plt.xlabel('Numéro de la combinaison de modèle')
    plt.show()


if (True):
    [choix, prediction] = loadModele("std")  # chargement des différents modèles

    nbGames = 100
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3

    tournoiIAvsIA(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
