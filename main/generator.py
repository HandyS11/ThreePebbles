from modules import *
sys.path.append("./games")
from gameRandomvsRandom import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                Générateur de données d'entrainement              ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def generateData(option, nbLignes, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()    # temps exact avant le lancement de la génération

    with open('data.csv', 'w', newline='') as csvfile:      # ouverture/création d'un fichier .csv
        
        spamwriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)                          # options du writer
        spamwriter.writerow(['winnerRound', 'predictionJ1', 'predictionJ2', 'nbCaillouxJ1', "nbCaillouxJ2", "choixJ1"])     # nomage des colonnes

        for i in range(0, nbLignes):    
            [winner, round, tab] = gameRandomvsRandom(option, nbCaillouxJ1, nbCaillouxJ2)
            tab = np.asarray(tab)
            for i in range(0, tab.shape[0]):        
                spamwriter.writerow(tab[i])
            
    t2 = time.time()
    print("Length: ", t2 - t1, "s\n")


if (True):      # appel à lui même (on le lance directement)
    
    nbParties = 10000
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    option = 1
    
    print("Beginnig generation.\n")
    generateData(option, nbParties, nbCaillouxJ1, nbCaillouxJ2)
    print("Generation complete.")