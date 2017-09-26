#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:37:11 2017

@author: Alex Belianinov

Adaptive thresholding on xray data for Fang Ren

Editted by Fang Ren
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters.rank import median
from skimage.morphology import disk

tif_file ='../data/LaB6/images/1.tif'
img = cv2.imread(tif_file, 0)

selem = disk(11)
img_bckgrd = median(img, selem)
img_subtracted = img - img_bckgrd

min = img.min()
max = img.max()

plt.title('adaptive thresholding image')
plt.subplot(131)
plt.imshow(img)
plt.clim(min, (max - min)*0.03+min)
plt.subplot(132)
plt.imshow(img_bckgrd)
plt.clim(min, (max - min)*0.03+min)
plt.subplot(133)
plt.imshow(img_subtracted)
plt.clim(min, (max - min)*0.03+min)
plt.show()