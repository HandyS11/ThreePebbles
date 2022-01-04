import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsRandomObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                   Tournoi IA vs Random (object)                  ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def tournoiIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction):  

    print("Début de la simulation ..\n")
    tempsD = time.time()

    listeWinrate = []
    listeLength = []
    listeName = []

    for i in range(len(choix)):     # du modèle (choix) présent de l'indice 0 à 3
        choixModele = choix[i]      # on le sélectionne

        for j in range(len(prediction)):                      # du modèle (prédiction) présent de l'indice 0 à 3 
            predictionModele = prediction[j]    # on le sélectionne

            sommeRounds = 0     # nombre de round total
            nbVictoireIA = 0    # nombre de victoire (j1)

            print("Simulation n°", i, j)    # repère visuel pour savoir quel model est en train de jouer

            for k in range(nbGames):    # pour le nombre de parties choisi
                [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)   # on exécute les parties

                sommeRounds = sommeRounds + round   # incrémentation de la somme des round

                if (winner == 1):       # test d'arrêt
                    nbVictoireIA = nbVictoireIA + 1     # incrémentation nombre de victoire

            dureeM = sommeRounds/nbGames
            pourcentageV = nbVictoireIA/nbGames*100

            listeWinrate.append(pourcentageV)
            listeLength.append(dureeM)
            listeName.append([i, j])

            print("Pourcentage de victoire de", pourcentageV, "%")              # statistiques
            print("La durée moyenne des parties est de", dureeM, "rounds.\n")

    tempsF = time.time()
    tempsS = tempsF - tempsD
    print("La simulation a durée", tempsS, "secondes.\n\n")

    stats = []
    stats.append(listeWinrate)
    stats.append(listeLength)
    stats.append(listeName)

    print("Les résultats du tournoi est :\n")

    for i in range(len(choix)):
        for j in range(len(prediction)):
            cpt = 0
            cpt2 = 0
            winrate = 0
            lenght = 0
            for k in range(len(stats[2])):
                if (stats[2][k] == [i, j]):
                    winrate = winrate + stats[0][k]
                    cpt = cpt + 1
                    if (stats[1][k] != -1):
                        lenght = lenght + stats[1][k]
                        cpt2 = cpt2 + 1
            print("Modele :", [i, j])
            print("Winrate :", winrate/cpt)
            if (cpt2 != 0):
                print("Durée :", lenght/cpt2)
            else:
                print("Durée : null")
            print("\n")


if (True):
    [choix, prediction] = loadModele("std")      # chargement des différents modèles

    nbGames = 100       # nombre de partie par "manche de test"
    nbCaillouxJ1 = 5    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 5    # nombre de cailloux du joueur 2

    tournoiIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
