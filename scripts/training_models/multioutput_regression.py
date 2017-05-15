"""
author: fangren
"""

from import_training import import_training
from import_test import import_test
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

X_raw, X_hog, Y = import_training()

Y = Y[:X_raw.shape[0],]
# print X_raw.shape, X_hog.shape, Y.shape

X_hog_train, X_hog_test, Y_train2, Y_val2 = train_test_split(X_hog, Y, test_size=0.25)

seed = 0   # We set our random seed to zero for reproducibility
params_rf = {
    'n_jobs': -1,
    'n_estimators': 3200,
    'warm_start': True,
    'max_features': 0.3,
    'max_depth': 15,
    'min_samples_leaf': 5,
    'random_state' : seed,
    'verbose': 1
}


rf2 = RandomForestRegressor(**params_rf)
rf2.fit(X_hog_train, Y_train2)
Y_predict2 = rf2.predict(X_hog_test)
score2 = rf2.score(X_hog_test, Y_val2)
print score2


# # use a real LaB6 image to test
# X_real, X_real_hog= import_test()
# Y_calib = rf2.predict(X_real_hog)
# print Y_calib

# # visualization
# save_path = '..//..//results//'
#
# # beam_X
# plt.plot(Y_val2[:,0], Y_predict2[:,0], 'o')
# plt.xlabel('Y_val')
# plt.ylabel('Y_predict_HOG')
# plt.savefig(save_path + 'beam_X.png')
# plt.close('all')
# print 'The MSE for beam_x using HOG features is', mean_squared_error(Y_val2[:,0], Y_predict2[:,0])
#
# # beam_Y
# plt.plot(Y_val2[:,1], Y_predict2[:,1], 'o')
# plt.xlabel('Y_val')
# plt.ylabel('Y_predict_HOG')
# plt.savefig(save_path + 'beam_Y.png')
# plt.close('all')
# print 'The MSE for beam_y using HOG features is', mean_squared_error(Y_val2[:,1], Y_predict2[:,1])
#
# # distance
# plt.plot(Y_val2[:,2], Y_predict2[:,2], 'o')
# plt.xlabel('Y_val')
# plt.ylabel('Y_predict_HOG')
# plt.savefig(save_path + 'distance.png')
# plt.close('all')
# print 'The MSE for distance using HOG features is', mean_squared_error(Y_val2[:,2], Y_predict2[:,2])
#
# # rotation (Rad)
# plt.plot(Y_val2[:,3], Y_predict2[:,3], 'o')
# plt.xlabel('Y_val')
# plt.ylabel('Y_predict_HOG')
# plt.savefig(save_path + 'rotation.png')
# plt.close('all')
# print 'The MSE for rotation using HOG features is', mean_squared_error(Y_val2[:,3], Y_predict2[:,3])
#
# # tilt (Rad)
# plt.plot(Y_val2[:,4], Y_predict2[:,4], 'o')
# plt.xlabel('Y_val')
# plt.ylabel('Y_predict_HOG')
# plt.savefig(save_path + 'tilt.png')
# plt.close('all')
# print 'The MSE for tilt using HOG features is', mean_squared_error(Y_val2[:,4], Y_predict2[:,4])

# save_path = '..//..//results//'
# plt.figure(1)
# plt.subplot(311)
# plt.imshow(Y_val)
# plt.subplot(312)
# plt.imshow(Y_predict1)
# plt.subplot(313)
# plt.imshow(Y_predict2)
# plt.savefig(save_path + 'RandomForest.png')