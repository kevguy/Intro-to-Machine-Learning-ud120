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

### What is the total value of the stock belonging to James Prentice?
for key in enron_data["PRENTICE JAMES"]:
    print key

print 'Stock value of James Prentice', enron_data["PRENTICE JAMES"]["total_stock_value"]

### How many email messages do we have from Wesley Colwell to persons of interest?
print 'No. of email messages from Wesley Colwell to POI is ', enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

### What's the value of stock options exercised by Jeffrey Skilling?
print 'Value of stock options exercised by Jeffrey Skilling is ', enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

### Of these three individuals (Lay, Skilling and Fastow), 
### who took home the most money (largest value of "total_payments" feature)? 
### How much money did that person get?
print 'Kenneth Lay: ', enron_data["LAY KENNETH L"]["total_payments"]
print 'Jeffrey Skilling: ', enron_data["SKILLING JEFFREY K"]["total_payments"]
print 'Andrew Fastow: ', enron_data["FASTOW ANDREW S"]["total_payments"]

### How many folks in this dataset have a quantified salary? What about a known email address?
import pandas as pd
import math
count = 0
for key in enron_data:
    if not(math.isnan(float(enron_data[key]["salary"]))):
        count = count + 1
print "People with quantified salary: ", count

count = 0
for key in enron_data:
    if (enron_data[key]["email_address"]!='NaN'):
        count = count + 1
print "People with known email address: ", count

