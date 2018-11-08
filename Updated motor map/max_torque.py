# -*- coding: utf-8 -*-
"""

Max Torque

Created on Mon Mar  5 10:32:31 2018

@author: jmajor
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd



def max_torque():
    '''this function starts at the bottom row of a column of pixles and moves upwards looking for a specific color(the max torque line color. Once it matches the color it saves the pixel location and moves over one column to the right'''
    color = list(map_image[30][121]) #max torque line color. this can reference an existing pixel or be a list of known RGB values
    torque_max_pix = [] #variable for the Y-axis location of the pixel
    speed_pix = [] #variable for the X-axis location of the pixel
    for j in range(120,1507): #range is the number of columns in the image map area (area of interest) 119,1505
        for i in range(820,37,-1): #range is the number of rows. Starts at the bottom and moves up
            pix = map_image[i][j]
            if list(pix) == color:
                torque_max_pix.append(i)
                speed_pix.append(j)
                break
    return speed_pix,torque_max_pix




def setup():
    '''Leaf inverter'''
    '''This function sets up the scale being used in the image.
    these lists must be changed to match the individual image being used'''
   
    #import the effencicy map image
    map_file = 'Leaf inverter map.PNG'
    map_image = mpimg.imread(map_file)
    
    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
    speed_y = [194,339,485,632,778,922,1071,1216,1363,1507] #x-axis pixel locations corosponding to the RPM incriment locations
    
    torque_x = [50,100,150,200,250]  #the incriments of torque shown in the image
    torque_y = [699,555,410,265,121] #the corosponding y-axis pixel locations
    
    speed_cof = np.polyfit(speed_x,speed_y,5) #fits the data to a third degree poly
    torque_cof = np.polyfit(torque_x, torque_y, 5) #fits the data to a third degree poly
    
    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
    
    
    
  
    
    return speed_fit, torque_fit, map_image



def lookup(speed_pix,torque_max_pix):
    '''this function takes in two list of the pixel location and outputs a lookup table for the max torque value at a given RPM'''
    
    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
    speed_y = [194,339,485,632,778,922,1071,1216,1363,1507] #x-axis pixel locations corosponding to the RPM incriment locations
    
    torque_x = [50,100,150,200,250]  #the incriments of torque shown in the image
    torque_y = [699,555,410,265,121] 
    
    #these two are backwards from the setup() function so that you input a pixel location and it outputs a speed or torque value
    speed_cof = np.polyfit(speed_y,speed_x,4) 
    torque_cof = np.polyfit(torque_y,torque_x,  4) 
    
    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the pixel location and get RPM
    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the pixel location and get Torque
    
    speed = [round(speed_fit(x)) for x in speed_pix]
    torque_max = [torque_fit(x) for x in torque_max_pix]
    
    lis = list(zip(speed,torque_max))
    
    lookup = pd.DataFrame(lis, columns = ['speed(RPM)','max_torque'])
    
    return lookup
    
    

#runs the setup function.
speed_fit, torque_fit, map_image = setup()

#gets the pixel pixle
speed_pix, torque_max_pix = max_torque()

#gives a buffer of 5 pixels
torque_max_pix = [x + 2 for x in torque_max_pix]

#creates the lookup table
lookup_table = lookup(speed_pix, torque_max_pix)

#plots the original image and then the location of the max torque for each given RPM
plt.imshow(map_image)
plt.plot(speed_fit(lookup_table['speed(RPM)']), torque_fit(lookup_table['max_torque']), 'go')  
plt.show()