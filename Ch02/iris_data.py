from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

#load the data set

data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']


plength = features[:,2]
is_setosa = (target == 'setosa')

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print 'Max of setosa', max_setosa
print 'Min of others', min_non_setosa


for t,marker,c in zip(xrange(3), ">xo","rgb"):
    plt.scatter(features[target == t,0], features[target == t,1], marker= marker, c=c)

plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()


