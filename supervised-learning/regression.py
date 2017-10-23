import numpy as np

from sklearn.datasets import load_boston

boston = load_boston()

from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit(X_rooms, y)

prediction_space = np.linspace(min(X_rooms), max(X_rooms).reshape(-1, 1))
