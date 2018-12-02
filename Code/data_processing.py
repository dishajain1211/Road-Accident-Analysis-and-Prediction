#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:56:47 2018

@author: adityamagarde
"""

#Importing the libraries
import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Imputer

#Creating the dataset with the required columns:
    # Date, Day_of_Week, Time, 1st_Road_Class, Road_Type, Speed_Limit, Light_Conditions, Weather_Conditions, Surface_Conditions, Urban_or_Rural_Area
dataset1 = pd.read_csv(r"/home/adityamagarde/Documents/Projects/RAP-ter/Datasets/1.6/1-6m-accidents-traffic-flow-over-16-years/accidents_2012_to_2014.csv")
dataset = dataset1[[9, 10, 11, 14, 16, 17, 24, 25, 26, 29]]


#TODO - 
    # Remove the 'nan' values - one was found in time column
    # Reduce date column to (int)month
    # Time - into a linear int scale (hour*60 + min) and then normalize
    # 1st_Road_Class - one hot encode
    # Road_Type- one hot encode
    # Speed_Limit - label encode
    # Light_Conditions - one hot encode
    # Weather_Conditions - one hot encode
    # Surface_Conditions - one hot encode
    
# Note -
    # Day_of_Week already an int
    # Urban_Rural - already encoded


# Object of the dataset created by the name X
X = dataset.iloc[:, :].values


# Remove the 'nan' values - one was found in time column
    #imputer = Imputer(missing_values='nan', strategy='most_frequent', axis=0)
    #imputer = imputer.fit(X[:, 2])
    #X[:, :] = imputer.transform(X[:, ])
# Imputer could not work as time is a string initially
# Thus we replace nan values by most frequent value

modeForTime = dataset.mode().iloc[:, 2]         #returns a dataframe with mode of time(2) column
modeForTimeVal = modeForTime[0]


for i in range(X.shape[0]):
    temp = X[i, 0]              #Date
    X[i, 0] = int(temp[-7:-5])    
    temp = X[i, 2]              #Time
    if(isinstance(temp, str)):
        X[i, 2] = (int(temp[0:2])*60 + int(temp[-2:]))/60
    else:
        X[i,2] = (int(modeForTimeVal[0:2])*60 + int(modeForTimeVal[-2:]))/60
    

    

    
    


#Creating the onehotencoder to encode data columns
oneHotEncoder = OneHotEncoder(categorical_features=[])