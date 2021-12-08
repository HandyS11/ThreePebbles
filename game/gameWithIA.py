import random


def gameWithIA(joueurQuiCommence, nbCaillouxJ1, nbCaillouxJ2):

    winner = 0
    winnerRound = 0
    round = 0
    tab = []

    while (winner == 0):

        [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2)
        #if (joueurQuiCommence == 1):
        #    [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2)
        #else:
        #    [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche2(round, nbCaillouxJ1, nbCaillouxJ2)
        
        
        if (winnerRound == 1):
            if (round%2 == 0):     
                tabI = [winnerRound, predictionJ1, -1, nbCaillouxJ1, nbCaillouxJ2]
            else:
                tabI = [winnerRound, predictionJ1, predictionJ2, nbCaillouxJ1, nbCaillouxJ2]
            tab.append(tabI)
            
        #elif (winnerRound == 2):
        #    if (round%2 == 0):     
        #        tabI = [winnerRound, predictionJ1, predictionJ2, nbCaillouxJ1, nbCaillouxJ2]
        #    else:
        #        tabI = [winnerRound, predictionJ1, -1, nbCaillouxJ1, nbCaillouxJ2]
        #    tab.append(tabI)
        
        
        round = round + 1

        if (nbCaillouxJ1 == 0):
            winner = 1
        elif (nbCaillouxJ2 == 0):
            winner = 2

    return [winner, round, tab]


def manche(round, nbCaillouxJ1, nbCaillouxJ2):

    winnerRound = 0
    
    choixJ1 = random.randint(0,nbCaillouxJ1)
    choixJ2 = random.randint(0,nbCaillouxJ2)

    nbCaillouxTotaux = choixJ1 + choixJ2

    predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))
    predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

    if (round%2 == 0):       
        while (predictionJ1 == predictionJ2):
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ1 == nbCaillouxTotaux):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 1
        elif (predictionJ2 == nbCaillouxTotaux):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 2

    else:
        while (predictionJ1 == predictionJ2):
            predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ2 == nbCaillouxTotaux):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 2
        elif (predictionJ1 == nbCaillouxTotaux):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 1

    #print(winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2)
    return [winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]





def manche2(round, nbCaillouxJ1, nbCaillouxJ2):
    
    winnerRound = 0
    
    choixJ1 = random.randint(0,nbCaillouxJ1)
    choixJ2 = random.randint(0,nbCaillouxJ2)

    nbCaillouxTotaux = choixJ1 + choixJ2

    predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))
    predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

    if (round%2 == 0):             
        while (predictionJ1 == predictionJ2):
            predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ2 == nbCaillouxTotaux):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 1
        elif (predictionJ1 == nbCaillouxTotaux):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 2

    else:
        while (predictionJ1 == predictionJ2):
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ1 == nbCaillouxTotaux):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 2
        elif (predictionJ2 == nbCaillouxTotaux):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 1   

    return [winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]



if (False):
    [winner, round, tab] = gameWithIA(1, 3, 3)