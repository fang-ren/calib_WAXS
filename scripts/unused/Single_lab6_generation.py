# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:39:33 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt

from scripts.training_models.lab6rings_generation import detArcGen


def single_lab6((x0, y0, d, Rot, tilt, lamda), (horiz, vert)):
    # Q definition for LaB6 standard
    Q = [1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, 5.17, 5.38, 5.59]
    x = []
    y = []
    for q in Q:
        # each q generates one ring
        xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, q)
        x.append(xdet)
        y.append(ydet)
    return x, y



# # pixel dimension for the detector
# horiz = 2048
# vert = 2048
#
# x0, y0, d, Rot, tilt, lamda = 1024, 2000, 2500, 4.7, 0.5, 0.9762
#
# x, y = single_lab6((x0, y0, d, Rot, tilt, lamda), (horiz, vert))
#
# plt.plot(x, y, 'o', c ='k', markersize = 1)
# plt.savefig('test.png')