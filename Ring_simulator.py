# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:57:30 2016

@author: fangren
"""

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
    

#       
#x0 = 969.878684978
#y0 = 2237.93277884
x0 = 0
y0 = 0

d = 2462.69726489
Rot = 4.69729438873
tilt = 0.5
lamda = 0.97621599151


Q1=1.415536797
Q2=2.041047234
Q3=2.546107216
Q4=2.961188286
Q5=3.315698407
Q6=3.650136865
Q7=4.25947852
Q8=4.481681001
Q9=4.728242491
Q10=4.962816151
Q11=5.185555034
Q12=5.401982521
Q13=5.606671075
Q14=6.010802762
Q15=6.180904961

plt.figure(6)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q1)
plt.plot(xdet, ydet)
#plt.axis([0, 2048, 0, 2048])
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q2)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q3)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q4)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q5)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q6)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q7)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q8)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q9)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q10)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q11)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q12)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q13)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q14)
plt.plot(xdet, ydet)
xdet, ydet = detArcGen(x0, y0, d, Rot, tilt, lamda, Q15)
plt.plot(xdet, ydet)
plt.show()