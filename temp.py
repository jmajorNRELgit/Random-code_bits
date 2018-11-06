# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:49:43 2018

@author: jmajor
"""

#Imports
from difflib import SequenceMatcher
import pandas as pd
import time

#function to remove exact duplicates
def remove_exact_duplicates(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)



#Function to find nrear but not perfect matches
def check_list(lis):

    #List to hold duplicate's location only used to avoid catching them twice
    dup_list = []

    #holds duplicate location data
    duplicate_locations = []

    for j in range(len(lis)): # j holds one address at a time
        for i in range(len(lis)): #compares the rest to j
            if i != j and i not in dup_list and j not in dup_list: #prevents catching the same duplicate twice
                ratio = SequenceMatcher(None, lis[j],lis[i]).quick_ratio() #match ratio
                if ratio > .9:
                    print(lis[j],
                          '\n'+lis[i],
                          '\nMatch: ' + str(ratio),
                          '\nlocations: ' + str(j+1),str(i+1),'\n' )
                    locations = lis[j] + ': ' +str(j+1) + ' \n'  +lis[i] + ': '+ str(i+1)
                    duplicate_locations.append(locations)
                    dup_list.append(i)
                    dup_list.append(j)
    return duplicate_locations




#read the excel file of email addresses
df = pd.read_excel('C:/Users/jmajor/Desktop/ContactstoEmail-1.xlsx', header = None, index = None)

#extrqact the data wanted
x1 = df.iloc[0,0]
x2 = df.iloc[1,0]
x3 = df.iloc[2,1]

#clean up the data
combine = x1+x2+x3 #combine the data into a single list
combine_split = combine.split(';') #split the emails
emails1 = [i.lstrip("'").rstrip("'") for i in combine_split] #removes the quotation marks from the email strings
emails1 = [i.lstrip(" '") for i in emails1]
emails1 = [i.rstrip("'") for i in emails1]



#Pull data fromthe csv taken from the html file
df = pd.read_csv('C:/Users/jmajor/Desktop/emails.csv', header = None)

#Put data into a list
emails2 = list(df[0])

combined_emails = emails1 + emails2


#checks if there are any exact duplicates in the list
if (any(combined_emails.count(i) > 1 for i in combined_emails)) == False:
    print('No exact duplicates found\n')

else:
    print('Duplicates found: removing exact duplicates')
    len1 = len(combined_emails)
    combined_emails = list(remove_exact_duplicates(combined_emails))
    print('Removed {} duplicates\n'.format(len1-len(combined_emails)))

emails = pd.DataFrame(combined_emails)



start = time.time() #times how long it takes to find all the duplicates

duplicate_locations = pd.DataFrame(check_list(combined_emails))



duplicate_locations = (duplicate_locations)
duplicate_locations.to_csv(r'C:\users\jmajor\desktop\duplicate_locations.csv', index = None, header = None)
#emails.to_csv(r'C:\users\jmajor\desktop\combined_emails.csv', index = None, header = None)

print(time.time() - start)