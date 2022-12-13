from dtw import DTWDistance
import numpy as np
import random
import matplotlib.pyplot as plt


def argmin(list):
    #get min index from a list
    return list.index(min(list))

def empty_list(k):
    #create a empty list
    list=[]
    for i in range(k):
        list.append([])
    return list
        
def get_nearest(list,index,ts):
    #get mean DTWdistance of a list
    sum_=0
    for i in range(len(list)):
        sum_+=DTWDistance(ts[list[i]],ts[list[index]])
    return sum_/len(list)


def get_medriod(ts,k):
    #get k clusters and their medroids
    done=False
    center=[]
    center_index=[]
    center_index=random.sample(range(0,len(ts)),k)
    print(center_index)
    # for i in range(k):
    #     center.append(ts[i])
    # for i in range(k):
    #     index=random.randint(0,len(ts)-1)
    #     center.append(ts[index])
    #     center_index.append(index)
    
    # p=0

    while done==False:
        #if the center of all cluster is not change, end while
        # p+=1
        cluster_list=empty_list(k)

        center=[]
        for i in range(k):
            center.append(ts[center_index[i]])

        for i in range(len(ts)):
            # if i not in center_index:
            d=[]
            for j in range(k):
                d.append(DTWDistance(ts[i],center[j]))
            index_d=argmin(d)
            # print(center_index)
            # print(index_d)
            # print(center_index[index_d])
            # cluster_list[center_index[index_d]].append(i)
            cluster_list[index_d].append(i)
        
        center_index_new=[]

        for i in range(len(cluster_list)):
            # print(cluster_list[i])
            mean_list=[]
            for j in range(len(cluster_list[i])):
                mean_list.append(get_nearest(cluster_list[i],j,ts))#
            x=argmin(mean_list)
            center_index_new.append(cluster_list[i][x])

        center_index.sort()
        center_index_new.sort()
        if center_index_new==center_index:
            #if the center of all cluster is not change, end while
            done=True
            print(done)
        
        center_index=center_index_new
    # print('p is')
    # print(p)
    return center_index_new,cluster_list

#generate list with 100 random time series
list=[]
for i in range(100):
    list.append(np.random.rand(100).tolist())

#k=4
center,cluster=get_medriod(list,4)

print('medroids list:',center)
print('clusters list:',cluster)
# print(list[center[0]])
# print(list[center[1]])
# print(list[center[2]])
# plt.plot(list[center[0]])
# plt.show()
# ###############
# time_points = np.arange(0,168,1)
# time_points_2 = time_points * ((2 * np.pi)/24)


# temp = 50 * np.sin(time_points_2 - (15 * ( np.pi/12)))

# temp = np.where(temp < 0, 0, temp)
# #print(temp)

# #plt.plot(time_points, temp)
# #plt.show()

# data = []
# for i in range(100):
#     data.append([])
#     for j in range(100):
#         data[i].append(temp)

# data = np.array(data)

# plt.plot(data[0][0])
# plt.show()