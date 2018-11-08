import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal


def forces_peak_detect(file_name,plot_show=True):
    '''
    This function is the main function for the peak detection.
    The first section does a quick pandas parse of the csv.
    The second section does a median filter subtraction,
    then a peak fitting. You have the option to graph 
    the result, otherwise the results will be returned 
    to you. It should run quite quickly.
    '''
    #Parse the csv
    forces = pd.read_csv(file_name)
    forces_y = list(forces['(N)'])
    forces_x = range(0,len(forces_y))
    #Apply a median filter
    smoothing = scipy.signal.medfilt(forces_y,205)
    #Subtract the median filter
    minus_smoothing = []
    for i in range(0,len(smoothing)):
        if forces_y[i]-smoothing[i] < 0.0:
            minus_smoothing.append(0.0)
        else:
            minus_smoothing.append(forces_y[i]-smoothing[i])
    #Run a peak detection on the result
    indexes = scipy.signal.find_peaks_cwt(minus_smoothing, np.arange(1, 200))
    #Find the two largest peaks in the data
    compare_li = []
    for i in indexes:
        compare_li.append([i,forces_y[i]])
    compare_li = sorted(compare_li, key = lambda x: x[1])
    highest_peaks = compare_li[len(compare_li)-2:len(compare_li)]
    new_indexes = [i[0] for i in highest_peaks]
    #Plotting, if necessary
    if plot_show == True:
        show_plot(forces_x,forces_y,new_indexes)
    else:
        pass
    #Return the result.
    return [round(i[1],9) for i in highest_peaks]

def show_plot(forces_x,forces_y,new_indexes):
    '''
    Shows the plot of the data (if necessary).
    '''
    plt.plot(forces_x,forces_y)
    plt.xlabel("Force Index")
    plt.ylabel("Force")
    plt.title('Force Peak Detection')
    for i in new_indexes:
        plt.scatter(forces_x[i],forces_y[i],marker='*',s=150,c='red')
    plt.show()


#Josh, all you need to input is the file name to the argument.
#Make sure that all of the files are in the same format or else
#things could break very easily.
highest_peaks = forces_peak_detect("Forces.csv",plot_show=True)
print(highest_peaks)