'''This file contains the different setup functions used for the different motor maps''' 



'''this function contains the setup for the 2012 Nissan LEAF motor **updated** '''
#def setup():
#    '''Leaf motor'''
#    '''This function sets up the scale being used in the image.
#    these lists must be changed to match the individual image being used'''
#   
#    #import the effencicy map image
#    map_file = 'C:/Users/jmajor/Desktop/Updated motor map/leaf motor map.PNG'
#    map_image = mpimg.imread(map_file)
#    
#    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
#    speed_y = [193,338,484,631,776,922,1069,1214,1361,1505] #x-axis pixel locations corosponding to the RPM incriment locations
#    
#    torque_x = [50,100,150,200,250,300]  #the incriments of torque shown in the image
#    torque_y = [740,597,453,308,164,21] #the corosponding y-axis pixel locations
#    
#    speed_cof = np.polyfit(speed_x,speed_y,5) #fits the data to a third degree poly
#    torque_cof = np.polyfit(torque_x, torque_y, 5) #fits the data to a third degree poly
#    
#    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
#    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
#    
#    
#    
#    #import the percent bar image
#    percent_file = 'C:/Users/jmajor/Desktop/Updated motor map/leaf motor bar.PNG'
#    percent_bar_image = mpimg.imread(percent_file)
#    
#    
#    
#    percent_bar_loc = 30 #this is the column in which the color from the heat map will be compared
#    
#    percent_bar_x = [875,566,257,12] #this is the corrosponding pixel location
#    percent_bar_y = [70,80,90,100] #this is the increments of percentage shown in the image
#    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 5)
#    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
#    
#    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc

'''this is the modified leaf motor used to find the max torque'''
#def setup():
#    
#    '''This function sets up the scale being used in the image.
#    These lists must be changed to match the individual image being used'''
#   
#    #import the effencicy map image
#    map_file = 'Leaf_motor3.PNG'
#    map_image = mpimg.imread(map_file)
#    
#    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
#    speed_y = [89,179,269,359,448,538,629,718,808,898] #x-axis pixel locations corosponding to the RPM incriment locations
#    
#    torque_x = [0,50,100,150,200,250,300]  #the incriments of torque shown in the image
#    torque_y = [550,460,371,282,193,104,15] #the corosponding y-axis pixel locations
#    
#    speed_cof = np.polyfit(speed_x,speed_y,3) #fits the data to a third degree poly
#    torque_cof = np.polyfit(torque_x, torque_y, 3) #fits the data to a third degree poly
#    
#    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
#    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
#    
#    
#    
#    #import the percent bar image
#    percent_file = 'Leaf_motor_bar.PNG'
#    percent_bar_image = mpimg.imread(percent_file)
#    
#    
#    
#    percent_bar_loc = 15 #this is the column in which the color from the heat map will be compared
#    
#    percent_bar_x = [554,357,162,6] #this is the corrosponding pixel location
#    percent_bar_y = [70,80,90,100] #this is the increments of percentage shown in the image
#    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 3)
#    percent_fit = np.poly1d(percent_cof) #imput a pixle location and outputs a percent efficiency
#    
#    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc


    
'''this function contains the setup for the 2012 Nissan LEAF motor/inverter combine'''
#def setup():
#
#    '''This function sets up the scale being used in the image.
#    these lists must be changed to match the individual image being used'''
#   
#    #import the effencicy map image
#    map_file = 'Leaf_combine.PNG'
#    map_image = mpimg.imread(map_file)
#    
#    speed_x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000] #the incriments of RPM shown in the image
#    speed_y = [89, 179, 269, 359, 448, 538, 629, 718, 808, 898] #x-axis pixel locations corosponding to the RPM incriment locations
#    
#    torque_x = [0,50,100,150,200,250,300]  #the incriments of torque shown in the image
#    torque_y = [550,460,371,282,193,104,15] #the corosponding y-axis pixel locations
#    
#    speed_cof = np.polyfit(speed_x,speed_y,3) #fits the data to a third degree poly
#    torque_cof = np.polyfit(torque_x, torque_y, 3) #fits the data to a third degree poly
#    
#    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
#    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
#    
#    
#    
#    #import the percent bar image
#    percent_file = 'Leaf_combine_bar.PNG'
#    percent_bar_image = mpimg.imread(percent_file)
#    
#    
#    
#    percent_bar_loc = 15 #this is the column in which the color from the heat map will be compared
#    
#    percent_bar_x = [537,355,171,6] #this is the corrosponding pixel location
#    percent_bar_y = [70,80,90,100] #this is the increments of percentage shown in the image
#    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 3)
#    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
#    
#    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc


'''this is a random motor map i found online'''
#def setup():
#    
#    '''This function sets up the scale being used in the image.
#    these lists must be changed to match the individual image being used'''
#    
#    #import the effencicy map image
#    map_file = 'random.PNG'
#    map_image = mpimg.imread(map_file)
#    
#    speed_x = [0,1000,2000,3000,4000,5000,6000] #the incriments of RPM shown in the image
#    speed_y = [51,174,297,421,544,668,790] #x-axis pixel locations corosponding to the RPM incriment locations
#    
#    torque_x = [0,50,100,150,200,250,300]  #the incriments of torque shown in the image
#    torque_y = [341,290,238,167,135,84,32] #the corosponding y-axis pixel locations
#    
#    speed_cof = np.polyfit(speed_x,speed_y,3) #fits the data to a third degree poly
#    torque_cof = np.polyfit(torque_x, torque_y, 3) #fits the data to a third degree poly
#    
#    speed_fit = np.poly1d(speed_cof) #function to fit the data. Enter the RPM and get pixel location
#    torque_fit = np.poly1d(torque_cof) #function to fit the data. Enter the Torque and get pixel location
#    
#    
#    
#    #import the percent bar image
#    percent_file = 'random_bar.PNG'
#    percent_bar_image = mpimg.imread(percent_file)
#    
#    percent_bar_loc = 15 #this is the column in which the color from the heat map will be compared
#    
#    percent_bar_x = [298,217,135,54,16] #this is the corrosponding pixel location
#    percent_bar_y = [80,84,88,92,94] #this is the increments of percentage shown in the image
#    percent_cof = np.polyfit(percent_bar_x, percent_bar_y, 3)
#    percent_fit = np.poly1d(percent_cof) #imput a pixle location output a percent efficiency
#    
#    return speed_fit, torque_fit, percent_fit, map_image, percent_bar_image, percent_bar_loc


