import sys
sys.path.append("./Code/main")
from modules import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                        Loader des modèles                        ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def loadModele():       # chargement des différents modèles 

    pickedMode = "+1"

    ModeleChoixSVC = pickle.load(open("./Modeles/"+pickedMode+"/choixSVC.pickle",'r+b')) 
    ModelePredictionSVC = pickle.load(open("./Modeles/"+pickedMode+"/predictionSVC.pickle", 'r+b'))

    ModeleChoixKNN = pickle.load(open("./Modeles/"+pickedMode+"/choixKNN.pickle",'r+b')) 
    ModelePredictionKNN = pickle.load(open("./Modeles/"+pickedMode+"/predictionKNN.pickle", 'r+b'))

    ModeleChoixArbre = pickle.load(open("./Modeles/"+pickedMode+"/choixArbre.pickle",'r+b')) 
    ModelePredictionArbre = pickle.load(open("./Modeles/"+pickedMode+"/predictionArbre.pickle", 'r+b'))


    choix = [ModeleChoixSVC, ModeleChoixKNN, ModeleChoixArbre]                               # tableau des modèles portant sur le choix
    prediction = [ModelePredictionSVC, ModelePredictionKNN, ModelePredictionArbre]      # tableau des modèles portant sur la prédiction

    return [choix, prediction]