from train import *
import numpy as np

def playRoundBigBrain(predictionJ2,nbCaillouxJ1,nbCaillouxJ2,model):
     AutoPredict([predictionJ2,nbCaillouxJ1,nbCaillouxJ2],[1,1,1],model)[0];


def choixBigBrain(nbCaillouxJ1, nbCaillouxJ2, model):
     #faire décider le modèle
     return AutoPredict([nbCaillouxJ1, nbCaillouxJ2],model);


def predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2,choixJ1, model):
     #faire décider le modèle
     return AutoPredict([predictionJ2,nbCaillouxJ1, nbCaillouxJ2,choixJ1],model);


#print(result)