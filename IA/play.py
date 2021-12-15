from train import *
import numpy as np
sys.path.append("./objects")
from player import *


def choixBigBrain(nbCaillouxJ1, nbCaillouxJ2, model):
     #faire décider le modèle
     return AutoPredictChoix([nbCaillouxJ1, nbCaillouxJ2],model);


def predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2,choixJ1, model):
     #faire décider le modèle
     return AutoPredictPrediction([predictionJ2,nbCaillouxJ1, nbCaillouxJ2,choixJ1],model);


#print(result)