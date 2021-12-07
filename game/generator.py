from game import *
from modules import *



def generateData(nbLignes):

    t1 = time.time()

    with open('data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= ' '
        , quotechar='|', quoting=csv.QUOTE_MINIMAL)

        spamwriter.writerow(['Winner', 'nbRoud', 'Data'])

        for i in range(0, nbLignes):

            [winner, round, tab] = game()
            spamwriter.writerow([winner, round, tab])
            
    t2 = time.time()
    print("Length: ", t2 - t1, "s\n")


if (True):
    print("Begin of the generation.\n")
    nbLignes = 1000000
    generateData(nbLignes)
    print("Generation complete.")