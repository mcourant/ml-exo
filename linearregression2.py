import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd
# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = np.array([[81682.0, 1], [81720.0, 2], [81760.0, 3], [81826.0, 4], [81844.0, 5], [81864.0, 6], [81881.0, 7], [81900.0, 8], [81933.0, 9], [82003.0, 10]])
diabetes_Y = np.array([["2019-03-16", 1], ["2019-03-18", 2], ["2019-03-20", 3], ["2019-03-24", 4], ["2019-03-25", 5], ["2019-03-26", 6], ["2019-03-27", 7], ["2019-03-28", 8], ["2019-03-30", 9], ["2019-04-03", 10]])

df = pd.DataFrame({'time': diabetes_Y, 'count': diabetes_X})
df.time = pd.to_datetime(df.time)

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_Y[:-20]
diabetes_y_test = diabetes_Y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(df.time.values.reshape(-1, 1), df['count'].reshape(-1, 1))

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()