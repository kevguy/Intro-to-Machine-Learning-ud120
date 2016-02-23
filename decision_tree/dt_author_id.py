#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree

min_samples_split_para = 40
clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split_para)
print 'Training starts'
clf = clf.fit(features_train, labels_train)
print 'Training finishes'

from sklearn.metrics import accuracy_score
print 'Beginning prediction'
pred = clf.predict(features_test)
print 'Prediction finishes'

print 'Calculating Accuracy'
accuracy = accuracy_score(labels_test, pred)
print 'The accuracy is ', accuracy


'''
data is organized into a numpy array where 
the number of rows is the number of data points
the number of columns is the number of features
'''
print 'no. of data points (no. of rows) is', len(features_train)
print 'no. of features (no. of columns) is ', len(features_train[0])
#########################################################


