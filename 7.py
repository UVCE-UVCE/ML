#K Means
import numpy as np
from sklearn.cluster import KMeans
import pylab as pl

np.random.seed(110)
red_mean=3
red_std=0.8
blue_mean=7
blue_std=1

red=np.random.normal(red_mean,red_std,size=40)
blue=np.random.normal(blue_mean,blue_std,size=40)

both_colors=np.sort(np.concatenate((red,blue)))
y=np.zeros(len(both_colors))

kmeans=KMeans(n_clusters=2)
kmeansoutput=kmeans.fit(both_colors.reshape(-1,1))

nc=range(1,5)
kmeans=[ KMeans(n_clusters=i) for i in nc]
score=[ model.fit(both_colors.reshape(-1,1)).score(both_colors.reshape(-1,1))   for model in kmeans]

pl.plot(nc,score)
pl.show()

pl.scatter(both_colors,y,c=kmeansoutput.labels_)
pl.show()