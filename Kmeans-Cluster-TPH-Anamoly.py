#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:54:30 2020

@author: mohithgowdahr
"""




from matplotlib import pyplot as plt
import pandas as pd
import pickle
import tensorflow as tf
import csv
from sklearn.cluster import KMeans

dataset = pd.read_csv("Raw-Dataset/D.csv")


#------------------------------------ humidity ------------------------------------
x = dataset.iloc[:,5:6].values
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++')
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("WCSS Graph for Humidity")
plt.show()


kmeans = KMeans(n_clusters = 3 , init = 'k-means++' )
h = kmeans.fit_predict(x)

kmeans.predict([[0]])

plt.scatter(x[h ==0,0],x[h == 0,0] ,s = 50, c = 'red')
plt.scatter(x[h ==1,0],x[h == 1,0] ,s = 50, c = 'blue')
plt.scatter(x[h ==2,0],x[h == 2,0] , s = 50,c = 'green')
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 0],s = 10, c = 'yellow')
plt.title("Clustering of Humidity Data")
plt.show()

kmeans = pickle.load(open('Cluster-Model/H_model', 'rb'))

 #------------------------------------ pressure ------------------------------------
x = dataset.iloc[:,6:7].values
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++')
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("WCSS Graph for Pressure")
plt.show()


kmeans = KMeans(n_clusters = 4 , init = 'k-means++' )
p = kmeans.fit_predict(x)

kmeans.predict([[0]])


plt.scatter(x[p ==0,0],x[p == 0,0] ,s = 50, c = 'red')
plt.scatter(x[p ==1,0],x[p == 1,0] ,s = 50, c = 'blue')
plt.scatter(x[p ==2,0],x[p == 2,0] , s = 50,c = 'green')
plt.scatter(x[h ==3,0],x[h == 3,0] ,s = 50, c = 'cyan')
plt.scatter(x[h ==4,0],x[h == 4,0] ,s = 50, c = 'pink')
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 0],s = 10, c = 'yellow')
plt.title("Clustering of Pressure Data")
plt.show()


with open('Cluster-Model/P_model','wb') as f:
    pickle.dump(kmeans,f)

kmeans = pickle.load(open('Cluster-Model/P_model', 'rb'))

 #------------------------------------ temperature ------------------------------------
x = dataset.iloc[:,7:8].values
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++')
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("WCSS Graph for Temperature")
plt.show()


kmeans = KMeans(n_clusters = 2 , init = 'k-means++' )
t = kmeans.fit_predict(x)

kmeans.predict([[0]])


plt.scatter(x[t ==0,0],x[t == 0,0] ,s = 50, c = 'red')
plt.scatter(x[t ==1,0],x[t == 1,0] ,s = 50, c = 'blue')
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 0],s = 10, c = 'yellow')
plt.title("Clustering of Temperature Data")
plt.show()


with open('Cluster-Model/T_model','wb') as f:
    pickle.dump(kmeans,f)

kmeans = pickle.load(open('Cluster-Model/T_model', 'rb'))


# ---------------------------------- Prepare Dataset ---------------------------------

x = dataset.iloc[:,5:8].values


with open("Final-Dataset/Dataset_H.csv",mode="w+",newline='') as f:
            writer = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["humidity","pressure","temperature","anamoly"])
for i in range(len(x)):
    if ( h[i] == 2 or p[i] == 2 or p[i] == 4 or t[i] == 1 ):
        anamoly = 1
    else: 
        anamoly = 0
    with open("Final-Dataset/Dataset_H.csv",mode="a+",newline='') as f:
                writer = csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                writer.writerow([x[i][0],x[i][1],x[i][2],anamoly])









