from train import *

class AIplayer:
    def __init__(self, model, cailloux = 3) -> None:
        self.model = model
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0

    def choisir(self, nbCaillouxJ2):
        self.choixCailloux = AutoPredictChoix([self.cailloux, nbCaillouxJ2],self.model);
        return self.choixCailloux;

    def predire(self):
        self.prediction = AutoPredictPrediction([predictionJ2,self.cailloux, nbCaillouxJ2,self.choixCailloux],self.model);
        return self.prediction
#--------------------------------------------------------------------------------------------------------------------------
class truePlayer:
    def __init__(self, cailloux = 3) -> None:
        self.cailloux = cailloux
        self.prediction = 0
        self.choixCailloux = 0

    def choisir(self, nbCaillouxJ2):
        self.choixCailloux = int(input("Combien de cailloux mettez vous en jeu : "))
        return self.choixCailloux;

    def predire(self):
        self.prediction = int(input("Quelle est votre prédiction : "))
        return self.prediction