#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:51:19 2018

@author: adityamagarde
"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def finding_modes(dataset):
    modeForTime = dataset.mode().iloc[:, 2]         #returns a dataframe with mode of time(2) column
    modeForTimeVal = modeForTime[0]
    modeForSurface = dataset.mode().iloc[:, 8]
    modeForSurfaceVal = modeForSurface[0]
    
    return modeForTimeVal, modeForSurfaceVal


def time_and_date_modifications(X, modeForTimeVal, modeForSurfaceVal):
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
        
    return X


def label_encode(X):
    labelEncoder = LabelEncoder()
    X[:, 5] = labelEncoder.fit_transform(X[:, 5])
    X[:, 3] = labelEncoder.fit_transform(X[:, 3])
    X[:, 4] = labelEncoder.fit_transform(X[:, 4])
    X[:, 6] = labelEncoder.fit_transform(X[:, 6])
    X[:, 7] = labelEncoder.fit_transform(X[:, 7])
    X[:, 8] = labelEncoder.fit_transform(X[:, 8])
    
    return X

def one_hot_encode(X):
    oneHotEncoder = OneHotEncoder(categorical_features=[3, 4, 6, 7, 8])
    X = oneHotEncoder.fit_transform(X).toarray()
    
    return X