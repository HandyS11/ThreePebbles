from train import *
import numpy as np
sys.path.append("./Code/objects")
from player import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###           Fonction de choix et de prédiction du modèle           ###
###                                                                  ###
### ---------------------------------------------------------------- ###



# interface entre la partie et l'AutoClasseur
def choixBigBrain(nbCaillouxJ1, nbCaillouxJ2, model):   
     return AutoPredictChoix([nbCaillouxJ1, nbCaillouxJ2],model)


# interface entre la partie et l'AutoClasseur
def predictionBigBrain(nbCaillouxJ1, nbCaillouxJ2, predictionJ2,choixJ1, model):
     return AutoPredictPrediction([predictionJ2,nbCaillouxJ1, nbCaillouxJ2,choixJ1],model)