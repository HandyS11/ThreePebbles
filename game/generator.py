from game import *
from gameWithIA import *
from modules import *



def generateData(nbLignes, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()

    with open('data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= ' '
        , quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['Winner', 'nbRound', 'Data'])

        for i in range(0, nbLignes):

            #[winner, round, tab] = game(nbCaillouxJ1, nbCaillouxJ2)
            [winner, round, tab] = gameWithIA(1, nbCaillouxJ1, nbCaillouxJ2)
            spamwriter.writerow([winner, round, tab])
            
    t2 = time.time()
    print("Length: ", t2 - t1, "s\n")


if (True):
    
    nbLignes = 1000
    nbCaillouxJ1 = 3
    nbCaillouxJ2 = 3
    
    print("Beginnig generation.\n")
    generateData(nbLignes, nbCaillouxJ1, nbCaillouxJ2)
    print("Generation complete.")