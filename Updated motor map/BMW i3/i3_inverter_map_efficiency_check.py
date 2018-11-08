'''This program is mainly used as a check for the lookup program. Use it to check the effeciency at a specific speed and torque'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


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
    
    high = l1 > l2-.01
    low = l1 < l2 +.01
    
    if all(high == True) and all(low == True):
        return True
    else:
        #print('No :(')
        pass

def setup():
    '''Leaf inverter'''
    '''This function sets up the scale being used in the image.
    these lists must be changed to match the individual image being used'''
   
    #import the effencicy map image
    map_file = 'C:/Users/jmajor/Desktop/Updated motor map/BMW i3/i3_Inverter.png'
    map_image = mpimg.imread(map_file)
    #plt.imshow(map_image)
    
    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000, 11000] #the incriments of RPM shown in the image
    speed_y = [174,302,431,561,688,818,947,1075,1204,1333, 1461] #x-axis pixel locations corosponding to the RPM incriment locations
    
    torque_x = [50,100,150,200,250]  #the incriments of torque shown in the image
    torque_y = [733,554,375,195,18] #the corosponding y-axis pixel locations
    
    speed_cof = np.polyfit(speed_x,speed_y,5) #fits the data to a third degree poly
    torque_cof = np.polyfit(torque_x, torque_y, 5) #fits the data to a third degree poly
    
    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
    
    
    
    #import the percent bar image
    percent_file = 'C:/Users/jmajor/Desktop/Updated motor map/BMW i3/i3_Inverter_bar.png'
    percent_bar_image = mpimg.imread(percent_file)
    #plt.imshow(percent_bar_image)
    
    
    percent_bar_loc = 25 #this is the column in which the color from the heat map will be compared
    
    percent_bar_x = [754,599,444,288,132,12] #this is the corrosponding pixel location
    percent_bar_y = [75,80,85,90,95,100] #this is the increments of percentage shown in the image
    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 5)
    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
    
    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc



def percent_efficiency(speed, torque):
    '''this function simply outputs the percent efficiency as an integer. If the program is run as __main__
    it will also display the images with a blue dot over the pixels used for the effencicy calculation'''
    
    #run the setup function
    speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc = setup()
    
    
    speed = int(speed_fit(speed))
    torque = int(torque_fit(torque))
    
    RGB_numbers = raw(map_image[torque][speed]) #map_image[row][column]
    
    
    stop = 0 #stops the loop if the pixel location is moved more than 20 times
    go = 0 #used to stop the while loop once the proper percent is found
    
    while stop < 20 and go == 0:
        
        
        for j in range(len(percent_bar_image)):
            if check(raw(percent_bar_image[j][percent_bar_loc]), RGB_numbers) == True and list(RGB_numbers) != [0.0, 0.0, 0.0, 1.0]:
                percent = int(percent_fit(j))
                go = 1
                break
            elif j == len(percent_bar_image)-1:
                speed += 1
                torque += 1
                stop +=1
                RGB_numbers = raw(map_image[torque][speed]) #map_image[row][column]
                
        if stop == 20:
            raise Exception('\n\nNo pixel values were matched. Try increasing the values in the check() function or the percent_bar_loc variable.\n\n')
    
    #if run as the main program this plots the images for use in troubleshooting           
    if __name__ == '__main__':
        #plotting the motor image
        plt.subplot(1,2,1)
        plt.imshow(map_image)
        plt.title('Efficiency Map')
        plt.ylabel('Torque')
        plt.xlabel('Speed(RPM)')
        plt.scatter([speed], [torque], label = 'RGB: {0}'.format(raw(map_image[torque][speed])))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
        
        #plotting the percent bar image
        plt.subplot(1,2,2)
        plt.imshow(percent_bar_image)
        plt.title('Efficiency percent bar')
        plt.scatter(percent_bar_loc,j, label = 'RGB: {0}'.format(raw(percent_bar_image[j][percent_bar_loc])))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
        
        plt.tight_layout()
        plt.show()
    
    return percent

if __name__ == '__main__':
    speed = int(input('Plese enter the speed(RPM): '))
    torque = int(input('Please enter the torque: '))
    print(str(percent_efficiency(speed, torque)) + '%')


#max torque for speed lookup
    
#pandas lookup for efficiency

#fill with a negitive inter
#pandas fill na for padding