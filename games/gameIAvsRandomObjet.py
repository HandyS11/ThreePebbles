import random
import sys
from types import new_class
sys.path.append("./objects")
from player import AIplayer, randPlayer
sys.path.append("./IA")
from play import *


def gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    winner = 0
    winnerRound = 0
    round = 0
    tab = []
    ia = AIplayer(choix,prediction,nbCaillouxJ1)
    rando = randPlayer(nbCaillouxJ2)

    while (winner == 0):
        [winnerRound, ia, rando] = mancheObj(round, rando, ia)
        tabI = [winnerRound, ia.cailloux, rando.cailloux, ia.choixCailloux, rando.choixCailloux, ia.prediction, rando.prediction]
        tab.append(tabI)
        round += 1

        if (ia.cailloux <= 0):
            winner = 1
        elif (rando.cailloux <= 0):
            winner = 2

    del ia
    del rando
    return [winner, round, tab]


def mancheObj(round, rando, ia):   #rando = J2
    winnerRound = 0

    ia.choisir(rando.cailloux)

    rando.choisir()
    rando.predire(ia.cailloux)
    

    if (round%2 == 0):
        ia.predire(rando.prediction)
        ia.clipPred(rando.cailloux)

        while (ia.prediction == rando.prediction):  #on empêche les situations où on ne peut pas décider du vainqueur
            rando.predire(ia.cailloux)

    else:
        ia.predire(rando.cailloux)
        ia.clipPred(rando.cailloux) #limite la prédiction aux maximum

        while (ia.prediction == rando.prediction):
            ia.prediction = random.randint(0,(ia.cailloux + rando.cailloux))
            
            
    if (rando.prediction == (rando.choixCailloux + ia.choixCailloux)):
        rando.cailloux = rando.cailloux - 1
        winnerRound = 2
    elif (ia.prediction == (rando.choixCailloux + ia.choixCailloux)):
        ia.cailloux = ia.cailloux - 1
        winnerRound = 1

    return [winnerRound, ia, rando]