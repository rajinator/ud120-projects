#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
import time
from sklearn.svm import SVC

clf = SVC(kernel="rbf",C=10000)

##uncomment the below lines to achieve faster training time by using 1% of training set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time.time()
clf.fit(features_train, labels_train)
print"time for clf fit: " ,round(time.time()-t0, 3), "seconds"

t0 = time.time()
pred = clf.predict(features_test)
print"time for clf prediction: " ,round(time.time()-t0, 3), "seconds"

from sklearn.metrics.scorer import accuracy_score

accuracy = accuracy_score(pred, labels_test)

print(accuracy)

##below commented code will print individual class predictions for element [n]
#print pred[10]
#print pred[26]
#print pred[50]

##this code will print how many are in class 1 - predicted for Chris

i = 0
sum_i = 0
while i < len(pred):
#    print i
    if pred[i] == 1:
     sum_i += 1
    i += 1

print sum_i