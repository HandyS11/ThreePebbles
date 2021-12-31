import random
import sys
sys.path.append("./IA")
from train import *


class AIplayer:
    def __init__(self, ChoixModel, PredictionModel,cailloux:int = 3) -> None:
        self.ChoixModel = ChoixModel
        self.PredictionModel = PredictionModel
        self.cailloux:int = cailloux
        self.prediction:int = 0
        self.choixCailloux:int = 0
        self.defautCailloux:int = cailloux

    def choisir(self, nbCaillouxJ2: int):
        self.choixCailloux = AutoPredictChoix([self.cailloux, nbCaillouxJ2],self.ChoixModel)[0]
        if(self.choixCailloux > self.cailloux):
            self.choixCailloux = self.cailloux

    def predire(self, nbCaillouxJ2:int, predictionJ2:int = -1):    #argument optionnel predictionJ2
        self.prediction = (AutoPredictPrediction([predictionJ2,self.cailloux, nbCaillouxJ2,self.choixCailloux],self.PredictionModel))[0]
        if(self.prediction > self.cailloux + nbCaillouxJ2):
            self.prediction = (self.cailloux + nbCaillouxJ2)

    def clipPred(self,nbCaillouxJ2: int):
        if (self.prediction > (self.cailloux+nbCaillouxJ2)):
            self.prediction = (self.cailloux+nbCaillouxJ2)

    def reset(self):
        self.prediction = 0
        self.choixCailloux = 0
        self.cailloux = self.defautCailloux

    def print(self):
        print("IA > cailloux: ",self.cailloux," pred: ",self.prediction," choix: ", self.choixCailloux)

#--------------------------------------------------------------------------------------------------------------------------
class randPlayer:
    def __init__(self, cailloux = 3) -> None:
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0
        self.defautCailloux = cailloux


    def choisir(self)-> int:
        self.choixCailloux = random.randint(0,self.cailloux)
        return self.choixCailloux

    def predire(self, nbCaillouxAdversaire: int)-> int:
        self.prediction = random.randint(0,(self.cailloux + nbCaillouxAdversaire))
        return self.prediction

    def reset(self):
        self.prediction = 0
        self.choixCailloux = 0
        self.cailloux = self.defautCailloux

    def print(self):
        print("random > cailloux: ",self.cailloux," pred: ",self.prediction," choix: ", self.choixCailloux)
#--------------------------------------------------------------------------------------------------------------------------
class truePlayer:
    def __init__(self, cailloux = 3) -> None:
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0
        self.defautCailloux = cailloux


    def choisir(self)->int:
        self.choixCailloux = int(input("Combien de cailloux mettez vous en jeu : "))

        return self.choixCailloux

    def predire(self)->int:
        self.prediction = int(input("Quelle est votre prédiction : "))
        return self.prediction

    def reset(self):
        self.prediction = 0
        self.choixCailloux = 0
        self.cailloux = self.defautCailloux