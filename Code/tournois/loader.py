import sys
sys.path.append("./Code/main")
from modules import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                        Loader des modèles                        ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def loadModele():       # chargement des différents modèles 

    ModeleChoixSVC = pickle.load(open("./Modeles/choixSVC.pickle",'r+b')) 
    ModelePredictionSVC = pickle.load(open("./Modeles/predictionSVC.pickle", 'r+b'))

    ModeleChoixKNN = pickle.load(open("./Modeles/choixKNN.pickle",'r+b')) 
    ModelePredictionKNN = pickle.load(open("./Modeles/predictionKNN.pickle", 'r+b'))

    ModeleChoixArbre = pickle.load(open("./Modeles/choixArbre.pickle",'r+b')) 
    ModelePredictionArbre = pickle.load(open("./Modeles/predictionArbre.pickle", 'r+b'))

    ModeleChoixDefaut = pickle.load(open("./Modeles/choix.pickle",'r+b')) 
    ModelePredictionDefaut = pickle.load(open("./Modeles/prediction.pickle", 'r+b'))


    choix = [ModeleChoixSVC, ModeleChoixKNN, ModeleChoixArbre, ModeleChoixDefaut]                               # tableau des modèles portant sur le choix
    prediction = [ModelePredictionSVC, ModelePredictionKNN, ModelePredictionArbre, ModelePredictionDefaut]      # tableau des modèles portant sur la prédiction

    return [choix, prediction]