# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:46:10 2019

@author: ADITYA
"""

import pandas as pd
import numpy as np

from helperFunctions_Preprocessing import *


FILEPATH_ACC = r'F:\Files\MajorProject\RAP-ter\Data\Acc.csv'
FEATURES_ACC = ['Accident_Index', 'Number_of_Vehicles', 'Date', 'Day_of_Week', 'Time', '1st_Road_Class', '1st_Road_Number', 'Road_Type', 'Light_Conditions', 'Weather_Conditions', 'Road_Surface_Conditions']

FILEPATH_VEH = r'F:\Files\MajorProject\RAP-ter\Data\Veh.csv'
FEATURES_VEH = ['Accident_Index', 'Vehicle_Type']


def stats_creator(filePath, coloumnsToSelect):
    dataFrame = pd.read_csv(filePath)
    stats = dataFrame[coloumnsToSelect]
    
    return stats


def array_veh_creator(numberOfVehicles, statsVeh):
    
    vehicles = []
    sumVal = 0
    
    for num in numVeh:
        temp = []
        for i in range(num):
            temp.append(vehType[sumVal + i])
        
        sumVal = sumVal + num
        vehicles.append(temp)

    return vehicles


def data_frame_creator(arr):
    arrNP = np.array(arr)
    arrNP = arrNP.reshape(-1, 1)
    arrayDF = pd.DataFrame(arrNP)
    
    return arrayDF


def set_creator(dataframe, skipCols):
    setList = []
    
    for i in range(dataframe.shape[1]):
        if(i in skipCols):
            continue
        else:
            temp = set(dataframe.iloc[:, i])
            setList.append(temp)
        
    return setList


def combinator(setList):
    
    combination = []
    for i, firstOptionList in enumerate(setList):
        for firstOption in firstOptionList:
            for secondOptionList in setList[i+1:]:
                for secondOption in secondOptionList:
                    temp = []
                    temp.append(firstOption)
                    temp.append(secondOption)
                    combination.append(temp)
    
    return combination


#statsAcc = stats_creator(FILEPATH_ACC, FEATURES_ACC)
#statsVeh = stats_creator(FILEPATH_VEH, FEATURES_VEH)
#
#numVeh = statsAcc.iloc[:, 1]
#vehType = statsVeh.iloc[:, 1]
#vehicles = array_veh_creator(numVeh, vehType)
#
#vehiclesDF = data_frame_creator(vehicles)
#
#stats = pd.concat((statsAcc, vehiclesDF), axis=1)
#
#
#columnDate = 2
#columnTime = 4
#columnSurfaceVal = 10
#
#modeForTime, modeForSurface = finding_modes(statsAcc, columnTime, columnSurfaceVal)
#   
#stats = time_and_date_modifications(statsAcc, modeForTime, columnDate, columnTime)
#statsNew = pd.concat((stats, vehiclesDF), axis = 1)

#statsNew.to_csv('out.csv')
statsNew = pd.read_csv(r'F:\Files\MajorProject\RAP-ter\Code\out.csv')
statsNew = statsNew.iloc[:, 1:]

statsSleak = statsNew.drop(['Accident_Index', 'Number_of_Vehicles'], axis=1)
statsSleak = statsSleak.drop(['1st_Road_Number'], axis=1)
statsSetCombinator = statsSleak.iloc[:, :-1]

statsSlice = statsSleak.iloc[:100, :]
statsSliceDOW = statsSlice.iloc[:, 1]

setList = set_creator(statsSetCombinator, [])

combination = combinator(setList)