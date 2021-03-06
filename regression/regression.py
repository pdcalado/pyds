import numpy as np
import pandas as pd

from sklearn import linear_model

reg = linear_model.LinearRegression()

boston = pd.read_csv('boston.csv')

X = boston.drop('MEDV', axis=1).values
y = boston['MEDV'].values

reg.fit(X_rooms, y)

prediction_space = np.linspace(min(X_rooms), max(X_rooms).reshape(-1, 1))

y_pred = reg.predict(X_test)

reg.score(X_test, y_test)

plt.scatter(X_rooms, y)

# labels..

plt.show()
