import numpy as np
import matplotlib.pyplot as plt
 
 
def DTWDistance(s1, s2):
    #calculate the DTWdistance of two time series
    DTW={}
 
    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0
 
    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])
 
    return np.sqrt(DTW[len(s1)-1, len(s2)-1])
 
