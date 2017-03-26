# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:39:33 2016

@author: fangren
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os.path



## open MARCCD tiff image
#im = Image.open('C:\\Research_FangRen\\Data\Apr2016\\Jae_samples\\LaB6\\lab6_041016_rct5_0001.tif')
#
## read image object into a 2048X2048 array
#imArray = np.array(im)
#s = int(imArray.shape[0])
#f = s/2048.0
#im.close()
#
## set up 2048X2048 X, Y grids for image array
#X = [i+1 for i in range(s)]
#Y = [i+1 for i in range(s)]
#X, Y = np.meshgrid(X, Y)
# 
#
## plug the data into pcolormesh
#plt.figure(5, figsize = (10, 10))
#plt.pcolormesh(X, Y, imArray)
#plt.axis([0, s, 0, s])
#plt.title('lab6.tif')
#plt.clim(0,2000)



def ArcGen(l, e, Xf):
    """
    generate an arc according to l and e after rotation counterclockwisely
    Xf is the coordinate of the foci point
    """
    chi = np.arange(0, 2*np.pi, .02)
    r = l/(1 + e * np.cos(chi))
    xbeam = r * np.cos(chi) + Xf
    ybeam = r * np.sin(chi)
    return xbeam, ybeam

def trans(xbeam, ybeam, x0, y0):
    xdet = xbeam + x0
    ydet = ybeam + y0
    return xdet, ydet

def rotation(Rot, x, y):
    xNew = x*np.cos(Rot) - y*np.sin(Rot)
    yNew = x*np.sin(Rot) + y*np.cos(Rot)
    return xNew, yNew
    
def arcParaGen(twoTheta, d, tilt):
    """
    According to the theta value, screen to sample distance(d), 
    and screen tilt(t, in degrees), return the semi-rectum(l), 
    eccentricity(e), and the coordiante of a foci point
    """
    p1 = d*np.sin(twoTheta)/np.cos(twoTheta-tilt)
    p2 = d*np.sin(twoTheta)/np.cos(twoTheta+tilt)
    p3 = d*np.tan(twoTheta)
    a = (p1+p2)/2
    Xc = (p1-p2)/2
    bSqr = p3**2/(1-Xc**2/a**2)
    b = np.sqrt(bSqr)
    e = np.sin(tilt)/np.cos(twoTheta)
    l = b**2/a
    Xf = p1-l/(1+e)
    #print a, b, c
    return l, e, Xf

def calTheta(lamda, Q):
    """
    caldulate theta from Q and lamda
    """    
    return np.arcsin(Q*lamda/(4*np.pi))


def detArcGen(x0, y0, d, Rot, tilt, lamda, Q):
    """
    put the functions together
    """
    twoTheta = 2 * calTheta(lamda, Q)
    l, e, Xf = arcParaGen(twoTheta, d, tilt)
    #print l, e
    x, y = ArcGen(l, e, Xf)
    xdet = []
    ydet = []
    for i in range(len(x)):
        xbeam, ybeam = rotation(Rot, x[i], y[i]) 
        xdet.append(trans(xbeam,ybeam, x0, y0)[0])
        ydet.append(trans(xbeam,ybeam, x0, y0)[1])        
    return xdet, ydet


# pixel dimension for the detector
horiz = 2048
vert = 2048

# Q definition for LaB6 standard
Q = [1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, 5.17, 5.38, 5.59]

lamda = 0.9762
d = 1622.75
tilt = 0.51
Rot = 3.23-np.pi
x0 = 1730.65
y0 = 1730.66



save_path = 'C:\Research_FangRen\Python codes\calib_WAXS\LaB6_simu'



fig = plt.figure(1, figsize = (20.48,20.48))
ax = fig.add_axes([0, 0, 1, 1])

for q in Q:
    # each q generates one ring
    xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, q)
    ax.plot(xdet, ydet, 'k')

plt.xlim(0, horiz)
plt.ylim(0, vert)
ax.axis('off')
plt.savefig(os.path.join(save_path, 'LaB6_simu1.tif'), trasparent = True)
plt.close()





