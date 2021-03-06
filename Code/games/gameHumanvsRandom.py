import random


### ---------------------------------------------------------------- ###
###                                                                  ###
###                          Humain vs Random                        ###
###                                                                  ###
### ---------------------------------------------------------------- ###

# Pas de commentaire sur de fichier (même fonctionnement que "gameIAvsRandom.py")


def gameWithHuman():

    winner = 0
    round = 0
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    tab = []

    print("\nLancement de la partie : vous être le joueur n°1 !\n\n")

    while (winner == 0):

        [nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2)
        tabI = [nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]
        tab.append(tabI)
        
        round = round + 1

        if (nbCaillouxJ1 == 0):
            winner = 1
        elif (nbCaillouxJ2 == 0):
            winner = 2

    return [winner, round, tab]


def manche(round, nbCaillouxJ1, nbCaillouxJ2):

    print("Il y a actuellement ", nbCaillouxJ1+nbCaillouxJ2, " cailloux en jeu. (", nbCaillouxJ1, " à ", nbCaillouxJ2, ")")
    choixJ1 = int(input("Combien de cailloux mettez vous en jeu : "))
    choixJ2 = random.randint(0,nbCaillouxJ2)

    nbCaillouxTotaux = choixJ1 + choixJ2
    predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

    if (round%2 == 0): 
        predictionJ1 = int(input("Quelle est votre prédiction : "))  
        while (predictionJ1 == predictionJ2):
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

    else:
        print("Votre adversaire à prédit ", predictionJ2)
        predictionJ1 = int(input("Quelle est votre prédiction : ")) 
        while (predictionJ1 == predictionJ2):  
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
    [winner, round, tab] = gameWithHuman()
    print("\nLe gagnant est le joueur : ", winner, " en ", round, " rounds.")
    print("\nDétails de la partie : ", tab)
    print("\n")