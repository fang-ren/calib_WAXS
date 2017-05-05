"""
author: fangren
"""

import numpy as np
import scipy.io
import os.path
import cv2
import matplotlib.pyplot as plt

path = '..//..//data//simulation'


features = scipy.io.loadmat(os.path.join(path, 'feature1.mat'))['data']
feature = features[0,:]

tif_file = path + '//images//1.tif'
imArray = cv2.imread(tif_file)

#imArray = cv2.resize(imArray, (64, 128))
# plt.imshow(imArray)

hog = cv2.HOGDescriptor(path + "//hog_test.xml")
# hog.save(path + "//hog.xml")

hog_feature = hog.compute(imArray)[:,0]

print feature.shape, hog_feature.shape

plt.subplot(121)
plt.plot(range(len(feature)), feature)
plt.subplot(122)
plt.plot(range(len(hog_feature)), hog_feature)
plt.savefig(path + 'feature_compare')


# HOG documentation
# class HOGDescriptor(__builtin__.object)
#  |  Methods defined here:
#  |
#  |  __repr__(...)
#  |      x.__repr__() <==> repr(x)
#  |
#  |  checkDetectorSize(...)
#  |      checkDetectorSize() -> retval
#  |
#  |  compute(...)
#  |      compute(img[, winStride[, padding[, locations]]]) -> descriptors
#  |
#  |  computeGradient(...)
#  |      computeGradient(img[, grad[, angleOfs[, paddingTL[, paddingBR]]]]) -> grad, angleOfs
#  |
#  |  detect(...)
#  |      detect(img[, hitThreshold[, winStride[, padding[, searchLocations]]]]) -> foundLocations, weights
#  |
#  |  detectMultiScale(...)
#  |      detectMultiScale(img[, hitThreshold[, winStride[, padding[, scale[, finalThreshold[, useMeanshiftGrouping]]]]]]) -> foundLocations, foundWeights
#  |
#  |  getDescriptorSize(...)
#  |      getDescriptorSize() -> retval
#  |
#  |  getWinSigma(...)
#  |      getWinSigma() -> retval
#  |
#  |  load(...)
#  |      load(filename[, objname]) -> retval
#  |
#  |  save(...)
#  |      save(filename[, objname]) -> None
#  |
#  |  setSVMDetector(...)
#  |      setSVMDetector(_svmdetector) -> None
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  L2HysThreshold
#  |      L2HysThreshold
#  |
#  |  blockSize
#  |      blockSize
#  |
#  |  blockStride
#  |      blockStride
#  |
#  |  cellSize
#  |      cellSize
#  |
#  |  derivAperture
#  |      derivAperture
#  |
#  |  gammaCorrection
#  |      gammaCorrection
#  |
#  |  histogramNormType
#  |      histogramNormType
#  |
#  |  nbins
#  |      nbins
#  |
#  |  nlevels
#  |      nlevels
#  |
#  |  signedGradient
#  |      signedGradient
#  |
#  |  svmDetector
#  |      svmDetector
#  |
#  |  winSigma
#  |      winSigma
#  |
#  |  winSize
#  |      winSize
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  __new__ = <built-in method __new__ of type object>
#  |      T.__new__(S, ...) -> a new object with type S, a subtype of T

