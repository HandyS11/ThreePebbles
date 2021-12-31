import random


### ---------------------------------------------------------------- ###
###                                                                  ###
###              Version du jeu la plus basique qui soit             ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def gameRandomvsRandom(option, nbCaillouxJ1, nbCaillouxJ2):

    winner = 0          # gagnant de la partie
    winnerRound = 0     # gagnant du round courrant
    round = 0
    tab = []

    while (winner == 0):    # boucle generale de jeu

        [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2] = manche(round, nbCaillouxJ1, nbCaillouxJ2)     # lancement d'une manche et recuperation des valeurs jouees
        tabI = []
        
        if (option == 1):
            tabI = [winnerRound, nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]              # ajout des valeurs de la manche dans un tableau temporaire
        elif (option == 2):
            if (winnerRound == 1):
                tabI = [predictionJ1, predictionJ2, nbCaillouxJ1, nbCaillouxJ2, choixJ1]                       # ajout des valeurs de la manche dans un tableau temporaire 
            else:
                tabI = [predictionJ1, predictionJ2, nbCaillouxJ1, nbCaillouxJ2, choixJ2]                       # ajout des valeurs de la manche dans un tableau temporaire 
        else:
            print("Option de jeu incorecte ! ", option)     # securite
            exit(1)
          
        tab.append(tabI)        # ajout du tableau temporaire (ligne) dans le tableau des logs
        
        round = round + 1       # incrementation du nombre de round

        if (nbCaillouxJ1 == 0):     # tests d'arret
            winner = 1
        elif (nbCaillouxJ2 == 0):
            winner = 2

    return [winner, round, tab]     # retour des valeurs permettant de decrire la partie



def manche(round, nbCaillouxJ1, nbCaillouxJ2):

    winnerRound = 0     # reinitialisation de la valeur (securite)
    
    choixJ1 = random.randint(0,nbCaillouxJ1)    # tirage du nombre de cailloux choisi par le joueur 1
    choixJ2 = random.randint(0,nbCaillouxJ2)    # tirage du nombre de cailloux choisi par le joueur 2

    nbCaillouxTotaux = choixJ1 + choixJ2        # calcule de la somme des cailloux choisi par les 2 joueurs (optimisation)

    predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))      # definition de la prediction du joueur 1
    predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))      # definition de la prediction du joueur 2


    if (round%2 == 0):       # round pair 
               
        while (predictionJ1 == predictionJ2):                                   # les predictions ne doivent pas etre egales (mais on les a defini plus tot pour gagner du temps)
            predictionJ2 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))      # generation d'une prediction possible (suivant les regles du jeu)

        if (predictionJ1 == nbCaillouxTotaux):      # si le joueur 1 devine le nombre de cailloux joues
            nbCaillouxJ1 = nbCaillouxJ1 - 1         # celui-ci pose un cailloux
            winnerRound = 1                         # et gagne le round
            
        elif (predictionJ2 == nbCaillouxTotaux):    # si le joueur 2 devine le nombre de cailloux joues
            nbCaillouxJ2 = nbCaillouxJ2 - 1         # celui-ci pose un cailloux
            winnerRound = 2                         # et gagne le round

    else:       # round impair                      #Procedure similaire au round pair
        
        while (predictionJ1 == predictionJ2):
            predictionJ1 = random.randint(0,(nbCaillouxJ1 + nbCaillouxJ2))

        if (predictionJ2 == nbCaillouxTotaux):
            nbCaillouxJ2 = nbCaillouxJ2 - 1
            winnerRound = 2
        elif (predictionJ1 == nbCaillouxTotaux):
            nbCaillouxJ1 = nbCaillouxJ1 - 1
            winnerRound = 1

    return [winnerRound ,nbCaillouxJ1, nbCaillouxJ2, choixJ1, choixJ2, predictionJ1, predictionJ2]



if (False):     # Test unitaire   
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    option = 1
    [winner, round, tab] = gameRandomvsRandom(option, nbCaillouxJ1, nbCaillouxJ2)
    print("Le gagnant est le joueur ", winner, " en ", round, "rounds.")
    print("Logs de la partie :\n", tab)