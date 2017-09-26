"""
author: fangren
"""

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from import_test import import_test
from import_training import import_training
from scripts.unused.Single_lab6_generation import single_lab6

X, Y = import_training()


# print X_raw.shape, X_hog.shape, Y.shape

X_train, X_test, Y_train, Y_val = train_test_split(X, Y, test_size=0.25)

seed = 0   # We set our random seed to zero for reproducibility
params_rf = {
    'n_jobs': -1,
    'n_estimators': 1280,
    'warm_start': True,
    'max_features': 0.3,
    'max_depth': 15,
    'min_samples_leaf': 5,
    'random_state' : seed,
    'verbose': 1
}


print 'model training starts...'
rf = RandomForestRegressor(**params_rf)
rf.fit(X_train, Y_train)
print X_test.shape
Y_predict = rf.predict(X_test)
score = rf.score(X_test, Y_val)
print score


print 'visualization...'
# visualization
save_path = '..//..//results//model_results//'

# use a real LaB6 image to test
import numpy as np
imArray, X_real_hog = import_test()
print X_real_hog.shape
Y_calib = rf.predict(X_real_hog)
# Y_calib = 1024, 2000, 2500, 4.7, 0.5
Y_calib = np.concatenate((Y_calib[0], [0.9762]))
print Y_calib
x, y = single_lab6(list(Y_calib), (2048, 2048))
plt.plot(x, y, 'o', c ='k', markersize = 1)
imArray = np.rot90(imArray)
imArray = np.rot90(imArray)
plt.imshow(imArray[:,:,0], vmin = 0, vmax = 25)
plt.savefig(save_path + 'test.png')
plt.close('all')


# beam_X
plt.plot(Y_val[:,0], Y_predict[:,0], 'o', markersize = 1)
plt.xlabel('Y_val')
plt.ylabel('Y_predict_HOG')
plt.savefig(save_path + 'beam_X.png')
plt.close('all')
print 'The MSE for beam_x using HOG features is', mean_squared_error(Y_val[:,0], Y_predict[:,0])

# beam_Y
plt.plot(Y_val[:,1], Y_predict[:,1], 'o', markersize = 1)
plt.xlabel('Y_val')
plt.ylabel('Y_predict_HOG')
plt.savefig(save_path + 'beam_Y.png')
plt.close('all')
print 'The MSE for beam_y using HOG features is', mean_squared_error(Y_val[:,1], Y_predict[:,1])

# distance
plt.plot(Y_val[:,2], Y_predict[:,2], 'o', markersize = 1)
plt.xlabel('Y_val')
plt.ylabel('Y_predict_HOG')
plt.savefig(save_path + 'distance.png')
plt.close('all')
print 'The MSE for distance using HOG features is', mean_squared_error(Y_val[:,2], Y_predict[:,2])

# rotation (Rad)
plt.plot(Y_val[:,3], Y_predict[:,3], 'o', markersize = 1)
plt.xlabel('Y_val')
plt.ylabel('Y_predict_HOG')
plt.savefig(save_path + 'rotation.png')
plt.close('all')
print 'The MSE for rotation using HOG features is', mean_squared_error(Y_val[:,3], Y_predict[:,3])

# tilt (Rad)
plt.plot(Y_val[:,4], Y_predict[:,4], 'o', markersize = 1)
plt.xlabel('Y_val')
plt.ylabel('Y_predict_HOG')
plt.savefig(save_path + 'tilt.png')
plt.close('all')
print 'The MSE for tilt using HOG features is', mean_squared_error(Y_val[:,4], Y_predict[:,4])

