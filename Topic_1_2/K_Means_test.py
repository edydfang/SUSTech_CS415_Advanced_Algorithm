import matplotlib.pyplot as plt
from numpy.random import multivariate_normal
import numpy as np
from K_Means import K_Means

def test():
    # test case 1
    '''
     rng(1);
%     x = [mvnrnd([5 5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([5 -5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([-5 5], [1.5 0; 0 1.5], 500); ...
%          mvnrnd([-5 -5], [1.5 0; 0 1.5], 500)];
    '''
    c = [(5,5),(5,-5),(-5,5),(-5,-5)]
    points = list()
    for ci in c:
        points.append(multivariate_normal(np.array(ci),[[1.5,0],[ 0,1.5]],500))
    xy = np.concatenate(points,axis=0)
    plt.scatter(xy[:,0],xy[:,1])
    #print(xy.shape)
    [result,class_] = K_Means(xy,4,int(1e3))
    plt.scatter(np.array(result[:,0]),np.array(result[:,1]),c='red')
    plt.show()


if __name__ == '__main__':
    test()