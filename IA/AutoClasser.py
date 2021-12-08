import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import math as ma
from sklearn.datasets import load_iris
from sklearn import tree

def arrayIse(notArr):
    Arr = np.asarray(notArr)
    Arr = Arr[:, np.newaxis];
    return Arr;

def sanitize(arr):

    for key,value in enumerate(arr):
        if(ma.isnan(value)):
            arr[key] = 0;
    return arr;

def sanitizeSex(arr):

    for key,value in enumerate(arr):
        if(value == "male"):
            arr[key] = 1;
        else:
            arr[key] = 0;
    return arr;

def runThroughClassificationAndTrainAndChoose(X, y, trainPerc, depthArg, gammaArg):
    X = np.asarray(X);
    X = X.reshape((X.shape[1],X.shape[0]))
    y = np.asarray(y);

    print(X);
    if(X.shape[0] == 1):
        X = sanitize(arrayIse(X));

    y = sanitize(y);

    from sklearn.model_selection import train_test_split
    if(trainPerc > 1):
        trainPerc = 1
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=trainPerc,random_state=0)

    #--------------------------------------------------------------------------
    from sklearn.datasets import load_iris
    from sklearn import tree
    from sklearn.tree import DecisionTreeClassifier

    Arbre_decision = DecisionTreeClassifier(random_state=0, max_depth=depthArg)
    clfDT = Arbre_decision.fit(Xtrain,ytrain)
    
    from sklearn.metrics import accuracy_score
    ypredit = clfDT.predict(Xtest)
    accDT = accuracy_score(ytest, ypredit);
    
    from sklearn import metrics
    DTconf = metrics.confusion_matrix(ytest, ypredit)
    #-------------------------------------------------------------------------
    from sklearn.neighbors import KNeighborsClassifier
    
    KNN = KNeighborsClassifier()
    clfKNN = KNN.fit(Xtrain, ytrain)
    
    ypredit = clfKNN.predict(Xtest)
    accKNN = accuracy_score(ytest, ypredit)
    KNNConf = metrics.confusion_matrix(ytest, ypredit)
    #-------------------------------------------------------------------------
    from sklearn import svm
    
    clfSVC = svm.SVC(gamma = gammaArg)
    clfSVC.fit(Xtrain,ytrain)
    
    from sklearn.metrics import accuracy_score
    ypredit = clfSVC.predict(Xtest)
    accSVC = accuracy_score(ytest,ypredit);
    
    ypredit = clfSVC.predict(Xtest)
    SVCConf = metrics.confusion_matrix(ytest,ypredit)
    #-------------------------------------------------------------------------
    if (accDT >= accKNN) and (accDT >= accSVC):
        mostAccurate = clfDT
        print("Decision tree choosen : ",accDT," accuracy")
        print(DTconf);
        printTree(mostAccurate)
  
    elif (accKNN >= accDT) and (accKNN >= accSVM):
        mostAccurate = clfKNN
        print("KNN choosen : ",accKNN," accuracy")
        print(KNNConf);
    else:
        mostAccurate = clfSVC
        print("SVC choosen : ",accSVC," accuracy")
        print(SVCConf);

    return mostAccurate;

def AutoPredict(data, model):
    data = np.asarray(data);
    if(data.shape[0] == 1):
        data = sanitize(arrayIse(data));
    return model.predict(data);

def printTree(model):
    tree.plot_tree(model)
    plt.show();