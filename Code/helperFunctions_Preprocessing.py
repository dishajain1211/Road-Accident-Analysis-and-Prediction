#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:51:19 2018

@author: adityamagarde
"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def finding_modes(dataset, coloumnTime, coloumnSurface):
    
    modeForTime = dataset.mode().iloc[:, coloumnTime]
    modeForTimeVal = modeForTime[0]
    modeForSurface = dataset.mode().iloc[:, coloumnSurface]
    modeForSurfaceVal = modeForSurface[0]
    
    return modeForTimeVal, modeForSurfaceVal


def time_and_date_modifications(X, modeForTimeVal, coloumnDate, coloumnTime):
    
    for i in range(X.shape[0]):    
        temp = X.iloc[i, coloumnDate]
        X.iloc[i, coloumnDate] = int(temp[-7:-5])
        
        
        temp = X.iloc[i, coloumnTime]
        if(isinstance(temp, str)):
            X.iloc[i, coloumnTime] = int(int(temp[0:2])/6)
        else: 
            X.iloc[i, coloumnTime] = int(int(modeForTimeVal[0:2])/6)
        
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



def average_calculator(lengthVal, L):
    
    LSum = sum(L)
    
    temp = 0
    for i in L:
        perc = i/LSum
        print(perc, " ", temp,":", int(temp+lengthVal*perc))
        temp = int(temp+lengthVal*perc) + 1
        

L = [87.7, 91.6, 97.0, 99.6, 101.6, 104.6, 105.2, 105.5, 105.0, 103.7, 100.8, 97.4]
lengthVal = 27300

average_calculator(lengthVal, L)
    
    
    
