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


#Function that takes the roadAccidentSet(Roads and respective number of Accidents on that road) and roadName (Road on which an accident occured) as input and returns updated roadAccidentSet and a set of accidents on unassignedRoads
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
#pass dictionary and roadAccidentSet and unassignedRoads one by one
def helper_for_apc(dictionaryOfClasses, array):
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
    
    dictionaryOfClasses = helper_for_apc(dictionaryOfClasses, roadAccidentsSet[1])
    dictionaryOfClasses = helper_for_apc(dictionaryOfClasses, unassignedRoads)
    
    return dictionaryOfClasses



#Function that calculates the traffic stats per road type
#Takes as input roadAccidentSet that has roads which are uniquely identified in the traffic statistics dataset
def road_stats(roadAccidentSet, stats):
    cols = roadAccidentSet.shape[1]
    
    #The traffic analysis dataset consists of the following coloumns that we'll consider
    #   FdPC – AADF for pedal cycles.
    #   Fd2WMV – AADF for two-wheeled motor vehicles.
    #   FdCar - AADF for Cars and Taxis.
    #   FdBUS – AADF for Buses and Coaches
    #   FdLGV – AADF for LGVs.
    #   FdHGV – AADF for all HGVs.
    #   FdAll_MV – AADF for all motor vehicles.
    #   count - Number of times the road appeared
    numZeros = 8
    shape = (numZeros, cols)
    
    zerosArray = np.zeros(shape)
    alteredRoadAccident = np.concatenate((roadAccidentSet, zerosArray), axis = 0).T
    
    for index, rows in stats.iterrows():
        road = rows['Road']

        pos, _ = np.where(alteredRoadAccident == road)          #pos[0] here contains the index at which the corresponding road is stored in alteredRoadAccident
        
        #Updating the alteredRoadAccident at pos[0] with values obtained from row
        alteredRoadAccident[pos[0], 2] = alteredRoadAccident[pos[0], 2] + rows['FdPC']
        alteredRoadAccident[pos[0], 3] = alteredRoadAccident[pos[0], 3] + rows['Fd2WMV']
        alteredRoadAccident[pos[0], 4] = alteredRoadAccident[pos[0], 4] + rows['FdCar']
        alteredRoadAccident[pos[0], 5] = alteredRoadAccident[pos[0], 5] + rows['FdBUS']
        alteredRoadAccident[pos[0], 6] = alteredRoadAccident[pos[0], 6] + rows['FdLGV']
        alteredRoadAccident[pos[0], 7] = alteredRoadAccident[pos[0], 7] + rows['FdHGV']
        alteredRoadAccident[pos[0], 8] = alteredRoadAccident[pos[0], 8] + rows['FdAll_MV']
        alteredRoadAccident[pos[0], 9] = alteredRoadAccident[pos[0], 9] + 1
        
    return alteredRoadAccident


#This function takes the alteredRoadAccident array and fetches the value of coount and divides all values in that row by count to obtain the average
def average_road_stats(alteredRoadAccident):
    for i in range(len(alteredRoadAccident)):
        count = alteredRoadAccident[i, 9]                   #Count obtained from that row
        if count != 0:
            alteredRoadAccident[i, 2:] = alteredRoadAccident[i, 2:]//count
            
    
    return alteredRoadAccident

    
    
    
    
    
    
#stats2017 = major_minor_stat_creation('F:\**\AADF-data-major-roads.csv', 'F:\**\AADF-data-minor-roads.csv', 2017)
#setOfRoads2017 = stats_set_creation(stats2017, 'Road')