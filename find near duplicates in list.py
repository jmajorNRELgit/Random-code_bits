# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:49:43 2018

@author: jmajor
"""
#Imports
from difflib import SequenceMatcher

import time
start = time.time()





#Put data into a list
x = "michael.barako@northropgrummannext.net","michael.barako@northrupgrummannext.net","daijiangnan@hust.edu.cn","daijiangnan@mail.hust.edu.cn"

#checks if there are any exact duplicates in the list
if (any(x.count(i) > 1 for i in x)) == False:
    print('No exact duplicates found\n')

#List to hold duplicate's location. Also used to avoid catching them twice
duplicate_locations = []



#Function to find nrear but not perfect matches
def check_list(lis):
    for j in range(len(lis)):
        for i in range(len(lis)):
            if i != j and i not in duplicate_locations and j not in duplicate_locations:
                if SequenceMatcher(None, lis[j],lis[i]).quick_ratio() > .9:
                    print(lis[j],
                          '\n'+str(lis[i]),
                          '\nMatch: ' + str(SequenceMatcher(None, lis[j],lis[i]).ratio()),
                          '\nlocation: ' + str(j+1),'\n' )
                    duplicate_locations.append(j)

check_list(x)

print(time.time() - start)


