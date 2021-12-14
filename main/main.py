from modules import *
sys.path.append("./../games")
from gameIAvsRandom import *
import pickle
from joblib import dump, load


f = open("./../IA/choix.pickle",'r+b')
fi = open("./../IA/prediction.pickle", 'r+b')
choix = pickle.load(f);
prediction = pickle.load(fi);


print("Début de la simulation ..\n")


nbGames = 1000
nbCaillouxJ1 = 3
nbCaillouxJ2 = 3
nbVictoireIA = 0
sommeRounds = 0



for i in range(0, nbGames):
    [winner, round, tab] = gameIAvsRandom(nbCaillouxJ1, nbCaillouxJ2, choix, prediction)
    sommeRounds = sommeRounds + round
    if (winner == 1):
        nbVictoireIA = nbVictoireIA + 1
    

print("L'IA a gagné ", nbVictoireIA, " partie sur ", nbGames)
print("Soit un pourcentage de victoire de ", nbVictoireIA/nbGames*100, "%")
print("La durée moyenne des partie est de ", sommeRounds/nbGames, " rounds.")