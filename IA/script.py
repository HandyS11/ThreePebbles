from AutoClasser import *

train = pd.read_csv("./IA/data.csv", sep=",");

print(train['nbRound']);

model = runThroughClassificationAndTrainAndChoose([train['nbRound'],train['Winner']], train['Winner'], 0.20,40,0.5);
result = AutoPredict([[10,2],[11,2],[10,8],[11,9]],model);
print(result)