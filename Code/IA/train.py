from AutoClasser import *

### ---------------------------------------------------------------- ###
###                                                                  ###
###            Entrainement des modèles suivant un DataSet           ###
###                                                                  ###
### ---------------------------------------------------------------- ###



def trainModel():
    train = pd.read_csv("./DataSets/data.csv", sep=" ")     # lecture des données d'entrainement
    model = runThroughClassificationAndTrainAndChoose([train['nbCaillouxJ1'],train['nbCaillouxJ2']], train['choixJ1'], 0.25,100,0.1)       # entrainement du modele de choix
    model = np.asarray([model, model])  
    model[1] = runThroughClassificationAndTrainAndChoose([train['nbCaillouxJ1'],train['nbCaillouxJ2'],train['choixJ1'],train['predictionJ2']], train['predictionJ1'], 0.25,100,0.1)     # entrainement du modele de prédiction
    return model