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


#Function that takes the roadAccidentSet(Roads and respective number of Accidents on that road) and roadName (Road on which an accident occured) as input and returns updated roadAccidentSet
def accident_flows(roadAccidentsSet, roadName):
    unassignedRoads = []
    for road in roadName:
        if road in roadAccidentsSet:
            tempLocation = np.where(roadAccidentsSet == road)                               #The location where the road is in roadAccidentSet
            indexToBeInc = tempLocation[1][0]                                               #The index of that location that need to be incremented
            roadAccidentsSet[0][indexToBeInc] = roadAccidentsSet[0][indexToBeInc] + 1       #Incrementing the count on that index
        else:
            unassignedRoads.append(road)
            
#    unassignedRoads = np.array(unassignedRoads)
    return roadAccidentsSet, unassignedRoads



#Helper function for accidents_per_classes() to calculate the number of accidents on road types
def helper_for_acp(dictionaryOfClasses, array):
    for road in array:
        if road[-1] == ')':
            dictionaryOfClasses['A(M)'] = dictionaryOfClasses['A(M)'] + 1
        elif road[0] == 'A':
            dictionaryOfClasses['A'] = dictionaryOfClasses['A'] + 1
        elif road[0] == 'B':
            dictionaryOfClasses['B'] = dictionaryOfClasses['B'] + 1
        elif road[0] == 'C':
            dictionaryOfClasses['C'] = dictionaryOfClasses['C'] + 1
        elif road[0] == 'M':
            dictionaryOfClasses['M'] = dictionaryOfClasses['M'] + 1
        else:
            dictionaryOfClasses['U'] = dictionaryOfClasses['U'] + 1
    
    return dictionaryOfClasses
    
    
#Function to calculate the total accidents in the road cateogories A(M), A, B, C, U, M
def accidents_per_class(roadAccidentsSet, unassignedRoads):
    dictionaryOfClasses = {'A(M)': 0, 'A':0, 'B':0, 'C':0, 'M':0, 'U':0}                    #Dictionary comprising of the count of all classes of roads
    
    dictionaryOfClasses = helper_for_acp(dictionaryOfClasses, roadAccidentsSet[1])
    dictionaryOfClasses = helper_for_acp(dictionaryOfClasses, unassignedRoads)
    
    return dictionaryOfClasses




#Function that 
#stats2017 = major_minor_stat_creation('F:\**\AADF-data-major-roads.csv', 'F:\**\AADF-data-minor-roads.csv', 2017)
#setOfRoads2017 = stats_set_creation(stats2017, 'Road')