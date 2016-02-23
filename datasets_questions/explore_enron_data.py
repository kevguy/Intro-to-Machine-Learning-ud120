#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### How many data points?
print 'No. of data points is ', len(enron_data)

### How many features?
print 'No. of features is ', len(enron_data["SKILLING JEFFREY K"])

### How mant POIs?
count = 0
for key in enron_data:
    if (enron_data[key]["poi"] == 1):
        count = count + 1

print 'No. of POIs is ', count
