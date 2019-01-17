# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:58:15 2019

@author: Disha
"""

import pandas as pd

dataset = pd.read_csv(r"C:\Users\This PC\Desktop\Road Accident Prediction\Acc.csv")
roadname = []

print(dataset)

def road_class(classname):
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

def road_name(dataset):
    for row in dataset.iloc[:,:]:
        road_class_number = road_class(row['1st_Road_Class'])             #check this line
        road_number = row['1st_Road_Number']                #check this line
        x = road_class_number + road_number
        roadname.append(x)
    return roadname

print(road_name(dataset))