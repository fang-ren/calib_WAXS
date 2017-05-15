# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""


import numpy as np
import os.path
import cv2
import matplotlib.pyplot as plt
import scipy.io

#path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\simulation\images\\'

def import_training(path = '..//..//data//simulation'):
    image_path = os.path.join(path, 'images')
    X_raw = []
    X_hog = []
    hog = cv2.HOGDescriptor(path + "//hog.xml")
    for i in range(10000):
        tif_file = os.path.join(image_path, str(i+1)+'.tif')
        print 'importing', tif_file
        imArray = cv2.imread(tif_file)
        #print imArray.shape
        imArray_flat = imArray[:,:,0].reshape(imArray.shape[0]*imArray.shape[1], 1)
        X_raw.append(imArray_flat[:,0])
        plt.imshow(imArray)

        hog_features = hog.compute(imArray)
        X_hog.append(hog_features[:,0])

    Y = scipy.io.loadmat(os.path.join(path, 'target.mat'))['target']
    return np.array(X_raw), np.array(X_hog), Y

# X_raw, X_hog, Y = import_training()
# print X_raw.shape, X_hog.shape, Y.shape