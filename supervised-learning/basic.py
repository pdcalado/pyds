from sklearn import datasets
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

plt.style.use('ggplot')

iris = datasets.load_iris()

type(iris)

print(iris.keys())

print(iris.data.shape)

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
pd.scatter_matrix(df, c = y, figsize = [8,8], s = 150, marker = 'D')


plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
