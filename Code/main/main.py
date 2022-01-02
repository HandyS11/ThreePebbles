from modules import *
sys.path.append("./Code/games")
from gameIAvsRandom import *
from gameIAvsRandomObjet import *
from gameIAvsIAObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                        Programme principal                       ###
###                                                                  ###
### ---------------------------------------------------------------- ###



model = -1      # choix du model de jeu pour l'IA
f = 0           # modele (choix)
fi = 0          # modele (prediction)


if (model == 0):
    f = open("./Modeles/choixSVC.pickle",'r+b')
    fi = open("./Modeles/predictionSVC.pickle", 'r+b')
    print("Mode SVC")
elif (model == 1):
    f = open("./Modeles/choixKNN.pickle",'r+b')
    fi = open("./Modeles/predictionKNN.pickle", 'r+b')
    print("Mode KNN")
elif (model == 2):
    f = open("./Modeles/choixArbre.pickle",'r+b')
    fi = open("./Modeles/predictionArbre.pickle", 'r+b')
    print("Mode Arbre de décision")
elif (model == 3):
    f = open("./Modeles/choixArbre.pickle",'r+b')
    fi = open("./Modeles/predictionSVC.pickle", 'r+b')
    print("Mode Arbre + SVC")
else:
    f = open("./Modeles/choix.pickle",'r+b')
    fi = open("./Modeles/prediction.pickle", 'r+b')
    print("Mode Défaut")


choix = pickle.load(f)          # chargement du model de choix
prediction = pickle.load(fi)    # chargement du model de prediction


print("Début de la simulation ..\n")
tempsD = time.time()    

nbGames = 1000      # nombre de parties
nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2
nbVictoireIA = 0    # nombre de victoire de l'IA
sommeRounds = 0     # nombre total de round


for i in range(nbGames):
    #[winner, round, tab] = gameIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
    [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choix, prediction) 

    sommeRounds = sommeRounds + round
    if (winner == 1):
        nbVictoireIA = nbVictoireIA + 1

tempsF = time.time()

tempsS = tempsF - tempsD
dureeM = sommeRounds/nbGames
pourcentageV = nbVictoireIA/nbGames*100

print("L'IA a gagné ", nbVictoireIA, " partie sur", nbGames)
print("Soit un pourcentage de victoire de", pourcentageV, "%")
print("La durée moyenne des parties est de", dureeM, "rounds.")
print("La simulation a durée", tempsS, "secondes.\n")