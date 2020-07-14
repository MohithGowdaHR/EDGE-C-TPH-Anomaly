#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:22:29 2020

@author: mohithgowdahr
"""

import csv
import pandas as pd
from datetime import datetime
from pytz import timezone
import tensorflow as tf
from tensorflow.keras import layers
from keras import optimizers
import numpy as np


dataset = pd.read_csv("Final-Dataset/Dataset_H.csv")
dataset = dataset.dropna()
x = dataset.iloc[:20000,0:-1].values
y = dataset.iloc[:20000,-1:].values


model = tf.keras.Sequential()
model.add(layers.Flatten(input_shape=(3,)))
model.add(layers.Dense(3, activation='relu'))
model.add(layers.Dense(3, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=2, batch_size=10)


model.predict(x[:1].tolist())
model.predict(x[11673:11674].tolist())


model.save('ANN-Model/TPH_model')

load_model = tf.keras.models.load_model('ANN-Model/TPH_model')
converter = tf.lite.TFLiteConverter.from_keras_model(load_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save the model to disk
open("TF-Model/TPH_Anamoly_Predictor.tflite", "wb").write(tflite_model)


#  command xxd -i TF-Model/TPH_Anamoly_Predictor.tflite > H-Model/TPH_Anamoly_Predictor.h

