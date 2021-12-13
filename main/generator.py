from modules import *
sys.path.append("./games")
import gameBasic
from gameRandom import *



def generateData(option, nbLignes, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()

    with open('data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= ' '
        , quotechar='|', quoting=csv.QUOTE_MINIMAL)

        if (option == 1):
            spamwriter.writerow(['winnerRound', 'predictionJ1', 'predictionJ2', 'nbCaillouxJ1', "nbCaillouxJ2"])

            for i in range(0, nbLignes):    
                [winner, round, tab] = gameWithIA(1, nbCaillouxJ1, nbCaillouxJ2)
                tab = np.asarray(tab)
                for i in range(0, tab.shape[0]):        
                    spamwriter.writerow(tab[i])
                    
        elif (option == 2):
            spamwriter.writerow(['Winner', 'Round', 'Data'])

            for i in range(0, nbLignes):    
                [winner, round, tab] = gameBasic(nbCaillouxJ1, nbCaillouxJ2)
                tab = np.asarray(tab)
                for i in range(0, tab.shape[0]):        
                    spamwriter.writerow(tab[i])
            
            
    t2 = time.time()
    print("Length: ", t2 - t1, "s\n")


if (True):
    
    nbLignes = 10000
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    
    print("Beginnig generation.\n")
    generateData(1, nbLignes, nbCaillouxJ1, nbCaillouxJ2)
    print("Generation complete.")