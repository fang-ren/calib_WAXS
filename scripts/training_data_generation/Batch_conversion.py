# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""

from PIL import Image
import PIL.ImageOps
import numpy as np
import os.path
import cv2


def convert_tif(path, filename, save_path):
    tif_file = os.path.join(path, filename)
    # open MARCCD tiff image
    im = Image.open(tif_file)
    # read into array and slice it
    imArray = np.array(im)[:,:,0]
    imArray[mask] = 255
    # load sliced array ino image
    im_new = Image.fromarray(imArray)
    # invert the color of array
    inverted_image = PIL.ImageOps.invert(im_new)

    image_compress = inverted_image
    image_compress.save(os.path.join(save_path, filename))

path =  '..\\..\\data\\simulation\\images'
save_path = '..\\..\\data\\simulation\\training_X'


tif_file = '..//..//data///LaB6//images//2.tif'
imArray = cv2.imread(tif_file)
imArray = np.rot90(imArray)
imArray = np.rot90(imArray)
mask = (imArray == 0.0)
mask = mask[:,:,0]
print mask.shape

for i in range(2000):
    print 'converting', path, str(i+1)+'.tif'
    convert_tif(path, str(i+1)+'.tif', save_path)

