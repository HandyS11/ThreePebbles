import train
import pickle
from joblib import dump, load

model = train.trainModel()

d = open("choix.pickle",'w')
d.close();
d = open("prediction.pickle",'w')
d.close();

f = open("choix.pickle",'r+b')
s1 = pickle.dump(model[0], f)

fi = open("prediction.pickle", 'r+b')
s2 = pickle.dump(model[1], fi)