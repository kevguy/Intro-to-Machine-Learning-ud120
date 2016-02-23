#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

from sklearn.svm import SVC
clf = SVC(kernel = 'rbf')
print 'Training begins'
t0 = time()
clf.fit(features_train, labels_train)
print 'Training finishes'
print 'Training time:', round(time()-t0), 's'

print 'Commencing Prediction'
t0 = time()
pred = clf.predict(features_test)
print 'Prediction time:', round(time()-t0), 's'
print 'Prediction finishes'

### calculate accuracy
from sklearn.metrics import accuracy_score
print 'Calculating accuracy'
accuracy = accuracy_score(labels_test, pred)
print 'Accuracy calculated, and the accuracy is', accuracy
print 'Bye\n'
#########################################################


