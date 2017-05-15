# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:39:33 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt
import os.path
import imp
import random
import PIL
from PIL import Image

LaB6rings_gen = imp.load_source('detArcGen', 'lab6rings_generation.py')
convert_tif = imp.load_source('convert_tif', 'Convert_tif.py')


# pixel dimension for the detector
horiz = 2048
vert = 2048

# Q definition for LaB6 standard
Q = [1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, 5.17, 5.38, 5.59]

lamda = 0.9762


D = np.arange(1500, 2500, 200)
Tilt = np.arange(0.1, 0.6, 0.1)
Rot = np.arange(-1, 1, 0.2)
X0 = np.arange(900, 1100, 100)
Y0 = np.arange(2100, 2500, 100)



save_path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\LaB6'


x0 = 969.878684978
y0 = 2237.93277884
d = 2462.69726489
Rot = 4.69729438873
tilt = 0.503226642865

fig = plt.figure(1, figsize=(1, 1))
ax = fig.add_axes([0, 0, 1, 1])

for q in Q:
    # each q generates one ring
    xdet, ydet = LaB6rings_gen.detArcGen(x0, y0, d, Rot, tilt, lamda, q)
    ax.plot(xdet, ydet, 'k')
plt.xlim(0, horiz)
plt.ylim(0, vert)
ax.axis('off')
plt.savefig(os.path.join(save_path, 'simulation.tif'), trasparent = True)


tif_file = os.path.join(save_path, 'simulation.tif')

# open MARCCD tiff image
im = Image.open(tif_file)
# read into array and slice it
imArray = np.array(im)[:, :, 0]
# load sliced array ino image
im_new = Image.fromarray(imArray)
# invert the color of array
inverted_image = PIL.ImageOps.invert(im_new)
image_compress = inverted_image.resize((40, 40), Image.ANTIALIAS)
image_compress.save(os.path.join(save_path, 'simulation1.tif' ))


