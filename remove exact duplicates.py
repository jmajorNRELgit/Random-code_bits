# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 08:22:39 2018

@author: jmajor
"""

#function to remove exact duplicates
def remove_exact_duplicates(items):

    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)




x = [1,2,5,2,8,3,5,9,5]

y =list(remove_exact_duplicates(x)) #by using list you loose the performance advantage of using a generator in the function

print(y, '\n'+str(x))