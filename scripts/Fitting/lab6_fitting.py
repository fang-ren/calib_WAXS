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
from Ring_simulator import detArcGen

# pixel dimension for the detector
horiz = 2048
vert = 2048

# Q definition for LaB6 standard
Q = np.array([1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, 5.17, 5.38, 5.59])

q = 1.48
lamda = 0.9762

save_path = 'C:\Research_FangRen\Python codes\calib_WAXS\data\LaB6'

x0 = 969.878684978
y0 = 2237.93277884
d = 2462.69726489
Rot = 4.69729438873
tilt = 0.503226642865


xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, q)

print xdet, ydet
plt.plot(xdet, ydet)
plt.savefig('test')