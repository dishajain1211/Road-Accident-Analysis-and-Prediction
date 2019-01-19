# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:58:15 2019
@author: Disha Jain
"""

import pandas as pd


roadname = []   

#print(dataset)

def road_class(classname):                                      #convert class number to class name
    if classname == 1:
        return 'M'
    elif classname == 2:
        return 'A(M)'
    elif classname == 3:
        return 'A'
    elif classname == 4:
        return 'B'
    elif classname == 5:
        return 'C'
    elif classname == 6:
        return 'U'

def road_name():                                         #generate road name
    dataset = pd.read_csv('F:\Files\MajorProject\RAP-ter-master\Data\Acc.csv')                                     #read dataset from path
    for index, row in dataset.iterrows():
        road_class_number = road_class(row['1st_Road_Class'])   #read class number
        road_number = row['1st_Road_Number']                    #read road number
        x = road_class_number + str(road_number)                #create road name
        roadname.append(x)
    return roadname

#print(road_name(dataset))
