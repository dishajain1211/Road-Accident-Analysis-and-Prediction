import pandas as pd
import numpy as np

#Functions that takes an year and 2 file paths: path1 and path2 for the major and minor road traffic statistics CSVs, then returns a dataframe comprising of statistics of 2017 from both the files
#Here:
#   year - year considered for accidents and statistics, example 2017
#   path1 - path of major roads file, example 'F:\a.csv'
#   path2 - path of minor roads file, example 'F:\b.csv'
def major_minor_stat_creation(path1, path2, year):
    statsMajorRoads = pd.read_csv(path1)                                                    #Traffic stats for major roads of GB (A)
    statsMinorRoads = pd.read_csv(path2)                                                    #Traffic stats for minor roads of GB (B, C, Unclassified)
    
    statsMajor = statsMajorRoads.loc[statsMajorRoads['AADFYear'] == year]                   #Traffic stats for year 2017 (Major roads)
    statsMinor = statsMinorRoads.loc[statsMinorRoads['AADFYear'] == year]                   #Traffic stats for year 2017 (Minor roads)
    
    stats = [statsMajor, statsMinor]
    stats = pd.concat(stats)                                                                #Combined stats of major and minor roads for 2017
    
    return stats


#Function that takes the dataframe of stats, creates a SET of roads with another coloumn giving the count of number of accidents on that road (Here initialized to 0s)
#Returns a 2D array such that:
#   roadsAccidentSet[0, 0] = 0 (Number of accidents on 0th index)
#   roadsAccidentSet[1, 0] = Axyz (The name of road at 0th index)
def stats_set_creation(stats, coloumnName):
    setOfRoads = pd.unique(stats[[coloumnName]].values.ravel('K'))                          #Finds all the unique values in coloumn 'coloumnName' and then unravels it (here, unique roads)
    numberOfRoads = setOfRoads.shape[0]                                                     #Number of unique roads
    zerosArray = np.zeros((numberOfRoads, 1))
    reshapedArray = setOfRoads.reshape((numberOfRoads, 1))                                  #From (numberOfRoads, ) to (numberOfRoads, 1)
    roadsAccidentsSet = np.concatenate((zerosArray, reshapedArray), axis=1).T               #Concatenating the zero array and the roads array
    return roadsAccidentsSet
    
    
    
    
    
    
    
    
    
    
stats2017 = major_minor_stat_creation('F:\Files\MajorProject\RAP-ter-master\Data\AADF-data-major-roads.csv', 'F:\Files\MajorProject\RAP-ter-master\Data\AADF-data-minor-roads.csv', 2017)
setOfRoads2017 = stats_set_creation(stats2017, 'Road')
