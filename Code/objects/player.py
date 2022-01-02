import random
import sys
sys.path.append("./Code/IA")
from AutoClasser import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###          Version object permettant de simuler des parties        ###
###                                                                  ###
### ---------------------------------------------------------------- ###



class AIplayer: #Objet qui définit un joueur IA
    def __init__(self, ChoixModel, PredictionModel,cailloux:int = 3) -> None: #constructeur du joueur IA
        self.ChoixModel = ChoixModel            #Modèle IA pour que le joueur choisisse son nombre de cailloux
        self.PredictionModel = PredictionModel  #Modèle IA pour que le joueur parie sur le nombre de cailloux totaux
        self.cailloux:int = cailloux            #nb de cailloux du joueur
        self.prediction:int = 0                 #prédiction du joueur (pari)
        self.choixCailloux:int = 0              #nb de cailloux choisis par le joueur
        self.defautCailloux:int = cailloux      #nb de cailloux détenus par le joueur, par défaut

    def choisir(self, nbCaillouxJ2: int):       #fait choisir un nombre de cailloux à mettre en jeu à l'ia
        self.choixCailloux = AutoPredictChoix([self.cailloux, nbCaillouxJ2],self.ChoixModel)[0]
        if(self.choixCailloux > self.cailloux): #si le choix est supérieur au maximum de cailloux que l'ia détient, on le limite
            self.choixCailloux = self.cailloux

    def predire(self, nbCaillouxJ2:int, predictionJ2:int = -1):    #argument optionnel predictionJ2
        self.prediction = (AutoPredictPrediction([predictionJ2,self.cailloux, nbCaillouxJ2,self.choixCailloux],self.PredictionModel))[0]
        if(self.prediction > self.cailloux + nbCaillouxJ2):        #si le choix est supérieur au maximum de cailloux des 2 joueurs, on le limite
            self.prediction = (self.cailloux + nbCaillouxJ2)

    def clipPred(self,nbCaillouxJ2: int):                           #code de limite déjà inclus dans la prédiction
        if (self.prediction > (self.cailloux+nbCaillouxJ2)):
            self.prediction = (self.cailloux+nbCaillouxJ2)

    def reset(self):    #remise à zéro du joueur
        self.prediction = 0
        self.choixCailloux = 0
        self.cailloux = self.defautCailloux

    def print(self):    #utilisé pour le débogage, affiche les variables internes
        print("IA > cailloux: ",self.cailloux," pred: ",self.prediction," choix: ", self.choixCailloux)

#--------------------------------------------------------------------------------------------------------------------------
class randPlayer:# objet qui définit un joueur random
    def __init__(self, cailloux = 3) -> None:   #les méthodes sont les mêmes que pour l'ia mais moins compliquées, pas besoin de les expliquer
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
class truePlayer:   #objet qui définit un vrai joueur (humain), idem, les méthodes sont identiques mais demandent une entrée.
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