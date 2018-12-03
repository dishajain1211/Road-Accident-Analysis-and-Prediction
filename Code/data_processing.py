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
import os
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import Imputer


# Changing the working directory
os.chdir(r"/home/adityamagarde/Documents/Projects/RAP-ter/Code")


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


# Imputer could not work as time is a string initially
# Thus we replace nan values by most frequent value
import helperFunctions_Preprocessing as hF
modeForTimeVal, modeForSurfaceVal = hF.finding_modes(dataset)


# Working with time and date coloumns
X = hF.time_and_date_modifications(X, modeForTimeVal, modeForSurfaceVal)


# Working with other columns that need to be encoded
X = hF.label_encode(X)


# OneHotEncoder for other columns
X = hF.one_hot_encode(X)



X_train = X[0:10000, :]


# Making the model
model = OneClassSVM(kernel='rbf', gamma=0.00005)  
model.fit(X_train)  