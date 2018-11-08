'''monday, 3-12-18. this is the trial program to make a lookup table for the efficiency map. It has the more efficient percent_efficiency() function with the condensed efficiency bar RGB data'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import time

def raw(array):
    '''Function to change the RGB data string into a list of floats.
       Input is the rgb data in a 3d array (eg. array[#][#])'''
       
    raw = list(str(array).strip('[').strip(']').split())
    raw =  list(map(float, raw))
    raw = [ round(elem, 3) for elem in raw ]
    return np.array(raw)


def check(l1,l2):
    '''This function is used if the colors on the percent bar are not an exact match for the heat map. It returns 
    true if the colors are close. The closer the colors match, the small the high/low numbers can be to improve accuracy'''
    
    high = l1 > l2-.08
    low = l1 < l2 +.08
    
    if all(high == True) and all(low == True):
        return True
    else:
        #print('No :(')
        pass
    
def setup():
    '''i3 motor'''
    '''This function sets up the scale being used in the image.
    these lists must be changed to match the individual image being used'''
   
    #import the effencicy map image
    map_file = 'i3_Motor_copy.png'
    map_image = mpimg.imread(map_file)
    
    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000, 11000] #the incriments of RPM shown in the image
    speed_y = [172,300,428,556,686,814,942,1071,1199,1327,1455] #x-axis pixel locations corosponding to the RPM incriment locations
    
    torque_x = [50,100,150,200,250]  #the incriments of torque shown in the image
    torque_y = [735,556,377,197,19] #the corosponding y-axis pixel locations
    
    speed_cof = np.polyfit(speed_x,speed_y,4) #fits the data to a third degree poly
    torque_cof = np.polyfit(torque_x, torque_y, 4) #fits the data to a third degree poly
    
    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
    
    
    
    #import the percent bar image
    percent_file = 'i3_Motor_bar.png'
    percent_bar_image = mpimg.imread(percent_file)
    
    
    
    percent_bar_loc = 25 #this is the column in which the color from the heat map will be compared
    
    percent_bar_x = [842,738,428,282,17] #this is the corrosponding pixel location
    percent_bar_y = [78,80,86,90,94] #this is the increments of percentage shown in the image
    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 5)
    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
    
    
    #this puts the rgb data and percent efficiency into a condensed list
    condenced_bar_full = []
    
    '''Change these'''
    for i in range(17, 873): #the range is the pixel locations within the color bar itself (no white or black...)
        condenced_bar_full.append([percent_bar_image[i][25], percent_fit(i), i]) #the column number is within the color bar
    
    #This condenses the list even further by removing duplicate RGB values
    condensed_bar = []
    for i in range(len(condenced_bar_full)-1):
      if not (condenced_bar_full[i][0] == condenced_bar_full[i+1][0]).all():
          condensed_bar.append(condenced_bar_full[i])
    
    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar

def percent_efficiency(speed, torque, speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar):
    '''this function simply outputs the percent efficiency as an integer.'''
    
    #run the setup function
   
    
    
    speed = int(speed_fit(speed))
    torque = int(torque_fit(torque))
    
    RGB_numbers = raw(map_image[torque][speed]) #map_image[row][column]
    
    
    stop = 0 #stops the loop if the pixel location is moved more than 20 times
    go = 0 #used to stop the while loop once the proper percent is found
    
    while stop < 20 and go == 0:
        
        
        for j in range(len(condensed_bar)):
            
            white = np.array([1,1,1,1]) #RGBA values for white
            
            if (RGB_numbers == white).all():
                percent = np.nan
                go = 1
                break
            
            elif check(raw(condensed_bar[j][0]), RGB_numbers) == True:
                percent = round(condensed_bar[j][1],3)
                go = 1
                break
            elif j == len(condensed_bar)-1:
                speed += 1
                torque += 1
                stop +=1
                RGB_numbers = raw(map_image[torque][speed]) #map_image[row][column]
                
            if stop == 20:
                percent = np.nan
               
    return percent     

def time_funct(function, speed, torque):
    start = time.time()
    function(speed,torque)
    end = time.time() - start
    return end

   
speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar = setup()

      
#df = pd.read_csv('i3 Max torque lookup table.csv', index_col=0) #this is the csv file made from the max_torque program. it's just for reference


torque_range = np.arange(0, 246) #the max torque value

speed_range = np.arange(512,11476,5) #the RPM values from the Max torque list

lookup_table = pd.DataFrame(np.nan, index = torque_range, columns = speed_range) #the pandas dataframe that will be the lookup table. initially filled with nan's



b = lookup_table.index.values.tolist() #these are the speed values that will be in the lookup table
a = list(lookup_table.columns.values) #these are the torque values that will be in the lookup table
a = list(map(int,a))

start = time.time()
for i in range(0,2193): #this is the number of columns in the lookup_table (or however many you want to try)
    print(i)
    for j in range(0,246): #this is the number of rows in the lookup table
        lookup_table.loc[b[j]][a[i]] = percent_efficiency(a[i], b[j], speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar)


end = time.time() - start


inverted = lookup_table.reindex(index=lookup_table.index[::-1])
