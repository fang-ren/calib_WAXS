"""
author: fangren
"""

import pyFAI
from pyFAI import calibration
from PIL import Image
import numpy as np


im = Image.open('C:\Research_FangRen\Python codes\calib_WAXS\data\LaB6\lab6_041016_rct5_0001.tif')

# change image object into 2048X2048 array
imArray = np.array(im)

calib = pyFAI.calibration
calib.calib(imArray, 'Lab_6', 'MARCCD')