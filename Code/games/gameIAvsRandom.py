import random
import sys
sys.path.append("./Code/IA")
from play import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###         Version de test de l'IA (contre un joueur random)        ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def gameIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):      # L'IA est toujours le joueur 1

    winner = 0          # gagnant de la partie      (0 = en cours | 1 = joueur 1 | 2 = joueur 2)
    winnerRound = 0     # gagnant du round actif    (0 = en cours | 1 = joueur 1 | 2 = joueur 2)   
    round = 0           # compteur du nombre de rounds
    tab = []            # tableau des logs de partie

    while (winner == 0):

        [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)      # lancement du round
        tabI = [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]  # récuparation des logs du round
        tab.append(tabI)       # ajout des logs du round dnas le tableau de log général
        
        round = round + 1   # incrémentation du nombre de round

        if (nbCaillouxJ1 == 0):     # test d'arrêt
            winner = 1
        elif (nbCaillouxJ2 == 0):
            winner = 2

    return [winner, round, tab]     # retour des valeurs permettant de décrire la partie


def manche(round, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    winnerRound = 0     # sécurité (remise à 0)
    
    choixJ1 = choixBigBrain(nbCaillouxJ1, nbCaillouxJ2, choix)  # l'IA choisi combien de cailloux elle veut jouer
    if (choixJ1 > nbCaillouxJ1):        # sécurité
        print("L'IA a fait un choix impossible !")
        print("IA :", choixJ1, "MAX :", nbCaillouxJ1)
        choixJ1 = nbCaillouxJ1          # attribution de la valeur maximale pour ne pas arrêter le programme
        
    choixJ2 = random.randint(0,nbCaillouxJ2)    # le joueur aléatoire choisi combien de cailloux il joue

    nbCaillouxTotaux = choixJ1 + choixJ2        # somme des cailloux sur le plateau

    predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))  # attribution d'une valeur temporaire pour optimiser le futur choix (si )
    predictionJ1 = 0    # sécurité (va être modifier dans le if/else qui suit)

    if (round%2 == 0):  #si le round est pair
        predictionJ1 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, -1, choixJ1, prediction)  # l'IA prédit le nombre total de cailloux sur le plateau
        if (predictionJ1 > (nbCaillouxJ1+nbCaillouxJ2)):        # sécurité      
            print("L'IA a fait une prédiction impossible !")
            print("IA :", predictionJ1, "MAX :", (nbCaillouxJ1+nbCaillouxJ2))
            predictionJ1 = (nbCaillouxJ1+nbCaillouxJ2)      # attribution de la valeur maximale pour ne pas arrêter le programme
            
        while (predictionJ1 == predictionJ2):       # tant que la prédiction du J1 = celle du j2
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))  # on essaye une nouvelle valeur pour le J2       

    else:       # si le round est impair
        predictionJ1 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2, choixJ1, prediction)
        if (predictionJ1 > (nbCaillouxJ1+nbCaillouxJ2)):        # sécurité      
            print("L'IA a fait une prédiction impossible !")
            print("IA :", predictionJ1, "MAX :", (nbCaillouxJ1+nbCaillouxJ2))
            predictionJ1 = (nbCaillouxJ1+nbCaillouxJ2)      # attribution de la valeur maximale pour ne pas arrêter le programme

        while (predictionJ1 == predictionJ2):               # tant que la prédiction du J1 = celle du j2
            predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))  # on essaye une nouvelle valeur pour le J1

    if (predictionJ1 == nbCaillouxTotaux):      # tests de victoire
        nbCaillouxJ1 = nbCaillouxJ1 - 1
        winnerRound = 1
    elif (predictionJ2 == nbCaillouxTotaux):
        nbCaillouxJ2 = nbCaillouxJ2 - 1
        winnerRound = 2

    return [winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]