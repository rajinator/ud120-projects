#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print len(features_train[0])




#########################################################
### your code goes here ###


#def classify(features_train, labels_train):
    ### your code goes here--should return a trained decision tree classifer
#    from sklearn import tree
#    clf = tree.DecisionTreeClassifier()
#    clf.fit(features_train, labels_train)

#    return clf

#clf = classify(features_train, labels_train)
#pred = clf.predict(features_test)

#from sklearn.metrics import accuracy_score
#acc = accuracy_score(pred, labels_test)
#print "accuracy is: ",acc

#########################################################
### Code for using min_samples_split

def classify(features_train, labels_train, x):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=x)
    clf.fit(features_train, labels_train)

    return clf


#x = 2
#clf1 = classify(features_train, labels_train, x)
#pred1 = clf1.predict(features_test)

#x = 50
#clf2 = classify(features_train, labels_train, x)
#pred2 = clf2.predict(features_test)

x = 40
clf3 = classify(features_train, labels_train, x)
pred3 = clf3.predict(features_test)

from sklearn.metrics import accuracy_score

#acc_min_samples_split_2 = accuracy_score(pred1, labels_test)
#acc_min_samples_split_50 = accuracy_score(pred2, labels_test)
acc_min_samples_split_40 = accuracy_score(pred3, labels_test)

#print "accuracy with min_samples_split 2 is: ", acc_min_samples_split_2
#print "accuracy with min_samples_split 50 is: ", acc_min_samples_split_50
print "accuracy with min_samples_split 40 is: ", acc_min_samples_split_40

#########################################################
### Code for entropy calculation is in entropy_calc.py



