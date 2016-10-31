#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn import tree

clf = tree.DecisionTreeClassifier()
print 'Training starts'
clf = clf.fit(features, labels)
print 'Training finishes'

print 'Accuracy'
print clf.score(features, labels)

#from sklearn.metrics import accuracy_score
#print 'Beginning prediction'
#pred = clf.predict(features_test)
#print 'Prediction finishes'

#print 'Calculating Accuracy'
#accuracy = accuracy_score(labels_test, pred)
#print 'The accuracy is ', accuracy

