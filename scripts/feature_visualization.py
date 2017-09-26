"""
author: Fang Ren (SSRL)

5/22/2017
"""
import scipy.io
import matplotlib.pyplot as plt

path = '..\\data\\simulation\\feature1.mat'
save_path = '..\\results\\hog_feature_visualization\\'
features = scipy.io.loadmat(path)['data']

print features.shape
print features[0, :]
print features[0, :].shape

for i in range(0, 12):
    plt.plot(range(576), features[i,:])
    plt.axis('off')
    plt.savefig(save_path + str(i))
    plt.close('all')