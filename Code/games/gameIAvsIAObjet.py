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

    winner = 0
    round = 0

    ia1 = AIplayer(choix1, prediction1, nbCaillouxJ1)
    ia2 = AIplayer(choix2, prediction2, nbCaillouxJ2)

    while (winner == 0):
        [ia1, ia2] = manche(round, ia1, ia2)

        round = round + 1
        
        if (ia1.cailloux <= 0):
            winner = 1
        elif (ia2.cailloux <= 0):
            winner = 2

        if (round >= 50):
            del ia1, ia2
            return [-1, -1]

    del ia1, ia2
    return [winner, round]


def manche(round, ia1, ia2):

    winnerRound = 0

    ia1.choisir(ia2.cailloux)
    ia2.choisir(ia1.cailloux)

    if (round%2 == 0):
        ia1.predire(ia2.cailloux)
        ia1.clipPred(ia2.cailloux)

        ia2.predire(ia1.cailloux, ia1.prediction)
        ia2.clipPred(ia1.cailloux)

        while (ia1.prediction == ia2.prediction):
            ia2.prediction = random.randint(0, (ia1.cailloux + ia2.cailloux))

    else:
        ia2.predire(ia1.cailloux)
        ia2.clipPred(ia1.cailloux)

        ia1.predire(ia2.cailloux, ia2.prediction)
        ia1.clipPred(ia2.cailloux)

        while (ia1.prediction == ia2.prediction):
            ia1.prediction = random.randint(0, (ia1.cailloux + ia2.cailloux))


    if (ia1.prediction == (ia1.choixCailloux + ia2.choixCailloux)):
        ia1.cailloux = ia1.cailloux - 1
        winnerRound = 1
    elif (ia2.prediction == (ia1.choixCailloux + ia2.choixCailloux)):
        ia2.cailloux = ia2.cailloux - 1
        winnerRound = 2

    return [ia1, ia2]