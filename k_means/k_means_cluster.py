#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### Task: What would be the rescaled value of a "salary" feature that had an original value of $200,000, 
### and an "exercised_stock_options" feature of $1 million?
from sklearn.preprocessing import MinMaxScaler
fake_data = data
fake_data = numpy.append(fake_data, [[float(0), float(200000), float(1000000)]], 0)
weights = numpy.array(fake_data)
scaler = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)

print rescaled_weights

print "rescaled value of $200000 in feature 'salary'"
print rescaled_weights[len(rescaled_weights)-1][1]
print "rescaled value of $1000000 in feature 'exercised_stock_options'"
print rescaled_weights[len(rescaled_weights)-1][2]



### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
clf = KMeans(n_clusters = 2)
clf.fit(data)
pred = clf.predict(data)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"


### Task for finding maximum and minimum values taken by the "exercised_stock_options" feature used in this example
min = 10000000000
max = -10000000000
for item in data_dict:
    if data_dict[item]['exercised_stock_options'] != "NaN":
        val = data_dict[item]['exercised_stock_options']
        if min > val:
            min = val
        if max < val:
            max = val

print 'Minimum is ', min
print 'Maximum is ', max

### Task for finding the maximum and minimum values taken by "salary"
min = 10000000000
max = -10000000000
for item in data_dict:
    if data_dict[item]['salary'] != "NaN":
        val = data_dict[item]['salary']
        if min > val:
            min = val
        if max < val:
            max = val

print 'Minimum is ', min
print 'Maximum is ', max