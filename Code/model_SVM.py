# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:58:56 2019

@author: ADITYA
"""

import pandas as pd

import numpy as npclear
import tensorflow as tf


from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC


TEST_SIZE = 0.2
EPOCHS = 100
BATCH_SIZE = 16


'''
    Preprocessing part
'''

nonAccidents = pd.read_csv(r'F:\Files\MajorProject\RAP-ter\DataF\GeneratedOne.csv')
accidents = pd.read_csv(r'F:\Files\MajorProject\RAP-ter\DataF\out1.csv')

frameset = [nonAccidents, accidents]
dataset = pd.concat(frameset, axis = 0)
dataset = dataset.sample(frac = 1).reset_index(drop = True)                         #Random Shuffle
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

def one_hot_encode(dataframe, cols = 'all'):
    '''
        Function that takes a dataframe and one-hot-encodes the columns provided
    '''
    
    oneHotEncoder = OneHotEncoder(categorical_features = cols)
    dataframe = oneHotEncoder.fit_transform(dataframe).toarray()
    
    return dataframe




X = one_hot_encode(X)
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = TEST_SIZE, random_state = 0)

classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(xTrain, yTrain)

yPred = classifier.predict(xTest)

cm = confusion_matrix(yTest, yPred)