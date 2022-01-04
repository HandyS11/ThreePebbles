import random
import sys
from types import new_class
sys.path.append("./Code/objects")
from player import AIplayer
sys.path.append("./Code/IA")
from play import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                          IA vs IA (objet)                        ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def gameIAvsIAObjet(nbCaillouxJ1, nbCaillouxJ2, choix1, prediction1, choix2, prediction2):

    winner = 0      # gagnant de la partie      (0 = en cours | 1 = joueur 1 | 2 = joueur 2)
    round = 0       # compteur du nombre de manches

    ia1 = AIplayer(choix1, prediction1, nbCaillouxJ1)       # initialisation du joueur 1
    ia2 = AIplayer(choix2, prediction2, nbCaillouxJ2)       # initialisation du joueur 2

    while (winner == 0):
        [ia1, ia2] = manche(round, ia1, ia2)    # lancement de la manche
        round = round + 1                       # incrémentation du nombre de manches
        
        if (ia1.cailloux <= 0):         # test d'arrêt (de victoire)
            winner = 1
        elif (ia2.cailloux <= 0):
            winner = 2

        if (round >= 50):               # test de sécurité (partie infinie)
            del ia1, ia2
            return [-1, -1]

    del ia1, ia2
    return [winner, round]


def manche(round, ia1, ia2):

    winnerRound = 0     # réinisialisation par sécurité

    ia1.choisir(ia2.cailloux)       # le joueur 1 choisit combien de cailloux il veut joueur
    ia2.choisir(ia1.cailloux)       # le joueur 2 choisit combien de cailloux il veut joueur

    if (round%2 == 0):              # pour les manches impaires (le comteur est toujours en retard de 1)
        ia1.predire(ia2.cailloux)   # le joueur 1 predit le nombre de cailloux total joués
        ia1.clipPred(ia2.cailloux)  # sécurité (vérification de la validité de la prédiction) -> si impossible : d'abord maximale puis aléatoire

        ia2.predire(ia1.cailloux, ia1.prediction)       # le joueur 2 predit le nombre de cailloux total joués (il a l'information de la prédiction du joueur 1)
        ia2.clipPred(ia1.cailloux)                      # sécurité (vérification de la validité de la prédiction) -> si impossible : maximale

        while (ia1.prediction == ia2.prediction):                               # test de sécurité
            ia2.prediction = random.randint(0, (ia1.cailloux + ia2.cailloux))   # attribution d'une valeur aléatoire

    else:                           # même déroulé mais en inversant les joueurs
        ia2.predire(ia1.cailloux)       
        ia2.clipPred(ia1.cailloux)

        ia1.predire(ia2.cailloux, ia2.prediction)
        ia1.clipPred(ia2.cailloux)

        while (ia1.prediction == ia2.prediction):
            ia1.prediction = random.randint(0, (ia1.cailloux + ia2.cailloux))


    if (ia1.prediction == (ia1.choixCailloux + ia2.choixCailloux)):     # test d'arrêt (victoire)
        ia1.cailloux = ia1.cailloux - 1
        winnerRound = 1
    elif (ia2.prediction == (ia1.choixCailloux + ia2.choixCailloux)):
        ia2.cailloux = ia2.cailloux - 1
        winnerRound = 2

    return [ia1, ia2]