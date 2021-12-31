from modules import *
sys.path.append("./games")
#from gameIAvsRandom import *
from gameIAvsRandomObjet import *
warnings.filterwarnings("ignore")


### ---------------------------------------------------------------- ###
###                                                                  ###
###                        Programme principal                       ###
###                                                                  ###
### ---------------------------------------------------------------- ###



model = 0;      # choix du model de jeu pour l'IA
f = 0           # modele (choix)
fi = 0          # modele (prediction)


if(model == 0):
    f = open("./modeles/choixSVC.pickle",'r+b')
    fi = open("./modeles/predictionSVC.pickle", 'r+b')
    print("Mode SVC")
elif(model == 1):
    f = open("./modeles/choixKNN.pickle",'r+b')
    fi = open("./modeles/predictionKNN.pickle", 'r+b')
    print("Mode KNN")
else:
    f = open("./modeles/choixArbre.pickle",'r+b')
    fi = open("./modeles/predictionArbre.pickle", 'r+b')
    print("Mode Arbre de décision")


choix = pickle.load(f);         # chargement du model de choix
prediction = pickle.load(fi);   # chargement du model de prediction


print("Début de la simulation ..\n")
t1 = time.time()

nbGames = 1000
nbCaillouxJ1 = 3
nbCaillouxJ2 = 3
nbVictoireIA = 0
sommeRounds = 0


for i in range(0, nbGames):
    [winner, round, tab] = gameIAvsRandomObjet(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)

    sommeRounds = sommeRounds + round
    if (winner == 1):
        nbVictoireIA = nbVictoireIA + 1

t2 = time.time()

tempsS = t2 - t1
dureeM = sommeRounds/nbGames
pourcentageV = nbVictoireIA/nbGames*100

print("L'IA a gagné ", nbVictoireIA, " partie sur", nbGames)
print("Soit un pourcentage de victoire de", pourcentageV, "%")
print("La durée moyenne des partie est de", dureeM, "rounds.")
print("La simulation a durée", tempsS, "secondes.\n")