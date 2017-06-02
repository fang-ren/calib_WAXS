"""
author: fangren
"""


import numpy as np
import os.path
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import scipy.io


def import_real_image(path = 'C://Research_FangRen//Python codes//calib_WAXS//data//LaB6//images//1.tif'):
    imArray = cv2.imread(path)
    print imArray.shape
    return imArray


imArray = import_real_image()[:,:,0]
imArray = imArray.astype(float)
imArray[imArray < 5] = np.nan
imArray = np.rot90(imArray)
imArray = np.rot90(imArray)
# plt.hist(imArray[imArray != 0])
plt.imshow(imArray, cmap = 'viridis')
plt.clim(0, 10)


imArray2 = import_real_image('C:\\Research_FangRen\\Python codes\\calib_WAXS\\data\\simulation\\training_X\\13.tif')[:,:,0]
imArray2 = imArray2.astype(float)
imArray2[imArray2 < 100] = np.nan
plt.figure(2)
plt.imshow(imArray2, cmap = 'viridis')