# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""

from PIL import Image
import numpy as np

# open MARCCD tiff image
im = Image.open('C:\Research_FangRen\Python codes\calib_WAXS\LaB6_simu\LaB6_simu1.tif')
#im = Image.open('C:\\Users\\Fang Ren\\Desktop\\Detector tilt geometry\\transformation\\lab6_arcs.tif')
# change image object into 2048X2048 array

imArray = np.array(im)[:,:,0]

im_new = Image.fromarray(imArray)


import PIL.ImageOps


inverted_image = PIL.ImageOps.invert(im_new)
inverted_image.save("LaB6_simu//your_file.tif")