from AutoClasser import *

def trainModel():
    train = pd.read_csv("./dataset/data.csv", sep=" ")
    model = runThroughClassificationAndTrainAndChoose([train['nbCaillouxJ1'],train['nbCaillouxJ2']], train['choixJ1'], 0.25,100,0.1)
    model = np.asarray([model, model])
    model[1] = runThroughClassificationAndTrainAndChoose([train['predictionJ2'],train['nbCaillouxJ1'],train['nbCaillouxJ2'], train['choixJ1']], train['predictionJ1'], 0.25,100,0.1)
    return model