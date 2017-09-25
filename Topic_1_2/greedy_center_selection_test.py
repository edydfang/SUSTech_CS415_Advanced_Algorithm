import matplotlib.pyplot as plt
from numpy.random import multivariate_normal
import numpy as np
from greedy_center_selection import greedy_center_select

def test():
    # test case 1
    x = multivariate_normal(np.array([2,-2]),[[2,1.5],[1.5,2]],500)
    y = multivariate_normal(np.array([-2,2]),[[2,1.5],[1.5,2]],500) 
    xy = np.concatenate((x,y),axis=0)
    plt.scatter(xy[:,0],xy[:,1])
    #print(xy.shape)
    result = greedy_center_select(xy,4)
    plt.scatter(np.array(result[:,0]),np.array(result[:,1]),c='red')
    plt.show()
    # test case 2
    x = np.matrix(np.arange(-10,11))
    y = np.matrix(np.arange(-10,11))
    xy = np.concatenate((x,y),axis=0)
    xy = np.array(xy.transpose())
    plt.scatter(xy[:,0],xy[:,0])
    #print(xy.shape)
    result = greedy_center_select(xy,2)
    plt.scatter(np.array(result[:,0]),np.array(result[:,1]),c='red')
    plt.show()


if __name__ == '__main__':
    test()