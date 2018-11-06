# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:49:43 2018

@author: jmajor
"""
#Imports
from difflib import SequenceMatcher
import pandas as pd

#Pull data from csv
df = pd.read_csv('C:/Users/jmajor/Desktop/emails.csv', header = None)

#Put data into a list
x = list(df[0])

#checks if there are any exact duplicates in the list
if (any(x.count(i) > 1 for i in x)) == False:
    print('No exact duplicates found\n')

#List to hold duplicate's location. Also used to avoid catching them twice
duplicates = []



#Function to find nrear but not perfect matches
def check_list(lis):
    for j in range(len(lis)):
        for i in range(len(lis)):
            if i != j and i not in duplicates and j not in duplicates:
                if SequenceMatcher(None, lis[j],lis[i]).ratio() > .9:
                    print(lis[j],
                          '\n'+str(lis[i]),
                          '\nMatch: ' + str(SequenceMatcher(None, lis[j],lis[i]).ratio()),
                          '\nlocation: ' + str(j+1),'\n' )
                    duplicates.append(j)

check_list(x)