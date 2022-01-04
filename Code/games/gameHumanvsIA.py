import random
import sys
sys.path.append("./Code/IA")
from play import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                           Humain vs IA                           ###
###                                                                  ###
### ---------------------------------------------------------------- ###

# Pas de commentaire sur de fichier (même fonctionnement que "gameIAvsRandom.py")


def gameHumanvsIA(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    winner = 0
    round = 0
    tab = []

    print("\nLancement de la partie : vous être le joueur n°1 !\n\n")

    while (winner == 0):

        [nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
        tabI = [nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]
        tab.append(tabI)
        
        round = round + 1

        if (nbCaillouxJ1 == 0):
            winner = 1
        elif (nbCaillouxJ2 == 0):
            winner = 2

    return [winner, round, tab]


def manche(round, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    print("Il y a actuellement ", nbCaillouxJ1+nbCaillouxJ2, " cailloux en jeu. (", nbCaillouxJ1, " à ", nbCaillouxJ2, ")")
    
    choixJ1 = int(input("Combien de cailloux mettez vous en jeu : "))
    while (choixJ1 > nbCaillouxJ1 or choixJ1 < 0):
        print("Choix impossible !")
        choixJ1 = int(input("Combien de cailloux mettez vous en jeu : "))
    
    choixJ2 = choixBigBrain(nbCaillouxJ1, nbCaillouxJ2, choix)
    if (choixJ2 < 0 or choixJ2 > nbCaillouxJ2):
        print("L'IA a fait un choix impossible !")
        exit(1)

    nbCaillouxTotaux = choixJ1 + choixJ2
    predictionJ2 = 0
    predictionJ1 = -1

    if (round%2 == 0): 
        
        predictionJ1 = int(input("Quelle est votre prédiction : "))
        while(predictionJ1 > nbCaillouxTotaux or predictionJ1 < 0):
            print("Prediction impossible !")
            predictionJ1 = int(input("Quelle est votre prédiction : "))
            
        predictionJ2 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2, choixJ1, prediction)
        if (predictionJ2 == predictionJ1):
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

    else:
        predictionJ2 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2, -1, prediction)
        print("Votre adversaire à prédit ", int(predictionJ2))
        
        predictionJ1 = int(input("Quelle est votre prédiction : "))
        while(predictionJ1 > nbCaillouxTotaux or predictionJ1 < 0):
            print("Prediction impossible !")
            predictionJ1 = int(input("Quelle est votre prédiction : "))

    if (predictionJ2 == nbCaillouxTotaux):
        nbCaillouxJ2 = nbCaillouxJ2 - 1
        print("\nVotre adversaire a gagné, il pose un cailloux. Il lui reste ", nbCaillouxJ2, " cailloux.")
        print("Vous avez joué : ", choixJ1, "et l'IA à joué : ", int(choixJ2), " soit un nombre total de cailloux de : ", int(nbCaillouxTotaux))
        print("Vous aviez prédit : ", predictionJ1, " tandis que votre adversaire avait prédis : ", int(predictionJ2))
    elif (predictionJ1 == nbCaillouxTotaux):
        nbCaillouxJ1 = nbCaillouxJ1 - 1
        print("\nVous avez gagné, vous posez un cailloux. Il vous reste ", nbCaillouxJ1, " cailloux.")
        print("Vous avez joué : ", choixJ1, "et l'IA à joué : ", int(choixJ2), " soit un nombre total de cailloux de : ", int(nbCaillouxTotaux))
        print("Vous aviez prédit : ", predictionJ1, " tandis que votre adversaire avait prédis : ", int(predictionJ2))
    else:
        print("\nRound nul !")
        print("Vous avez joué : ", choixJ1, "et l'IA à joué : ", int(choixJ2), " soit un nombre total de cailloux de : ", int(nbCaillouxTotaux))
        print("Vous aviez prédit : ", predictionJ1, " tandis que votre adversaire avait prédis : ", int(predictionJ2))   

    print("\n\n")
    return [nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]


if (True):    
    f = open("./modeles/choixSVC.pickle",'r+b')
    fi = open("./modeles/predictionSVC.pickle", 'r+b')
    choix = pickle.load(f)
    prediction = pickle.load(fi)
    
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    
    [winner, round, tab] = gameHumanvsIA(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
    print("\nLe gagnant est le joueur : ", winner, " en ", round, " rounds.")
    print("\nDétails de la partie : ", tab)
    print("\n")