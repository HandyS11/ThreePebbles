from AutoClasser import *

train = pd.read_csv("./data.csv", sep=",");

model = runThroughClassificationAndTrainAndChoose([train['predJ1'],train['Data']], train['Winner'], 0.20,70,0.5);
result = AutoPredict([[2,1],[3,-1],[1,0],[1,1]],model);
print(result)