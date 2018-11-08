'''
This script searches an HTML website file for specific email addresses
'''
#read the html file as a test file
with open('C:/Users/jmajor/Desktop/emails.htm', 'r') as f:
    html_text = f.read()

#list to hold all the email addresses
names = []

#split the test string
html_split = html_text.split('document.Person.submit();"><b>')

for html in html_split:
    for i in range(len(html)):
        if html[i] == '<':
            names.append(html[:i])
            break

emails = []
html_split = html_text.split('href="mailto:')


for html in html_split:
    for i in range(len(html)):
        if html[i] == '"':
            emails.append(html[:i])
            break

names = names[1:]
emails = emails[1:-1]

#'''
#This script searches an HTML website file for specific email addresses
#'''
##read the html file as a test file
#with open('C:/Users/jmajor/Desktop/emails.htm', 'r') as f:
#    html_text = f.read()
#
##list to hold all the email addresses
#emails = []
#
##split the test string
#html_split = html_text.split('href="mailto')
#
#
#for html in html_split:
#    for i in range(len(html)):
#        if html[i] == '"':
#            emails.append(html[1:i])
#            break
#
#
#
#
#
#import pandas as pd
#df = pd.DataFrame(emails)
##df.to_csv('emails.csv', index = None, header = None)
