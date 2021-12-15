from modules import *
sys.path.append("./games")
from gameRandomvsRandom import *



def generateData(nbLignes, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()

    with open('data.csv', 'w', newline='') as csvfile: 
        spamwriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['winnerRound', 'predictionJ1', 'predictionJ2', 'nbCaillouxJ1', "nbCaillouxJ2", "choixJ1"])

        for i in range(0, nbLignes):    
            [winner, round, tab] = gameRandomvsRandom(1, nbCaillouxJ1, nbCaillouxJ2)
            tab = np.asarray(tab)
            for i in range(0, tab.shape[0]):        
                spamwriter.writerow(tab[i])
            
    t2 = time.time()
    print("Length: ", t2 - t1, "s\n")


if (True):
    
    nbParties = 10000
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    
    print("Beginnig generation.\n")
    generateData(nbParties, nbCaillouxJ1, nbCaillouxJ2)
    print("Generation complete.")