############### Import Libraries ####################
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


############### Reading csv files ####################
#Read the heart patient dataset
df = pd.read_csv('heart.csv')
df.head()

split_list = [0.3,0.2,0.1]

for i in range(3):
    print("Split Ratio", (1-split_list[i])*100, " : ", (split_list[i])*100)
    ############### Spliting dataset into test and training ####################
    #Split the Dataset for training and testing @70:30 ratio
    df_train,df_test = train_test_split(df,train_size=1-split_list[i], test_size=split_list[i], random_state=42, shuffle=True)

    print('Number of training dataset: ', len(df_train))
    print('Number of test dataset: ', len(df_test))


    ############### Seperate Dataset X and Y ####################
    #Drop the target column from test and training dataset
    X_train = df_train.drop(columns='target')
    X_test  = df_test.drop(columns='target')

    #Take the target column for the prediction
    Y_train = df_train['target']
    Y_test  = df_test['target']

    #Counting number of heart patient in different set
    total_train_heart_patient = Y_train[Y_train==1]
    total_train_no_heart_patient = Y_train[Y_train==0]

    total_test_heart_patient = Y_test[Y_test==1]
    total_test_no_heart_patient = Y_test[Y_test==0]

    print('For training...')
    print('Total heart patient in the dataset: ', len(total_train_heart_patient))
    print('Total patient having no heart deseases: ', len(total_train_no_heart_patient))
    print('\nFor testing...')
    print('Total heart patient in the dataset: ', len(total_test_heart_patient))
    print('Total patient having no heart deseases: ', len(total_test_no_heart_patient))


    ############### Half Space classifier ####################
    random_state = 0
    tol = 1e-3

    #Build a model of Perceptron
    clf_pctn = Perceptron(tol=tol, random_state=random_state)

    #Training the X_train dataset
    clf_pctn.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_pctn.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using perceptron algorithm...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    ############### Logistic Regression ####################

    random_state = 0
    max_iter = 1000

    #Build a model of Logistic Regression
    clf_lgr = LogisticRegression(random_state=random_state, max_iter=max_iter)

    #Training the X_train dataset
    clf_lgr.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_lgr.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using Logistic Regression...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    ############### SVM(linear kernel) ####################
    random_state = 0
    kernel = 'linear'

    #Build a model of SVM
    clf_svm_l = SVC(random_state=random_state, kernel=kernel)

    #Training the X_train dataset
    clf_svm_l.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_svm_l.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using SVM linear kernel...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    ############### SVM(Ploy kernel) ####################
    random_state = 0
    kernel = 'poly'

    #Build a model of SVM with StandardScalar
    clf_svm_p = make_pipeline(StandardScaler(), SVC(random_state=random_state, kernel=kernel))

    #Training the X_train dataset
    clf_svm_p.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_svm_p.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using SVM Ploynomial kernel...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    ############### SVM(Gussian kernel) ####################
    random_state = 0
    kernel = 'rbf'

    #Build a model of SVM with StandardScalar
    clf_svm_g = make_pipeline(StandardScaler(),SVC(random_state=random_state, kernel=kernel))

    #Training the X_train dataset
    clf_svm_g.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_svm_g.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using SVM gussian kernel...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    ############### SGD ####################
    random_state = 0
    max_iter=1000
    tol=1e-3
    alpha=0.001
    
    #Build a model of SGDClassifier with StandardScalar
    clf_svm_sgd = make_pipeline(StandardScaler(),SGDClassifier(max_iter=max_iter,alpha=alpha))

    #Training the X_train dataset
    clf_svm_sgd.fit(X_train,Y_train)

    #Predicting the X_test(testing) Dataset
    y_pred = clf_svm_sgd.predict(X_test)

    #Get the score/accuracy_score between y_pred and Y_test
    print('Using SGD classifier...')
    print("Accuracy: {0:.2f}%".format(accuracy_score(Y_test,y_pred)*100))

    #Plot confusion matrix for checking how it is predicted
    cfu_matrix = confusion_matrix(Y_test,y_pred)
    ax = sns.heatmap(cfu_matrix/sum(cfu_matrix), annot=True,fmt='.2%', cmap='Blues')

    print("\nnumber of support vectors obtained for every dataset split: ", len(clf_svm_l.support_vectors_))
    print("--------------------------------------------------------")
