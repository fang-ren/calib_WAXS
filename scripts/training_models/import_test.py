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
    for i in range(1):
        tif_file = os.path.join(image_path, str(i+1)+'.tif')
        print 'importing', tif_file
        imArray = cv2.imread(tif_file)
        print imArray.shape
        imArray_flat = imArray[:,:,0].reshape(imArray.shape[0]*imArray.shape[1], 1)
        X_raw.append(imArray_flat[:,0])
        plt.imshow(imArray)

        hog_features = hog.compute(imArray)
        X_hog.append(hog_features[:,0])

    return np.array(X_raw), np.array(X_hog)

# X_raw, X_hog= import_test()
# print X_raw.shape, X_hog.shape
