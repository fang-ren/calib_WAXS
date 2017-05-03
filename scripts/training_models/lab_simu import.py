# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""

from PIL import Image
import numpy as np
import os.path


def open_tif(path, filename):
    tif_file = os.path.join(path, filename)
    im = Image.open(tif_file)
    imArray = np.array(im)
    imArray_resize = np.resize(imArray, (imArray.shape[0]*imArray.shape[1], 1))
    return imArray_resize

path = 'C:\Research_FangRen\Python codes\calib_WAXS\LaB6_simu\converted'

features = []
for i in range(20000):
    imArray = open_tif(path, str(i+1)+'.tif')
    #print imArray.shape
    features.append(imArray[:,0])

features = np.array(features)
np.savetxt(os.path.join(path, 'training_X.csv'), features, delimiter=',')

