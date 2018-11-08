# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 08:52:02 2018

@author: jmajor
"""
import pandas as pd
from difflib import SequenceMatcher

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
#emails1 = [i.lstrip("'").rstrip("'") for i in combine_split] #removes the quotation marks from the email strings
#emails1 = [i.lstrip(" '") for i in emails1]
#emails1 = [i.rstrip("'") for i in emails1]

names_emails = [x.split(' ') for x in combine_split]

emails = [x[-1] for x in names_emails]
emails = [i.lstrip("'").rstrip("'") for i in emails]
emails = [i.lstrip(" '").rstrip("'") for i in emails]
emails = [i.lstrip("<").rstrip('>') for i in emails]
emails = [i.lstrip("(").rstrip(')') for i in emails]

emails = list(remove_exact_duplicates(emails)) #removes duplicates

df2 = pd.read_csv('C:/Users/jmajor/Desktop/all_emails.csv', header = None)

master_list = list(df2.iloc[:,0])
master_list = list(remove_exact_duplicates(master_list))

locat = check_list(master_list)
locat = pd.DataFrame(locat)

master_list = pd.DataFrame(master_list)
master_list.to_csv(r'C:/Users/jmajor/Desktop/master_email_list.csv', index = None, header = None)
#duplicate_locations = list(check_list(emails))
#emails = pd.DataFrame(emails, index = None)
#emails.to_csv(r'C:\users\jmajor\desktop\excel_emails.csv', index = None, header = None)
