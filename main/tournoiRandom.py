from modules import *
sys.path.append("./games")
from gameIAvsRandomObjet import *


ModeleChoixSVC = pickle.load(open("./modeles/choixSVC.pickle",'r+b')) 
ModelePredictionSVC = pickle.load(open("./modeles/predictionSVC.pickle", 'r+b'))

ModeleChoixKNN = pickle.load(open("./modeles/choixKNN.pickle",'r+b')) 
ModelePredictionKNN = pickle.load(open("./modeles/predictionKNN.pickle", 'r+b'))

ModeleChoixArbre = pickle.load(open("./modeles/choixArbre.pickle",'r+b')) 
ModelePredictionArbre = pickle.load(open("./modeles/predictionArbre.pickle", 'r+b'))

ModeleChoixDefaut = pickle.load(open("./modeles/choix.pickle",'r+b')) 
ModelePredictionDefaut = pickle.load(open("./modeles/prediction.pickle", 'r+b'))


choix = [ModeleChoixSVC, ModeleChoixKNN, ModeleChoixArbre, ModeleChoixDefaut]
prediction = [ModelePredictionSVC, ModelePredictionKNN, ModelePredictionArbre, ModelePredictionDefaut]


nbGames = 1000
nbCaillouxJ1 = 3
nbCaillouxJ2 = 3

print("Début de la simulation ..\n")
tempsD = time.time()

for i in range(4):
    choixModele = choix[i]

    for j in range(4):
        predictionModele = prediction[j]

        sommeRounds = 0
        nbVictoireIA = 0

        print("Simulation n°", i, j)

        for k in range(nbGames):
            [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choixModele, predictionModele)

            sommeRounds = sommeRounds + round

            if (winner == 1):
                nbVictoireIA = nbVictoireIA + 1

        dureeM = sommeRounds/nbGames
        pourcentageV = nbVictoireIA/nbGames*100

        print("Pourcentage de victoire de", pourcentageV, "%")
        print("La durée moyenne des partie est de", dureeM, "rounds.\n")


tempsF = time.time()
tempsS = tempsF - tempsD
print("La simulation a durée", tempsS, "secondes.\n")