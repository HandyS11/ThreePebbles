from modules import *


def loadModele():
    ModeleChoixSVC = pickle.load(open("./modeles/choixSVC.pickle",'r+b')) 
    ModelePredictionSVC = pickle.load(open("./modeles/predictionSVC.pickle", 'r+b'))

    ModeleChoixKNN = pickle.load(open("./modeles/choixKNN.pickle",'r+b')) 
    ModelePredictionKNN = pickle.load(open("./modeles/predictionKNN.pickle", 'r+b'))

    ModeleChoixArbre = pickle.load(open("./modeles/choixArbre.pickle",'r+b')) 
    ModelePredictionArbre = pickle.load(open("./modeles/predictionArbre.pickle", 'r+b'))

    ModeleChoixDefaut = pickle.load(open("./modeles/choix.pickle",'r+b')) 
    ModelePredictionDefaut = pickle.load(open("./modeles/prediction.pickle", 'r+b'))


    choix = [ModeleChoixSVC, ModeleChoixKNN, ModeleChoixArbre, ModeleChoixDefaut]
    prediction = [ModelePredictionSVC, ModelePredictionKNN, ModelePredictionArbre, ModelePredictionDefaut]

    return [choix, prediction]