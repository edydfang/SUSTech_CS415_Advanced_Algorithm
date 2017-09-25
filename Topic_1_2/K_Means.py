from scipy.spatial import distance
import numpy as np


def K_Means(x, k, max_iter):
    '''
    % --------
    % INPUT  :
    % --------
    %   x    : matrix(point_num, dimension_num), Double
    %          point set
    %   k    : matrix(1, 1), Integer
    %          total number of centroids
    %   max_iter : matrix(1, 1), Integer
    %          maximum number of iterations
    % --------
    % OUTPUT :
    % --------
    %   class: matrix(point_num, 1), Integer
    %          range from 1 to k
    %   cent : matrix(k, dimension_num), Double
    % --------
    '''
    point_num = x.shape[0]
    r = np.arange(point_num)
    np.random.shuffle(r)
    centers = x[r[:k],:]
    class_ = None
    for i in range(max_iter):
        D = distance.cdist(x,np.matrix(centers), 'euclidean')
        class_ = np.argmin(D, axis=1)
        for j in range(k):
            centers[j,:] = np.mean(x[class_ ==j],axis=0)
    return (centers,class_)