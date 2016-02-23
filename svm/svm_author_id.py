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
### features_train = features_train[:len(features_train)/100] 
### labels_train = labels_train[:len(labels_train)/100] 

from sklearn.svm import SVC
clf = SVC(kernel = 'rbf', C=10000)
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
print 'Accuracy calculated, and the accuracy is', accuracy, '\n'

### predict 10, 26, 50th element of testing dataset
### assuming zero-indexed list
sequence = [10, 26, 50]
for i in range(0,3):
    print 'Predicting ', sequence[i], 'th element'
    pred2 = clf.predict([features_test[sequence[i]]])
    print 'Prediction is ', pred2
    print 'Real result is ', labels_test[sequence[i]]
    print '\n'


print 'Bye\n'
#########################################################


