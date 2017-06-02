"""
author: fangren
"""


import numpy as np
import os.path
import cv2
import matplotlib.pyplot as plt
import scipy.io

#path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\simulation\images\\'

# def import_real_image(path = '..//..//data//LaB6//'):
path = 'C:\\Research_FangRen\\Python codes\\calib_WAXS\\data\\LaB6\\'

tif_file = path +'lab6_041016_rct5_0001.tif'

print 'importing', tif_file
imArray = cv2.imread(tif_file)
imArray = cv2.resize(imArray, (2000, 2000))
imArray = np.rot90(imArray)
imArray = np.rot90(imArray)
print imArray.shape
plt.imshow(imArray[:,:,0])
plt.clim(0, 10)
plt.colorbar()
plt.savefig(path + 'test.png')
plt.close('all')
hog = cv2.HOGDescriptor(path + '/hog.xml')
hog_features = hog.compute(imArray)
print hog_features.shape
plt.plot(range(len(hog_features)), hog_features)
plt.savefig(path + 'test1.png')

calib_file = path + 'lab6_041016_rct5_0001.calib'
file = open(calib_file, 'r')
data = []
with file as inputfile:
    for line in inputfile:
        data.append(line.strip().split('\n'))

bcenter_x = float(data[1][0][10:])
bcenter_y = float(data[2][0][10:])
detector_dist = float(data[3][0][12:])
detect_tilt_alpha = float(data[4][0][18:])
detect_tilt_delta = float(data[5][0][18:])

Y = [bcenter_x, bcenter_y, detector_dist, detect_tilt_alpha, detect_tilt_delta]
print Y
#    return np.array(X_hog), Y

# X_hog, Y = import_real_image()
# print X_hog.shape, Y.shap