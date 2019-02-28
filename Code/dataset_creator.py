# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:02:28 2019

@author: ADITYA
"""

import pandas as pd
import numpy as np


NUM_ROWS = 130000


def create_road_class_list():
    '''
        Function that creates a list based on the road-class-traffic distribution
        
        Returns:
            roadClassList - List containing data
    '''

    '''
        TRANSPORT STATISTICS GREAT BRITAIN : 2017 (Page-21)
        
        Motorway - 21%; Label - 1, 2
        Urban 'A' Roads - 15%; Label - 3
        Rural 'A' Roads - 29%; Label - 3
        Urban Minor Roads - 21%; Label - 4
        Rural Minor Roads - 14%; Label - 5
        
    '''    
    roadClassList = []
    
    for i in range(27300):
        roadClassList.append(1)
    
    for i in range(57200):
        roadClassList.append(3)
    
    for i in range(27300):
        roadClassList.append(4)
        
    for i in range(18200):
        roadClassList.append(5)

    '''
        Distribution:
            0:27299 - 1
            27300:84499 - 3
            84500:111799 - 4
            111799:129999 - 5
    '''
    
    return roadClassList


def monthPercentage():
    listOfValues = [87.7, 91.6, 97.0, 99.6, 101.6, 104.6, 105.2, 105.5, 105.0, 103.7, 100.8, 97.4]
    sumOfValues = sum(listOfValues)
    
    retList = []
    for i in listOfValues:
        val = (i/sumOfValues)*100
        retList.append(val)
        
    return retList


def dayPercentage():
    listOfValues = [80.4, 102.9, 104.1, 105.9, 108.1 ,111.7, 87.3]
    sumOfValues = sum(listOfValues)

    retList = []
    for i in listOfValues:
        val = (i/sumOfValues)*100
        retList.append(val)
    
    return retList


def rangeCreator(difference, retList, toAdd):
    initialVal = 0
    finalRetList = []
    for i in retList:
        val = initialVal + int(difference*i/100)
#        print('C',initialVal+toAdd, ':', 'C',val+toAdd, sep='')
        temp = [initialVal+toAdd, val+toAdd]
        finalRetList.append(temp)
        initialVal = val+1
    return finalRetList
    

def dayFrameCreator(retListDays, NUM_ROWS):
    dayDF = []
    for val, i in enumerate(retListDays):
        number = int(i*NUM_ROWS/100)
        for j in range(number):
            dayDF.append(val+1)
    
    dayDF = pd.DataFrame(dayDF)
    
    #Shuffle
    dayDFShuffled = dayDF.sample(frac = 1).reset_index(drop=True)
    
    return dayDFShuffled

    
def tester():
    alpha = pd.read_csv(r'F:\Files\MajorProject\RAP-ter\Data\GeneratedOne.csv')
    
    return alpha




def timePercentageListCreator():
    oneList = [15.6, 15.3,	16.4,	17.2,	19.2,	25.0,	27.0, 10.2,	11.0,	11.6,	12.0,	13.5,	17.0,	17.6, 8.6,	9.9,	10.2,	10.6,	11.6,	13.2,	12.2, 11.0,	11.6,	11.8,	12.3,	12.9,	12.7,	10.6, 21.4,	19.2,	19.2,	19.6,	19.6,	15.0,	10.9, 54.5,	48.6,	47.7,	47.6,	45.4,	24.7,	15.6]
    twoList = [121.2	,117.8,	115.9,	115.1,	106.0,	42.1,	25.3, 184.1,	185.9,	184.8,	183.5,	170.1,	66.2,	38.0, 183.1,	186.3,	186.0,	185.7,	172.9,	97.9,	56.0, 150.1,	152.7,	153.6	,153.8,	147.7,	129.1,	92.6, 143.7,	138.9,	140.6,	142.9,	151.6,	155.7,	129.5,146.6,	139.0,	141.9,	145.5,	162.4,	169.5,	151.7]
    threeList = [147.3,	142.1,	145.2,	149.1,	171.2,	169.4,	159.0, 148.4,	145.2,	148.5,	152.8,	176.7,	161.6,	155.0, 154.6,	154.4,	158.6,	162.8,	184.1,	151.7,	150.5, 168.1,	171.7,	176.1,	179.8,	195.0,	144.5,	150.7, 191.4,	197.4,	199.8,	201.2,	202.9,	142.9,	151.9, 192.3,	198.7,	200.8,	201.5,	194.4,	138.3,	140.3]
    fourList = [146.8, 155.5, 159.3,	162.9,	160.6,	118.8,	122.6, 97.2,	104.1,	108.5,	116.1,	122.4,91.6,	102.6, 68.6,	72.3,	76.2,	83.3,	88.5,	67.7,	80.8, 51.4,	55.1,57.6,	62.2,	64.6,	52.6,	58.6, 37.4,	42.0,	43.6,	46.4,	50.8,	45.6,	39.8, 23.6,	26.1,	27.5,	30.0,	36.8,	37.4,	25.6]
    
    listTime = [sum(oneList), sum(twoList), sum(threeList), sum(fourList)]
    
    sumTimeList = sum(listTime)
    valsTimeList = []
    
    for i in listTime:
        tempVal = i/sumTimeList*100
        valsTimeList.append(tempVal)
        
    return valsTimeList


def time_and_light_conditions_frame_creator(valsTimeList):
    timeLightConditionDF = []
    for val, i in enumerate(valsTimeList):
        number = int(i*NUM_ROWS/100)
        for j in range(number):
            timeLightConditionDF.append(val+1)
    
    timeLightConditionDF = pd.DataFrame(timeLightConditionDF)
    
    #Shuffle
    timeLightConditionDFShuffled = timeLightConditionDF.sample(frac = 1).reset_index(drop=True)
    
    return timeLightConditionDFShuffled



def weather_updater(numRange, start):
    finalRetList = rangeCreator(numRange, retList, start)
    weatherList = [[0.69, 0.22, 0.09], [0.61, 0.25, 0.14], [0.70, 0.24, 0.06], [0.83, 0.13, 0.04], [0.87, 0.13, 0.0], [0.8, 0.2, 0.0], [0.78, 0.22, 0.0], [0.78, 0.22, 0.0], [0.7, 0.3, 0.0], [0.81, 0.19, 0.0], [0.753, 0.233, 0.023], [0.70, 0.24, 0.06]]
    
    mainListForWeather = []
    
    for i in range(12):
        retListVal = finalRetList[i]
        weatherListVal = weatherList[i]
        
        difference = retListVal[1] - retListVal[0]
        
        for val, perc in enumerate(weatherListVal):
            tempVal = int(difference*perc)
            for j in range(tempVal):
                mainListForWeather.append(val + 1)
    
    return mainListForWeather
            

def weather_frame_creator():
    mainListForWeatherOne = weather_updater(27300, 0)
    mainListForWeatherTwo = weather_updater(57200, 27300)
    mainListForWeatherThree = weather_updater(27299, 84501)
    mainListForWeatherFour = weather_updater(18200, 111801)
    
    DFone = pd.DataFrame(mainListForWeatherOne)
    DFtwo = pd.DataFrame(mainListForWeatherTwo)
    DFthree = pd.DataFrame(mainListForWeatherThree)
    DFfour = pd.DataFrame(mainListForWeatherFour)
    
    frameset = [DFone, DFtwo, DFthree, DFfour]
    weatherDF = pd.concat(frameset)
    
    return weatherDF


def vehicle_dataframe_creator():
    distribution = [0.78, 0.15, 0.05, 0.02]
    distributionRows = []
    for i in distribution:
        temp = int(i*NUM_ROWS)
        distributionRows.append(temp)
    
    vehicleDF = []
    for val, i in enumerate(distributionRows):
        for j in range(i):
            vehicleDF.append(val+1)
            
    return vehicleDF
        

retList = monthPercentage()
retListDays = dayPercentage()
valsTimeList = timePercentageListCreator()

dayDF = dayFrameCreator(retListDays, NUM_ROWS)
dayDFSaved = dayDF
timeLightDF = time_and_light_conditions_frame_creator(valsTimeList)


weatherDF = weather_frame_creator()

frames = [dayDFSaved, timeLightDF]
concatenated = pd.concat(frames, axis = 1)


concatenated.to_csv('concatenated.csv')
weatherDF.to_csv('weather.csv')



vehicleDF = vehicle_dataframe_creator()
vehicleDF = pd.DataFrame(vehicleDF)
vehicleDFShuffled = vehicleDF.sample(frac = 1).reset_index(drop=True)

vehicleDFShuffled.to_csv('vehicleDF.csv')

#rangeCreator(57200, retList, 27300)
#rangeCreator(27299, retList, 84501)
#rangeCreator(18200, retList, 111801)



