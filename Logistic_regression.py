# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""
import os.path
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as MSD
from PIL import Image


def open_tif(path, filename):
    tif_file = os.path.join(path, filename)
    im = Image.open(tif_file)
    imArray = np.array(im)
    imArray_resize = np.resize(imArray, (imArray.shape[0]*imArray.shape[1], 1))
    return imArray_resize

path = 'C:\Research_FangRen\Python codes\calib_WAXS\LaB6_simu\converted'

X = []

for i in range(20000):
    imArray = open_tif(path, str(i+1)+'.tif')
    #print imArray.shape
    X.append(imArray[:,0])

X = np.array(X)
Y = np.genfromtxt(os.path.join(path, 'training_Y.csv'), delimiter=',')

# data = np.concatenate((X_raw, Y_raw), axis = 1)
# data_shuffle = data[np.random.permutation(data.shape[0]), :]
#
# plt.figure(1)
# imArray = data[0,:1600]
# imArray = imArray.reshape((40, 40))
# plt.imshow(imArray)
#
# plt.figure(2)
# imArray = data_shuffle[0,:1600]
# imArray = imArray.reshape((40, 40))
# plt.imshow(imArray)

# X = data_shuffle[:, :1600]
# Y = data_shuffle[:, 1600:]

X_training = X[:11200,:]
Y_training = Y[:11200,:]

X_test = X[11200:,:]
Y_test = Y[11200:,:]


LR1 = MLPRegressor(hidden_layer_sizes=(2000, 1000, 1000, 100))
#LR1 = Ridge(alpha = 10)
LR1.fit(X_training, Y_training[:,0])
y1_training = LR1.predict(X_training)
y1_test = LR1.predict(X_test)
MSD_training1 = MSD(Y_training[:,0], y1_training)
MSD_test1 = MSD(Y_test[:,0], y1_test)
print MSD_training1, MSD_test1

# LR2 = Ridge()
# LR2.fit(X_training, Y_training[:,1])
# y2 = LR2.predict(X_test)
# LR2.score(X_test, Y_test[:,1])
#
# LR3 = Ridge()
# LR3.fit(X_training, Y_training[:,2])
# y3 = LR3.predict(X_test)
# LR3.score(X_test, Y_test[:,2])
#
# LR4 = Ridge()
# LR4.fit(X_training, Y_training[:,3])
# y4 = LR4.predict(X_test)
# LR4.score(X_test, Y_test[:,3])
#
# LR5 = Ridge()
# LR5.fit(X_training, Y_training[:,4])
# y5 = LR5.predict(X_test)
# LR5.score(X_test, Y_test[:,4])
#
#
