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
import pprint
import math

pp = pprint.PrettyPrinter(indent=4)

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

num_persons = float(len(enron_data.keys()))

print "Number of people in Enron dataset are: ",num_persons

#from collections import Counter

#C = Counter(enron_data.keys())

#print "Number of people in Enron dataset are:",sum(C.values())

#C.clear()

#print enron_data["SKILLING JEFFREY K"]

n = 0
for i in enron_data:
    if enron_data[i]["poi"]==1:
     n += 1
print "Number of POIs are :",n

print "James Pretice's total stock value is:",enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Emails sent from Wesley Colwell to persons of interest:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Stock options exercised by Jeffrey K Skilling are:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#print "Names of keys in enron_data: ", pp.pprint(enron_data.keys())
#print "enron_data: ", pp.pprint(enron_data)

#print "Value of total_payments for Jeff Skilling is: ",enron_data["SKILLING JEFFREY K"]["total_payments"]

#print "Value of total_patments for Ken Lay is: ",enron_data["LAY KENNETH L"]["total_payments"]

#print "Value of total_patments for Andrew Fastow is: ",enron_data["FASTOW ANDREW S"]["total_payments"]

total_comp_list = {("Jeff Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"]),("Ken Lay", enron_data["LAY KENNETH L"]["total_payments"]),("Andy Fastow", enron_data["FASTOW ANDREW S"]["total_payments"])}

print "Person who took most money among Ken Lay, Jeff Skilling and Andy Fastow is: ",max(total_comp_list)

n = 0
for i in enron_data:
    if enron_data[i]["salary"] !='NaN':
     n += 1

print "Number of people in Dataset with a quantified Salary are: ", n

n = 0
for i in enron_data:
    if enron_data[i]["email_address"] != 'NaN':
        n += 1

print "Number of people in Dataset with a known email address are: ", n

n = 0
for i in enron_data:
    if enron_data[i]["total_payments"] == 'NaN':
        n += 1
perc_people = str(round((n/num_persons) * 100,2))+"%"

print "Number and Percentage of people in Dataset with 'NaN' for their total payments are: Number - ", n," " + "Percentage - ",perc_people

n = 0
for i in enron_data:
    if enron_data[i]["total_payments"] == 'NaN' and enron_data[i]["poi"]==1:
        n += 1
perc_people = str(round((n/num_persons) * 100,2))+"%"

print "Number and Percentage of people in Dataset with 'NaN' for their total payments who are also POIs are: Number - ", n," " + "Percentage - ",perc_people
