# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:12:53 2019

@author: ADITYA
"""

import pandas as pd
import numpy as npclear
import tensorflow as tf

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix


TEST_SIZE = 0.2
EPOCHS = 100
BATCH_SIZE = 16

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


model = Sequential()
model.add(Dense(activation = 'relu',  input_dim = 38, units = 20, kernel_initializer = 'uniform'))
model.add(Dense(activation = 'relu', units = 7, kernel_initializer = 'uniform'))
model.add(Dense(activation = 'sigmoid', units = 1, kernel_initializer = 'uniform'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(xTrain, yTrain, batch_size = BATCH_SIZE, nb_epoch = EPOCHS)

yPred = model.predict(xTest)
yPred = (yPred > 0.5)
cm = confusion_matrix(yTest, yPred)
testSetAccuracy = (cm[0, 0] + cm[1, 1])/(sum(sum(cm)))


modelJSON = model.to_json()
with open('model_NN_version1.json', 'w') as jsonFile:
    jsonFile.write(modelJSON)
    
model.save_weights('model_NN_version1.h5')