from scipy.spatial import distance
import numpy as np

def greedy_center_select(x,k):
    '''
    Input 
    x: matrix: (number of points, Dimensions)
    k: number of centers
    '''
    centers = list()
    centers.append(x[0])
    np.delete(x,0,0)
    for i in range(1,k):
        #print(x.shape,centers)
        D = distance.cdist(x,np.matrix(centers), 'euclidean')
        min_dis = np.amin(D, axis=1)
        max_idx = np.argmax(min_dis)
        centers.append(x[max_idx])
        np.delete(x,max_idx,0)
    return np.matrix(centers)