# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:56:38 2016

@author: fangren
"""

from PIL import Image
import PIL.ImageOps
import numpy as np
import os.path



def convert_tif(path, filename):
    tif_file = os.path.join(path, filename)
    save_path = os.path.join(path, 'converted')
    # open MARCCD tiff image
    im = Image.open(tif_file)
    # read into array and slice it
    imArray = np.array(im)[:,:,0]
    # load sliced array ino image
    im_new = Image.fromarray(imArray)
    # invert the color of array
    inverted_image = PIL.ImageOps.invert(im_new)
    inverted_image.save(os.path.join(save_path, filename))