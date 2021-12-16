from modules import *
sys.path.append("./games")
from gameRandomvsRandom import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                Générateur de données d'entrainement              ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def generateData(option, nbParties, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()    # temps exact avant le lancement de la génération

    with open('data.csv', 'w', newline='') as csvfile:      # ouverture/création d'un fichier .csv
        
        spamwriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)          # options du writer
        
        if (option == 1):
            spamwriter.writerow(['winnerRound', 'nbCaillouxJ1', 'nbCaillouxJ2', 'choixJ1', 'choixJ2', 'predictionJ1', 'predictionJ2'])     # nomage des colonnes
        elif (option ==2):
            spamwriter.writerow(['nbCaillouxJ1', "nbCaillouxJ2", "choixJ1", 'predictionJ1', 'predictionJ2'])                                # nomage des colonnes
        else:
            print("Option impossible !")
            exit(1)

        for i in range(0, nbParties):            # Pour le nombre de parties choisi
            [winner, round, tab] = gameRandomvsRandom(option, nbCaillouxJ1, nbCaillouxJ2)   # faire un partie et récupérer les données de cette dernière
            tab = np.asarray(tab)               # transformation du tableau avec numpy
            for i in range(0, tab.shape[0]):    # pour tous les éléments du tableau
                spamwriter.writerow(tab[i])     # les écrire indépendament (lignes différentes)
            
    t2 = time.time()    # temps exact après l'exécution de la génération
    print("Length: ", t2 - t1, "s\n")   # calcul de la durée d'exécution


if (True):      # appel à lui même (on le lance directement)
    
    nbParties = 1000    # nombre de parties jouées
    nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2
    option = 2          # option pour choisir la forme des données retournées 
    
    print("Beginnig generation.\n")
    generateData(option, nbParties, nbCaillouxJ1, nbCaillouxJ2)     # lancement de la génération des données
    print("Generation complete.")