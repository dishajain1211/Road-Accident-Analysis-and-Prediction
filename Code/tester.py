# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:06:56 2019

@author: ADITYA
"""

import pandas as pd

dataframe = pd.read_csv(r'F:\Files\MajorProject\RAP-ter\DataF\out_worked_f.csv')

LightConditions = dataframe['Light_Conditions'].unique()
WeatherConditions = dataframe['Weather_Conditions'].unique()

vehicles = dataframe.iloc[:, -1]

vehiclesModifiedDF = []

for i in vehicles:
    if '1' in i:
        vehiclesModifiedDF.append(4)
    elif '2' in i:
        vehiclesModifiedDF.append(4)
    elif '3' in i:
        vehiclesModifiedDF.append(4)
    elif '4' in i:
        vehiclesModifiedDF.append(4)
    elif '5' in i:
        vehiclesModifiedDF.append(4)
    elif '97' in i:
        vehiclesModifiedDF.append(4)
    elif '90' in i:
        vehiclesModifiedDF.append(4)
    elif '23' in i:
        vehiclesModifiedDF.append(4)
    elif '22' in i:
        vehiclesModifiedDF.append(4)
    elif '10' in i:
        vehiclesModifiedDF.append(4)
    elif '16' in i:
        vehiclesModifiedDF.append(4)
    elif '20' in i:
        vehiclesModifiedDF.append(3)
    elif '21' in i:
        vehiclesModifiedDF.append(3)
    elif '18' in i:
        vehiclesModifiedDF.append(3)
    elif '11' in i:
        vehiclesModifiedDF.append(3)
    elif '19' in i:
        vehiclesModifiedDF.append(2)
    elif '98' in i:
        vehiclesModifiedDF.append(2)
    elif '-1' in i:
        vehiclesModifiedDF.append(2)
    elif '17' in i:
        vehiclesModifiedDF.append(2)
    else:
        vehiclesModifiedDF.append(1)
        
vehiclesModifiedDF = pd.DataFrame(vehiclesModifiedDF)
vehiclesModifiedDF.to_csv('vehiclesModfied.csv')