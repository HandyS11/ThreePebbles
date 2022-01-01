from modules import *
sys.path.append("./games")
from gameRandomvsRandom import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                Generateur de donnees d'entrainement              ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def generateData(option, nbParties, nbCaillouxJ1, nbCaillouxJ2):

    t1 = time.time()    # temps exact avant le lancement de la generation

    with open('./datasets/data.csv', 'w', newline='') as csvfile:      # ouverture/creation d'un fichier .csv
        
        spamwriter = csv.writer(csvfile, delimiter= ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)          # options du writer
        
        if (option == 1):
            spamwriter.writerow(['winnerRound', 'nbCaillouxJ1', 'nbCaillouxJ2', 'choixJ1', 'choixJ2', 'predictionJ1', 'predictionJ2'])     # nomage des colonnes
        elif (option ==2):
            spamwriter.writerow(['nbCaillouxJ1', "nbCaillouxJ2", "choixJ1", 'predictionJ1', 'predictionJ2'])                                # nomage des colonnes
        else:
            print("Option impossible !")
            exit(1)

        for i in range(0, nbParties):            # Pour le nombre de parties choisi
            [winner, round, tab] = gameRandomvsRandom(option, nbCaillouxJ1, nbCaillouxJ2)   # faire un partie et recuperer les donnees de cette derniere
            tab = np.asarray(tab)               # transformation du tableau avec numpy
            for i in range(0, tab.shape[0]):    # pour tous les elements du tableau
                spamwriter.writerow(tab[i])     # les ecrire independament (lignes differentes)
            
    t2 = time.time()    # temps exact apres l'execution de la generation
    print("Length: ", t2 - t1, "s\n")   # calcul de la duree d'execution


if (True):      # appel a lui meme (on le lance directement)
    
    nbParties = 1000    # nombre de parties jouees
    nbCaillouxJ1 = 3    # nombre de cailloux du joueur 1
    nbCaillouxJ2 = 3    # nombre de cailloux du joueur 2
    option = 2          # option pour choisir la forme des donnees retournees 
    
    print("Beginnig generation.\n")
    generateData(option, nbParties, nbCaillouxJ1, nbCaillouxJ2)     # lancement de la generation des donnees
    print("Generation complete.")