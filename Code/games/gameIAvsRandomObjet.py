import random
import sys
from types import new_class
sys.path.append("./Code/objects")
from player import AIplayer, randPlayer
sys.path.append("./Code/IA")
from play import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                        IA vs Random (objet)                      ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    winner = 0          # gagnant de la partie      (0 = en cours | 1 = joueur 1 | 2 = joueur 2)
    winnerRound = 0     # gagnant de la manche      (0 = en cours | 1 = joueur 1 | 2 = joueur 2)
    round = 0           # compteur du nombre de manches
    tab = []            # tableau des logs de partie

    ia = AIplayer(choix,prediction,nbCaillouxJ1)    # initialisation du joueur 1 (IA)
    rando = randPlayer(nbCaillouxJ2)                # initialisation du joueur 2 (Random)

    while (winner == 0):
        [winnerRound, ia, rando] = mancheObj(round, ia, rando)      # lancement d'une manche
        tabI = [winnerRound, ia.cailloux, rando.cailloux, ia.choixCailloux, rando.choixCailloux, ia.prediction, rando.prediction]       # récupération des données temporairement
        tab.append(tabI)    # ajout des données temporaires au tableau de log global
        round += 1          # incrémentation du nombre de manches

        if (ia.cailloux <= 0):      # tests d'arrêt (victoire)
            winner = 1
        elif (rando.cailloux <= 0):
            winner = 2

    del ia
    del rando
    return [winner, round, tab]


def mancheObj(round, ia, rando):

    winnerRound = 0                 # sécurité (remise à 0)

    ia.choisir(rando.cailloux)      # le joueur 1 choisit combien de cailloux jouer
    rando.choisir()                 # le joueur 2 choisit combien de cailloux jouer

    rando.predire(ia.cailloux)      # le joueur 2 prédit le nombre total de cailloux joués (optimisation)

    if (round%2 == 0):                  # si la manche est impair (retard de 1 par rapport au compteur réel)
        ia.predire(rando.prediction)    # le joueur 1 prédit le nombre total de cailloux joués
        ia.clipPred(rando.cailloux)     # sécurité (vérification de la validité de la prédiction) -> si impossible : d'abord maximale puis aléatoire

        while (ia.prediction == rando.prediction):  # test de sécurité
            rando.predire(ia.cailloux)              # attribution d'une valeur aléatoire  

    else:                           # même principe mais en inversant les joueurs
        ia.predire(rando.cailloux)
        ia.clipPred(rando.cailloux)

        while (ia.prediction == rando.prediction):
            ia.prediction = random.randint(0,(ia.cailloux + rando.cailloux))
            
            
    if (rando.prediction == (rando.choixCailloux + ia.choixCailloux)):      # tests d'arrêt (victoire)
        rando.cailloux = rando.cailloux - 1
        winnerRound = 2
    elif (ia.prediction == (rando.choixCailloux + ia.choixCailloux)):
        ia.cailloux = ia.cailloux - 1
        winnerRound = 1

    return [winnerRound, ia, rando]