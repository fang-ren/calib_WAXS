# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:06:21 2016

@author: fangren
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('C:\\Research_FangRen\\Data\\Jae_samples\\LaB6\\LaB6_rock_t10_b_0001.tif')

# change image object into 2048X2048 array
imArray = np.array(im)

im.close()

# set up 2048X2048 X, Y grids for image array
X = [i+1 for i in range(2048)]
Y = [i+1 for i in range(2048)]
X, Y = np.meshgrid(X, Y)


# plug the data into pcolormesh
plt.pcolormesh(X, Y, imArray)
plt.axis([0, 2048, 0, 2048])
plt.colorbar() #need a colorbar to show the intensity scale
plt.title('LaB6.tif')
plt.figure(1)
