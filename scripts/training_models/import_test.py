"""
author: fangren
"""
import numpy as np
import os.path
import cv2
import matplotlib.pyplot as plt
import scipy.io

#path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\simulation\images\\'

def import_test(path = '..//..//data//LaB6'):
    image_path = os.path.join(path, 'images')
    X_raw = []
    X_hog = []
    hog = cv2.HOGDescriptor(path + "//hog.xml")

    tif_file = os.path.join(image_path, str(1)+'.tif')
    print 'importing', tif_file
    imArray = cv2.imread(tif_file)
    imArray = np.rot90(imArray)
    imArray = np.rot90(imArray)
    imArray = imArray
    imArray[imArray < 5] = 0
    hog_features = hog.compute(imArray)

    return imArray, hog_features.T

# imArray, hog_features = import_test()
# print imArray.shape, hog_features.shape
