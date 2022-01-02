import sys
sys.path.append("./Code/main")
from modules import *


### ---------------------------------------------------------------- ###
###                                                                  ###
###                           Modèles..                              ###
###                                                                  ###
### ---------------------------------------------------------------- ###

#Ce fichier contient les fonctions liées à l'entraînement du modèle de classification et à la prédiction, et aux conversions requises.



# si l'entrée n'est pas un tableau elle est convertie en tableau
def arrayIse(notArr):
    Arr = np.asarray(notArr)
    Arr = Arr[:, np.newaxis]
    return Arr
# si l'entrée contient des valeurs qui ne sont pas des chiffres (NaN), on les met 0
def sanitize(arr):

    for key,value in enumerate(arr):
        if(ma.isnan(value)):
            arr[key] = 0
    return arr

#Cette fonction va entraîner 3 modèles sur le dataset donné, un Arbre de décision, un SVM, et un Voisin proche.
#Elle sélectionne ensuite le plus performant pour la tâche et le retourne.
def runThroughClassificationAndTrainAndChoose(X, y, trainPerc, depthArg, gammaArg):

    #sanitation et conversions :
    X = np.asarray(X)
    X = X.reshape((X.shape[1],X.shape[0]))
    y = np.asarray(y)

    print(X)
    if(X.shape[0] == 1):
        X = sanitize(arrayIse(X))

    y = sanitize(y)

    if(trainPerc > 1):
        trainPerc = 1
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=trainPerc,random_state=0)

    #-------------------------------------------------------------------------- Entraînement Arbre de décision

    Arbre_decision = DecisionTreeClassifier(random_state=0, max_depth=depthArg)
    clfDT = Arbre_decision.fit(Xtrain,ytrain)
    
    ypredit = clfDT.predict(Xtest)
    accDT = accuracy_score(ytest, ypredit)
    
    DTconf = metrics.confusion_matrix(ytest, ypredit)

    #------------------------------------------------------------------------- Entraînement Voisin Proche
    
    KNN = KNeighborsClassifier()
    clfKNN = KNN.fit(Xtrain, ytrain)
    
    ypredit = clfKNN.predict(Xtest)
    accKNN = accuracy_score(ytest, ypredit)
    KNNConf = metrics.confusion_matrix(ytest, ypredit)

    #------------------------------------------------------------------------- Entraînement vecteurs proches (SVM)
    
    clfSVC = svm.SVC(gamma = gammaArg)
    clfSVC.fit(Xtrain,ytrain)
    
    ypredit = clfSVC.predict(Xtest)
    accSVC = accuracy_score(ytest,ypredit)
    
    ypredit = clfSVC.predict(Xtest)
    SVCConf = metrics.confusion_matrix(ytest,ypredit)

    #------------------------------------------------------------------------- Séléction du modèle le plus performant

    if (accDT >= accKNN) and (accDT >= accSVC):
        mostAccurate = clfDT
        print("Decision tree choosen : ",accDT," accuracy")
        print(DTconf) 
    elif (accKNN >= accDT) and (accKNN >= accSVC):
        mostAccurate = clfKNN
        print("KNN choosen : ",accKNN," accuracy")
        print(KNNConf)
    else:
        mostAccurate = clfSVC
        print("SVC choosen : ",accSVC," accuracy")
        print(SVCConf)

    return mostAccurate #retour de ce modèle

#prédit une valeur en fonction d'une autre valeurn donnée, en faisant les conversions requises
def AutoPredict(data, model):
    data = np.asarray(data)
    print(data)
    data = data[np.newaxis, :]
    print(data)
    print(data.shape)
    data.reshape(1,2)
    print(data.shape)
    i = model.predict(data)
    print("done ",i)
    return i

#idem mais pour le choix d'un nombre de cailloux
def AutoPredictChoix(data, model):
    data = np.asarray(data)
    data = data[np.newaxis, :]
    data.reshape(1,2)
    i = model.predict(data)
    return i

#idem mais pour la prédiction d'un nombre de cailloux
def AutoPredictPrediction(data, model):
    data = np.asarray(data)
    data = data[np.newaxis, :]
    i = model.predict(data)
    return i

#utilisé pour le débogage des arbres de décision, les affiche
def printTree(model):
    tree.plot_tree(model)
    plt.show()