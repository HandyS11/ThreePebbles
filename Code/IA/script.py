import sys
import train
sys.path.append("./Code/main")
from modules import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                     Enregistrement des modèles                   ###
###                                                                  ###
### ---------------------------------------------------------------- ###



model = train.trainModel()

d = open("./Modeles/choix.pickle",'w')
d.close()
d = open("./Modeles/prediction.pickle",'w')
d.close()

f = open("./Modeles/choix.pickle",'r+b')
s1 = pickle.dump(model[0], f)

fi = open("./Modeles/prediction.pickle", 'r+b')
s2 = pickle.dump(model[1], fi)