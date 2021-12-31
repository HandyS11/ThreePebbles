import sys
sys.path.append("./main")
from modules import *


def arrayIse(notArr):
    Arr = np.asarray(notArr)
    Arr = Arr[:, np.newaxis]
    return Arr

def sanitize(arr):

    for key,value in enumerate(arr):
        if(ma.isnan(value)):
            arr[key] = 0
    return arr

def sanitizeSex(arr):

    for key,value in enumerate(arr):
        if(value == "male"):
            arr[key] = 1
        else:
            arr[key] = 0
    return arr

def runThroughClassificationAndTrainAndChoose(X, y, trainPerc, depthArg, gammaArg):
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

    #--------------------------------------------------------------------------

    Arbre_decision = DecisionTreeClassifier(random_state=0, max_depth=depthArg)
    clfDT = Arbre_decision.fit(Xtrain,ytrain)
    
    ypredit = clfDT.predict(Xtest)
    accDT = accuracy_score(ytest, ypredit)
    
    DTconf = metrics.confusion_matrix(ytest, ypredit)
    #-------------------------------------------------------------------------
    
    KNN = KNeighborsClassifier()
    clfKNN = KNN.fit(Xtrain, ytrain)
    
    ypredit = clfKNN.predict(Xtest)
    accKNN = accuracy_score(ytest, ypredit)
    KNNConf = metrics.confusion_matrix(ytest, ypredit)
    #-------------------------------------------------------------------------
    
    clfSVC = svm.SVC(gamma = gammaArg)
    clfSVC.fit(Xtrain,ytrain)
    
    ypredit = clfSVC.predict(Xtest)
    accSVC = accuracy_score(ytest,ypredit)
    
    ypredit = clfSVC.predict(Xtest)
    SVCConf = metrics.confusion_matrix(ytest,ypredit)
    #-------------------------------------------------------------------------
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

    return mostAccurate

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

def AutoPredictChoix(data, model):
    data = np.asarray(data)
    data = data[np.newaxis, :]
    data.reshape(1,2)
    i = model.predict(data)
    return i

def AutoPredictPrediction(data, model):
    data = np.asarray(data)
    data = data[np.newaxis, :]
    i = model.predict(data)
    return i

def printTree(model):
    tree.plot_tree(model)
    plt.show()

def printSVC(model):

    # import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # we only take the first two features. We could
                          # avoid this ugly slicing by using a two-dim dataset
    y = iris.target

    h = .02  # step size in the mesh

    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(X, y)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
    lin_svc = svm.LinearSVC(C=C).fit(X, y)

    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # title for the plots
    titles = ['SVC with linear kernel',
                  'LinearSVC (linear kernel)',
                  'SVC with RBF kernel',
                  'SVC with polynomial (degree 3) kernel']


    for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])
    plt.show()