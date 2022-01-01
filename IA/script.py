import sys
import train
sys.path.append("./main")
from modules import *


model = train.trainModel()

d = open("./modeles/choix.pickle",'w')
d.close()
d = open("./modeles/prediction.pickle",'w')
d.close()

f = open("./modeles/choix.pickle",'r+b')
s1 = pickle.dump(model[0], f)

fi = open("./modeles/prediction.pickle", 'r+b')
s2 = pickle.dump(model[1], fi)