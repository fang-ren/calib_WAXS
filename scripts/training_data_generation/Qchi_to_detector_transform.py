# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:39:33 2016

@author: fangren
"""

import numpy as np

def ArcGen(chi, l, e, Xf):
    """
    generate a coordinate on an conic section according to l and e
    Xf is the coordinate of the foci point
    https://en.wikipedia.org/wiki/Conic_section
    """
    r = l/(1 + e * np.cos(chi))
    xbeam = r * np.cos(chi) + Xf
    ybeam = r * np.sin(chi)
    return xbeam, ybeam

def trans(xbeam, ybeam, x0, y0):
    """
    Translate the coordinate (xbeam, ybeam) from x-ray coordinate system (with the x-ray as the origin (0, 0)
    into detector coordinate system
    x0 and y0 are the coordinates of direct x-ray beam in the detector coordinate system
    (with the detector corner as the origin (0, 0), and pixel number as the stepsize 1)
    """
    xdet = xbeam + x0
    ydet = ybeam + y0
    return xdet, ydet

def rotation(Rot, x, y):

    xNew = x*np.cos(Rot) - y*np.sin(Rot)
    yNew = x*np.sin(Rot) + y*np.cos(Rot)
    return xNew, yNew
    
def arcParaGen(twoTheta, d, tilt):
    """
    theta angles is the angle between the vertical lines and the diffraction lines
    According to the theta value, detector to sample distance(d),
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


def detArcGen(x0, y0, d, Rot, tilt, lamda, Q, chi):
    """
    put the functions together
    """
    twoTheta = 2 * calTheta(lamda, Q)
    l, e, Xf = arcParaGen(twoTheta, d, tilt)
    #print l, e
    x, y = ArcGen(chi, l, e, Xf)
    xbeam, ybeam = rotation(Rot, x, y)
    xdet, ydet = trans(xbeam,ybeam, x0, y0)
    return xdet, ydet


if __name__ == '__main__':
    Q = 1.48
    chi = np.arange(-np.pi, np.pi, 0.1)
    xdet, ydet = detArcGen(1024, 2500, 2500, 4.7, 0.5, 0.9762, Q, chi)

    import matplotlib.pyplot as plt
    plt.plot(xdet, ydet, 'o')
    plt.xlim(0, 2048)
    plt.ylim(0, 2048)
    plt.show()