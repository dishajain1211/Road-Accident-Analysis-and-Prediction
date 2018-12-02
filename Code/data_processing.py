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
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import Imputer


#Creating the dataset with the required columns:
    # Date, Day_of_Week, Time, 1st_Road_Class, Road_Type, Speed_Limit, Light_Conditions, Weather_Conditions, Surface_Conditions, Urban_or_Rural_Area
dataset1 = pd.read_csv(r"/home/adityamagarde/Documents/Projects/RAP-ter/Datasets/1.6/1-6m-accidents-traffic-flow-over-16-years/accidents_2012_to_2014.csv")
dataset = dataset1[[9, 10, 11, 14, 16, 17, 24, 25, 26, 29]]


#TODO - 
    # Remove the 'nan' values - one was found in time column - 
    # Reduce date column to (int)month - 
    # Time - into a linear int scale (hour*60 + min) and then normalize - 
    # 1st_Road_Class - one hot encode 3
    # Road_Type- one hot encode 4
    # Speed_Limit - label encode
    # Light_Conditions - one hot encode 6
    # Weather_Conditions - one hot encode 7
    # Surface_Conditions - one hot encode 8

    
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
modeForSurface = dataset.mode().iloc[:, 8]
modeForSurfaceVal = modeForSurface[0]


# Working with time and date coloumns
for i in range(X.shape[0]):
    temp = X[i, 0]                              # Date
    X[i, 0] = int(temp[-7:-5])
    
    temp = X[i, 2]                              # Time
    if(isinstance(temp, str)):                  # If there is a string, then convert it into the value
        X[i, 2] = (int(temp[0:2])*60 + int(temp[-2:]))/60
    else:                                       # Else there is probably the nan value, thus use the mode value 
        X[i,2] = (int(modeForTimeVal[0:2])*60 + int(modeForTimeVal[-2:]))/60
    
    temp = X[i, 8]
    if(isinstance(temp, str)):
        continue
    else:
        X[i, 8] = modeForSurfaceVal
    

# Working with other columns that need to be encoded


# LabelEncoder for Speed_Limit
labelEncoder = LabelEncoder()
X[:, 5] = labelEncoder.fit_transform(X[:, 5])   #Speed_limit
X[:, 3] = labelEncoder.fit_transform(X[:, 3])   #1st_class_road
X[:, 4] = labelEncoder.fit_transform(X[:, 4])
X[:, 6] = labelEncoder.fit_transform(X[:, 6])
X[:, 7] = labelEncoder.fit_transform(X[:, 7])
X[:, 8] = labelEncoder.fit_transform(X[:, 8])


# OneHotEncoder for other columns
oneHotEncoder = OneHotEncoder(categorical_features=[3, 4, 6, 7, 8])
X = oneHotEncoder.fit_transform(X).toarray()


X_train = X[0:10000, :]

# Making the model
model = OneClassSVM(kernel='rbf', gamma=0.00005)  
model.fit(X_train)  