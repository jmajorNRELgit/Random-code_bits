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
    
    high = l1 > l2-.09
    low = l1 < l2 +.09
    
    if all(high == True) and all(low == True):
        return True
    else:
        #print('No :(')
        pass
    
def setup():
    
    '''Leaf motor'''
    '''This function sets up the scale being used in the image.
    these lists must be changed to match the individual image being used'''
   
    #import the effencicy map image
    map_file = 'C:/Users/jmajor/Desktop/Updated motor map/leaf motor map.PNG'
    map_image = mpimg.imread(map_file)
    
    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
    speed_y = [193,338,484,631,776,922,1069,1214,1361,1505] #x-axis pixel locations corosponding to the RPM incriment locations
    
    torque_x = [50,100,150,200,250,300]  #the incriments of torque shown in the image
    torque_y = [740,597,453,308,164,21] #the corosponding y-axis pixel locations
    
    speed_cof = np.polyfit(speed_x,speed_y,5) #fits the data to a third degree poly
    torque_cof = np.polyfit(torque_x, torque_y, 5) #fits the data to a third degree poly
    
    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
    
    
    
    #import the percent bar image
    percent_file = 'C:/Users/jmajor/Desktop/Updated motor map/leaf motor bar.PNG'
    percent_bar_image = mpimg.imread(percent_file)
    
    
    
    percent_bar_loc = 30 #this is the column in which the color from the heat map will be compared
    
    percent_bar_x = [875,566,257,12] #this is the corrosponding pixel location
    percent_bar_y = [70,80,90,100] #this is the increments of percentage shown in the image
    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 5)
    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
    
    
    #this puts the rgb data and percent efficiency into a condensed list
    condenced_bar_full = []
    
    for i in range(12, 875): #the range is the pixel locations within the color bar itself (no white or black...)
        condenced_bar_full.append([percent_bar_image[i][25], percent_fit(i), i]) #the column number is within the color bar
    
    #This condenses the list even further by removing duplicate RGB values
    condensed_bar = []
    for i in range(len(condenced_bar_full)-1):
      if not (condenced_bar_full[i][0] == condenced_bar_full[i+1][0]).all():
          condensed_bar.append(condenced_bar_full[i])
    
    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar

def percent_efficiency(speed, torque, speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar):
    '''this function simply outputs the percent efficiency as an integer. If the program is run as __main__
    it will also display the images with a blue dot over the pixels used for the effencicy calculation'''
    
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
                #raise Exception('\n\nNo pixel values were matched. Try increasing the values in the check() function or the percent_bar_loc variable.\n\n')
        #if run as the main program this plots the images for use in troubleshooting           
#        if __name__ == '__main__':
#            #plotting the motor image
#            plt.subplot(1,2,1)
#            plt.imshow(map_image)
#            plt.title('Efficiency Map')
#            plt.ylabel('Torque')
#            plt.xlabel('Speed(RPM)')
#            plt.scatter([speed], [torque], label = 'RGB: {0}'.format(raw(map_image[torque][speed])))
#            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
#            
#            #plotting the percent bar image
#            plt.subplot(1,2,2)
#            plt.imshow(percent_bar_image)
#            plt.title('Efficiency percent bar')
#            plt.scatter(percent_bar_loc,condensed_bar[j][2], label = 'RGB: {0}'.format(raw(percent_bar_image[j][percent_bar_loc])))
#            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
#            
#            plt.tight_layout()
#            plt.show()            
    return percent     

def time_funct(function, speed, torque):
    start = time.time()
    function(speed,torque)
    end = time.time() - start
    return end

   
speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar = setup()

      
#df = pd.read_csv('i3 Max torque lookup table.csv', index_col=0) #this is the csv file made from the max_torque program. it's just for reference


torque_range = np.arange(3, 276) #the max torque value

speed_range = np.arange(500,10000,5) #the RPM values from the Max torque list

lookup_table = pd.DataFrame(np.nan, index = torque_range, columns = speed_range) #the pandas dataframe that will be the lookup table. initially filled with nan's



b = lookup_table.index.values.tolist() #these are the speed values that will be in the lookup table
a = list(lookup_table.columns.values) #these are the torque values that will be in the lookup table
a = list(map(int,a))

start = time.time()
for i in range(0,1900): #this is the number of columns in the lookup_table (or however many you want to try)
    print(i)
    for j in range(0,273): #this is the number of rows in the lookup table
        lookup_table.loc[b[j]][a[i]] = percent_efficiency(a[i], b[j], speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc, condensed_bar)


end = time.time() - start


inverted = lookup_table.reindex(index=lookup_table.index[::-1])
