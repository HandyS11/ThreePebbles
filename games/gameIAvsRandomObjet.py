import random
import sys
from objects.player import AIplayer, randPlayer
sys.path.append("./IA")
from play import *


def gameIAvsRandom(model):

    winner = 0
    winnerRound = 0
    predictionJ1 = 0;
    round = 0
    tab = []
    IA = AIplayer(model);
    rando = randPlayer();

    while (winner == 0):

        [winnerRound] = manche(round, rando, IA)
        tabI = [winnerRound, IA.cailloux, rando.cailloux, IA.choixCailloux, rando.choixCailloux, IA.prediction, rando.prediction]
        tab.append(tabI)
        
        round += 1

        if (IA.cailloux == 0):
            winner = 1
        elif (rando.cailloux == 0):
            winner = 2

    return [winner, round, tab]


def manche(round, rando, IA):

    winnerRound = 0
    
    nbCaillouxParie = IA.choisir(rando.cailloux) + rando.choisir()

    predictionJ2 = rando.predire(IA.cailloux);
    predictionJ1 = 0;

    if (round%2 == 0):
        predictionJ1 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, -1, choixJ1, prediction)
        if (predictionJ1 > (nbCaillouxJ1+nbCaillouxJ2)):
            predictionJ1 = (nbCaillouxJ1+nbCaillouxJ2)
            
        while (predictionJ1 == predictionJ2):
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ1 == nbCaillouxParie):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 1
        elif (predictionJ2 == nbCaillouxParie):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 2

    else:
        predictionJ1 = predictionJ2
        predictionJ1 = predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2, choixJ1, prediction)
        if (predictionJ1 > (nbCaillouxJ1+nbCaillouxJ2)):
            predictionJ1 = (nbCaillouxJ1+nbCaillouxJ2)
            
        if (predictionJ2 == nbCaillouxParie):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 2
        elif (predictionJ1 == nbCaillouxParie):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 1

    return [winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]


if (False):
    [winner, round, tab] = gameIAvsRandom(3, 3)