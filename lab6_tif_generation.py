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



save_path = 'C:\Research_FangRen\Python codes\calib_WAXS\LaB6_simu'



data = []
for i in np.arange(141209, 200000):
    x0 = 900 + random.random()*200
    y0 = 2100 + random.random() * 400
    d =  1500 + random.random() * 1000
    Rot = -1 + random.random() * 2
    tilt = 0.1 + random.random() * 0.5
    fig = plt.figure(1, figsize=(1, 1))
    ax = fig.add_axes([0, 0, 1, 1])
    for q in Q:
        # each q generates one ring
        xdet, ydet = LaB6rings_gen.detArcGen(x0, y0, d, Rot, tilt, lamda, q)
        ax.plot(xdet, ydet, 'k')
    plt.xlim(0, horiz)
    plt.ylim(0, vert)
    ax.axis('off')
    plt.savefig(os.path.join(save_path, str(i+1)+'.tif'), trasparent = True)
    plt.close()
    print float(i)/2000.0
    data.append([x0, y0, d, Rot, tilt])

data = np.array(data)
np.savetxt(os.path.join(save_path, 'training_Y.csv'), data, delimiter=',')






