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



def tournoiIAvsRandom(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):  

    print("Début de la simulation ..\n")
    tempsD = time.time()    # temps exact avant la simulation

    tabStats = []       # tableau de statistique sur les parties

    for i in range(len(choix)):     # du modèle (choix) présent de l'indice (0 à 2 dans notre cas)
        choixModele = choix[i]      # on le sélectionne

        for j in range(len(prediction)):        # du modèle (prédiction) présent de l'indice (0 à 2 dans notre cas)
            predictionModele = prediction[j]    # on le sélectionne

            sommeRounds = 0     # nombre de manches totales
            nbVictoireIA = 0    # nombre de victoires (j1)

            print("Simulation n°", i, j)    # repère visuel pour savoir quel model est en train de jouer

            for k in range(nbGames):    # pour le nombre de parties choisi
                [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)   # on exécute les parties

                sommeRounds = sommeRounds + round   # incrémentation de la somme des round

                if (winner == 1):                       # test de victoire
                    nbVictoireIA = nbVictoireIA + 1     # incrémentation nombre de victoire

            dureeM = sommeRounds/nbGames                # durée moyenne des manches
            pourcentageV = nbVictoireIA/nbGames*100     # pourcentage de victoire

            tabT = [pourcentageV, dureeM, [i, j]]       # tableau temporaire
            tabStats.append(tabT)                       # ajout du tableau temporaire au tableau des statistiques global

            print("Pourcentage de victoire de", pourcentageV, "%")              # statistiques
            print("La durée moyenne des parties est de", dureeM, "rounds.\n")

    tempsF = time.time()        # temps exact à la fin de la simulation
    tempsS = tempsF - tempsD    # calcul de la durée de la simulation
    print("La simulation a durée", tempsS, "secondes.\n\n")

    graphWinrate = []       # tableau de données sur le % de victoire
    graphLenght = []        # tableau de données sur la durrée des manches
    etalon = list(range(1,(len(choix) * len(prediction) + 1)))      # représente un numéro de modèle (1 à n modèle)
    print("Les résultats du tournoi est :\n")

    for i in range(len(choix)):             # pour tous les modèles choix
        for j in range(len(prediction)):    # pour tous les modèles prédiction
            for k in range((len(choix) * len(prediction))):     # pour toutes les données du tableau de statistique
                if (tabStats[k][2] == [i, j]):      # si la donnée correspond à la bonne combinaison de modèles (inutile car le tableau est trié mais fonctionnerait si il ne l'était pas)

                    print("Modele :", [i, j])
                    print("Winrate :", tabStats[k][0]) 
                    print("Durée :", tabStats[k][1])
                    print("\n")

                    graphWinrate.append(tabStats[k][0])     # ajout de la valeur pour ce modèle au tableau de stats pour le graph
                    graphLenght.append(tabStats[k][1])

    plt.bar(etalon, graphWinrate, align = 'center')             # création des graphs
    plt.title('Taux de victoire par combinaison de modèle')
    plt.ylabel('Taux de victoire `%`')
    plt.xlabel('Numéro de la combinaison de modèle')
    plt.show()

    plt.bar(etalon, graphLenght, align = 'center')
    plt.title('Durée moyenne des parties par combinaison de modèle')
    plt.ylabel('Durée des parties`')
    plt.xlabel('Numéro de la combinaison de modèle')
    plt.show()


if (True):
    [choix, prediction] = loadModele("std")      # chargement des différents modèles

    nbGames = 1000      # nombre de partie jouées pour chaque combinaison de modèle
    nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2

    tournoiIAvsRandom(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)   # lancement du tournoi
