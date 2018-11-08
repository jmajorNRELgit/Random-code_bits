import numpy as np

a = np.arange(-15,15).reshape(5,6) **2

print(a.min())

print(a.argmin()) #works if flat

print(np.unravel_index(a.argmin(), (5,6)))

print(np.where(a = a.min()))  #This should work


list(zip(*np.where(a == a.min()))) #this makes it pretty


'''
find the location of a specific value in a np.array
'''