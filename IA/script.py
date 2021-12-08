from AutoClasser import *

train = pd.read_csv("./IA/data.csv", sep=",");

print(train['nbRound']);

model = runThroughClassificationAndTrainAndChoose(np.asarray([train['nbRound'],train['nbRound']]), train['Winner'], 0.20,25,0.5);
result = AutoPredict([10,2,7,6],model);
print(result)