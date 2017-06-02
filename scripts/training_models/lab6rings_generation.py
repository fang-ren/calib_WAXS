# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:39:33 2016

@author: fangren
"""

import numpy as np

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

