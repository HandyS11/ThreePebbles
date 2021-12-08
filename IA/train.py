from AutoClasser import *

def trainModel():
    train = pd.read_csv("./data.csv", sep=",");
    model = runThroughClassificationAndTrainAndChoose([train['predictionJ2'],train['nbCaillouxJ1'],train['nbCaillouxJ2']], train['predictionJ1'], 0.25,100,0.1);
    return model;