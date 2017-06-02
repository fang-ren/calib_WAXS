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
    X = scipy.io.loadmat(os.path.join(path, 'training_X.mat'))['training_X']
    Y = scipy.io.loadmat(os.path.join(path, 'training_Y.mat'))['training_Y']

    return X, Y

# X, Y = import_training()
# print X.shape, Y.shape