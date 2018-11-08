# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:03:41 2018

@author: jmajor
"""

import pandas as pd

df = pd.read_csv('C:/Users/jmajor/Desktop/combined_emails.csv', header = None)

emails = list(df.iloc[:,0])

i = 0
for email in emails:
    if len(email.split(' ')) > 1:
        email = email.split(' ')[-1].lstrip('<').lstrip('(').rstrip('>').rstrip(')')
        print(email)
        emails[i] = email
    i +=1

print(i)

#function to remove exact duplicates
def remove_exact_duplicates(items):
    seen = set()
    for item in items:
        if item not in seen:
            print(item)
            yield item
            seen.add(item)

remove_exact_duplicates(emails)

'''This section sorted out the names as well as the email addresses'''

#'''
#This script searches an HTML website file for specific email addresses
#'''
##read the html file as a test file
#with open('C:/Users/jmajor/Desktop/emails.htm', 'r') as f:
#    html_text = f.read()
#
##list to hold all the email addresses
#names = []
#
##split the test string
#html_split = html_text.split('document.Person.submit();"><b>')
#
#for html in html_split:
#    for i in range(len(html)):
#        if html[i] == '<':
#            names.append(html[:i])
#            break
#
#emails = []
#html_split = html_text.split('href="mailto:')
#
#
#for html in html_split:
#    for i in range(len(html)):
#        if html[i] == '"':
#            emails.append(html[:i])
#            break
#
#names = names[1:]
#emails = emails[1:-1]