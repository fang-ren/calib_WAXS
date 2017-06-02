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

path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\simulation\\'

image_path = os.path.join(path, 'training_X')

X_hog = []
hog = cv2.HOGDescriptor(path + "//hog.xml")

num = 2000
for i in range(num):
    tif_file = os.path.join(image_path, str(i+1)+'.tif')
    print 'importing', tif_file
    imArray = cv2.imread(tif_file)
    #print imArray.shape

    hog_features = hog.compute(imArray)
    X_hog.append(hog_features[:,0])

X_hog = np.nan_to_num(np.array(X_hog))
scipy.io.savemat(path + 'training_X.mat',{'training_X': X_hog})
