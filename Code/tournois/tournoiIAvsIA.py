import sys
from loader import *
sys.path.append("./Code/main")
from modules import *
sys.path.append("./Code/games")
from gameIAvsIAObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                     Tournoi IA vs IA (object)                    ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def tournoiIAvsIA(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction):

    print("Début de la simulation ..\n")
    tempsD = time.time()    # temps exact avant la simulation

    tabStats = []       # tableau de statistique sur les parties

    for i in range(len(choix)):         # du modèle (choix) présent de l'indice (0 à 2 dans notre cas)
        choixModeleJ1 = choix[i]        # on le sélectionne

        for j in range(len(prediction)):            # du modèle (prédiction) présent de l'indice (0 à 2 dans notre cas)
            predictionModeleJ1 = prediction[j]      # on le sélectionne

            for k in range(len(choix)):         # du modèle (choix) présent de l'indice (0 à 2 dans notre cas)
                choixModeleJ2 = choix[k]        # on le sélectionne

                for l in range(len(prediction)):            # du modèle (prédiction) présent de l'indice (0 à 2 dans notre cas)
                    predictionModeleJ2 = prediction[l]      # on le sélectionne

                    sommeRounds = 0         # nombre de manches totales
                    nbVictoireJ1 = 0        # nombre de victoires (j1)

                    print("Simulation n°", i, j, k, l)      # chaque variable correspond au numéro du modèle utilisé (i = choix pour J1, j = prédiction pour J1 ..)

                    for m in range(nbGames):    # pour le nombre de parties choisi
                        [winner, round] = gameIAvsIAObjet(nbCaillouxJ1, nbCaillouxJ2, choixModeleJ1, predictionModeleJ1, choixModeleJ2, predictionModeleJ2)     # lancement de la partie

                        if (round == -1):   # si la valeur du nombre de manches retourné vaut -1
                            break           # on arrête la simulation des ces modèles (partie infinie détectée)

                        if (winner == 1):           # test de victoire du joueur 1
                            nbVictoireJ1 = nbVictoireJ1 + 1

                        sommeRounds = sommeRounds + round   # incrémentation du nombre de manches totales

                    if (round != -1):       # si la dernière valeur du nombre de manches retourné ne vaut pas vaut -1
                        dureeM = sommeRounds/nbGames                # calcul de la durée moyenne des manches
                        pourcentageV = nbVictoireJ1/nbGames*100     # calcul du pourcentage de victoire

                        tabT = [pourcentageV, dureeM, [i, j]]       # ajout des données à un tableau temporaire
                        tabStats.append(tabT)                       # ajout des données au tableau de statistiques global

                        print("Pourcentage de victoire du joueur 1 :", pourcentageV, "%")
                        print("La durée moyenne des parties est de", dureeM, "rounds.\n")
                    else:                   # sinon
                        tabT = [50, -1, [i, j]]     # ajout de valeurs spéciales (pour détecter le problème rencontré lors de la simulation)
                        tabStats.append(tabT)

                        print("Draw infini !!\n")
                    
    tempsF = time.time()        # temps exact à la fin de la simulation
    tempsS = tempsF - tempsD    # calcul de la durée de la simulation
    print("La simulation a durée", tempsS, "secondes.\n\n\n")

    graphWinrate = []       # tableau de données sur le % de victoire
    graphLenght = []        # tableau de données sur la durrée des manches
    etalon = list(range(1,(len(choix) * len(prediction) +1)))   # représente un numéro de modèle (1 à n modèle)
    print("Les résultats du tournoi sont :\n")

    for i in range(len(choix)):             # pour tous les modèles choix
        for j in range(len(prediction)):    # pour tous les modèles prédiction
            winrateT = []       # tableau temporaire des pourcentages de victoire
            lenghtT = []        # tableau temporaire des durées
            for k in range((len(choix) * len(prediction))**2):      # pour toutes les données du tableau de statistique
                if (tabStats[k][2] == [i, j]):          # si la donnée correspond à la bonne combinaison de modèles (peut être optimisé dans un tableau trié mais a l'avantgae de marcher partout)
                    winrateT.append(tabStats[k][0])     # ajout du pourcentage de victoire au tableau temporaire
                    if (tabStats[k][1] != -1):          # si la durrée de la manche n'est pas égale à -1
                        lenghtT.append(tabStats[k][1])  # ajout de la durée de la manche au tableau temporaire

            print("Modele :", [i, j])   # modèles du joueur 1 (celui auquel on s'intéresse)

            if (len(winrateT) != 0):    # divison par 0
                winrateG = sum(winrateT)/len(winrateT)
            else:
                winrateG = 0
            print("Winrate :", winrateG) 

            if (len(lenghtT) != 0):     # divison par 0
                lenghtG = sum(lenghtT)/len(lenghtT)
            else:
                lenghtG = 0
            print("Durée :", lenghtG)
            print("\n")

            graphWinrate.append(winrateG)   # ajout des données temporaires aux tableaux des graphs
            graphLenght.append(lenghtG)

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
    [choix, prediction] = loadModele("std")  # chargement des différents modèles

    nbGames = 100           # nombre de partie jouées pour chaque combinaison de modèle
    nbCaillouxJ1 = 3        # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3        # nombre de cailloux du joueur 2

    tournoiIAvsIA(nbGames, nbCaillouxJ1, nbCaillouxJ2, choix, prediction)   # lancement du tournoi
