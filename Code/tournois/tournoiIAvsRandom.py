import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsRandomObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                   Tournoi IA vs Random (object)                  ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def tournoiIAvsRandom(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):  

    print("Début de la simulation ..\n")
    tempsD = time.time()

    tabStats = []

    for i in range(len(choix)):     # du modèle (choix) présent de l'indice 0 à 3
        choixModele = choix[i]      # on le sélectionne

        for j in range(len(prediction)):                      # du modèle (prédiction) présent de l'indice 0 à 3 
            predictionModele = prediction[j]    # on le sélectionne

            sommeRounds = 0     # nombre de round total
            nbVictoireIA = 0    # nombre de victoire (j1)

            print("Simulation n°", i, j)    # repère visuel pour savoir quel model est en train de jouer

            for k in range(nbGames):    # pour le nombre de parties choisi
                [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)   # on exécute les parties

                sommeRounds = sommeRounds + round   # incrémentation de la somme des round

                if (winner == 1):                       # test de victoire
                    nbVictoireIA = nbVictoireIA + 1     # incrémentation nombre de victoire

            dureeM = sommeRounds/nbGames                # durée moyenne des manches
            pourcentageV = nbVictoireIA/nbGames*100     # pourcentage de victoire

            tabT = [pourcentageV, dureeM, [i, j]]       # tableau temporaire
            tabStats.append(tabT)                       # ajout du tableau temporaire au tableau des statistiques global

            print("Pourcentage de victoire de", pourcentageV, "%")              # statistiques
            print("La durée moyenne des parties est de", dureeM, "rounds.\n")

    tempsF = time.time()
    tempsS = tempsF - tempsD
    print("La simulation a durée", tempsS, "secondes.\n\n")

    graphWinrate = []
    graphLenght = []
    etalon = list(range(1,(len(choix) * len(prediction) + 1)))
    print("Les résultats du tournoi est :\n")

    for i in range(len(choix)):
        for j in range(len(prediction)):
            winrateT = 0
            lenghtT = 0
            for k in range((len(choix) * len(prediction))):
                if (tabStats[k][2] == [i, j]):
                    winrateT = tabStats[k][0]
                    lenghtT = tabStats[k][1]

            print("Modele :", [i, j])
            print("Winrate :", winrateT) 
            print("Durée :", lenghtT)
            print("\n")

            graphWinrate.append(winrateT)
            graphLenght.append(lenghtT)

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
    [choix, prediction] = loadModele("std")      # chargement des différents modèles

    nbGames = 1000      # nombre de partie par "manche de test"
    nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2

    tournoiIAvsRandom(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
