from train import *
import random
import sys

class AIplayer:
    def __init__(self, model, cailloux = 3) -> None:
        self.model = model
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0

    def choisir(self, nbCaillouxJ2: int)->int:
        self.choixCailloux = AutoPredictChoix([self.cailloux, nbCaillouxJ2],self.model)
        if(self.choixCailloux > self.cailloux):
            self.choixCailloux = self.cailloux
        return self.choixCailloux

    def predire(self)->int:
        self.prediction = AutoPredictPrediction([predictionJ2,self.cailloux, nbCaillouxJ2,self.choixCailloux],self.model)
        return self.prediction
#--------------------------------------------------------------------------------------------------------------------------
class randPlayer:
    def __init__(self, cailloux = 3) -> None:
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0

    def choisir(self)-> int:
        self.choixCailloux = random.randint(0,self.cailloux)
        return self.choixCailloux

    def predire(self, nbCaillouxAdversaire: int)-> int:
        self.prediction = random.randint(0,(self.cailloux + nbCaillouxAdversaire))
        return self.prediction
#--------------------------------------------------------------------------------------------------------------------------
class truePlayer:
    def __init__(self, cailloux = 3) -> None:
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0

    def choisir(self)->int:
        self.choixCailloux = int(input("Combien de cailloux mettez vous en jeu : "))

        return self.choixCailloux

    def predire(self)->int:
        self.prediction = int(input("Quelle est votre prédiction : "))
        return self.prediction