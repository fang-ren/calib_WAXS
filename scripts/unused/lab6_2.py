# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:39:09 2016

@author: fangren
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# open MARCCD tiff image
im = Image.open('C:\Research_FangRen\Python codes\calib_WAXS\LaB6\lab6_041016_rct5_0001.tif')

# change image object into 2048X2048 array
imArray = np.array(im)
s = int(imArray.shape[0])
f = s/2048.0
im.close()
#
#image = []
#for i in range(s):
#    image.append([])
#    for j in range(s):
#        image[i].append(imArray[i][j][0])
#
#image = np.array(image)
#imArray = image


# set up 2048X2048 X, Y grids for image array
X = [i+1 for i in range(s)]
Y = [i+1 for i in range(s)]
X, Y = np.meshgrid(X, Y)
 
#Xbeam = []
#Ybeam = []  
#for i in range(s):
#    Xbeam.append([])
#    Ybeam.append([])
#    for j in range(s):
#        xbeam, ybeam = trans(X[i][j],Y[i][j], x0, y0)
#        Xbeam[-1].append(xbeam)
#        Ybeam[-1].append(ybeam)
#
#  
#Xbeam = np.array(Xbeam)
#Ybeam = np.array(Ybeam)   


# plug the data into pcolormesh
plt.figure(5, figsize = (10, 10))
plt.pcolormesh(X, Y, imArray)
plt.axis([0, s, 0, s])
plt.title('lab6_simu.tif')
plt.clim(0,2000)

#plt.figure(2)
#plt.pcolormesh(Xbeam, Ybeam, imArray)
#plt.colorbar() #need a colorbar to show the intensity scale
#plt.clim(0,2000)
#plt.grid()
#plt.show()




import matplotlib.pyplot as plt
import numpy as np

def degrToRad(theta):
    """
    convert an angle from degree to radius
    """
    return float(theta) * np.pi/180.0

def rotArcGen(l, e, Rot):
    """
    generate an arc according to l and e after rotation counterclockwisely
    """
    chi = np.arange(0, 2*np.pi, .02)
    r = l/(1 + e * np.cos(chi-Rot))
    xbeam = r * np.cos(chi)
    ybeam = r * np.sin(chi)
    return xbeam, ybeam

def trans(xbeam, ybeam, x0, y0):
    xdet = xbeam + x0
    ydet = ybeam + y0
    return xdet, ydet

#x, y = rotArcGen(10,0.5, np.pi/2)
#plt.plot(x, y)
#plt.axis([-20,20,-10, 30])
#plt.show()

#def rotArcsGen(L, E, Rot):
#    numArcs = len(L)
#    X = []
#    Y = []
#    for i in range(numArcs):
#        X.append(rotArcGen(L[i], E[i], Rot)[0])
#        Y.append(rotArcGen(L[i], E[i], Rot)[1])
#    return X, Y
    
def arcParaGen(twoTheta, d, tilt):
    """
    According to the theta value (in degrees), screen to sample distance(D), 
    and screen tilt(t, in degrees), return the semi-rectum(l) and 
    eccentricity(e)
    """
    l = d * np.tan(twoTheta)
    e = np.sin(tilt)/np.cos(twoTheta)
    return l, e

#def arcsParaGen(twoTHETA, D, tilt):
#    """
#    According to the theta values (in degrees), screen to sample distance(D), 
#    and screen tilt(t, in degrees), return the semi-rectum(L) and 
#    eccentricity(E)
#    """
#    numArcs = len(twoTHETA)
#    L = []
#    E = []
#    for i in range(numArcs):
#        L.append(arcParaGen(twoTHETA[i], D, tilt)[0])
#        E.append(arcParaGen(twoTHETA[i], D, tilt)[1])
#    return L, E


def calTheta(lamda, Q):
    return np.arcsin(Q*lamda/(4*np.pi))


def detArcGen(x0, y0, d, Rot, tilt, lamda, Q):
    twoTheta = 2 * calTheta(lamda, Q)
    l, e = arcParaGen(twoTheta, d, tilt)
    #print l, e
    xbeam, ybeam = rotArcGen(l, e, Rot)
    xdet = []
    ydet = []
    for i in range(len(xbeam)):
        xdet.append(trans(xbeam[i],ybeam[i], x0, y0)[0])
        ydet.append(trans(xbeam[i],ybeam[i], x0, y0)[1])        
    return xdet, ydet
    

#x0 = 969.878684978*f
#y0 = 2237.93277884*f
##y0 = 2087*f
#d = 2462.69726489*f
##d = 2462*f
#Rot = 4.69729438873
#tilt = 0.503226642865
##tilt = 0.2
#lamda = 0.97621599151


       
x0 = 969.878684978*f
#y0 = 2237.93277884
y0 = 2087*f
#d = 2462.69726489
d = 2252*f
Rot = 4.69729438873
#tilt = 0.503226642865
tilt = 0.2
lamda = 0.97621599151



#Q = [1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, \
#5.17, 5.38, 5.59, 6.010802762, 6.180904961]

Q = [1.48, 2.1, 2.57, 2.97, 3.33, 3.65, 4.22, 4.48, 4.71, 4.95, \
5.17, 5.38, 5.59]

plt.figure(5, figsize = (10, 10))

for q in Q:
    xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, q)
    plt.plot(xdet, ydet)
plt.axis([0, s, 0, s])
#plt.axis([-1000, 1500, 0, 2500])
plt.show()
