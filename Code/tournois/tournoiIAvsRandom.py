import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsRandomObjet import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                   Tournoi IA vs Random (object)                  ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def tournoiIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):  

    print("Début de la simulation ..\n")
    tempsD = time.time()

    for i in range(4):              # du modèle (choix) présent de l'indice 0 à 3
        choixModele = choix[i]      # on le sélectionne

        for j in range(4):                      # du modèle (prédiction) présent de l'indice 0 à 3 
            predictionModele = prediction[j]    # on le sélectionne

            sommeRounds = 0     # nombre de round total
            nbVictoireIA = 0    # nombre de victoire (j1)

            print("Simulation n°", i, j)    # repère visuel pour savoir quel model est en train de jouer

            for k in range(nbGames):    # pour le nombre de parties choisi
                [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)   # on exécute les parties

                sommeRounds = sommeRounds + round   # incrémentation de la somme des round

                if (winner == 1):       # test d'arrêt
                    nbVictoireIA = nbVictoireIA + 1     # incrémentation nombre de victoire

            dureeM = sommeRounds/nbGames
            pourcentageV = nbVictoireIA/nbGames*100

            print("Pourcentage de victoire de", pourcentageV, "%")              # statistiques
            print("La durée moyenne des parties est de", dureeM, "rounds.\n")

    tempsF = time.time()
    tempsS = tempsF - tempsD
    print("La simulation a durée", tempsS, "secondes.\n")


if (True):
    [choix, prediction] = loadModele()      # chargement des différents modèles

    nbGames = 1000      # nombre de partie par "manche de test"
    nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2

    tournoiIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)