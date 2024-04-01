from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

cali = fetch_california_housing()
X = cali.data
y = cali.target

# Perform simple linear regression for each feature
for i, feature_name in enumerate(cali.feature_names):
  X_feature = X[:, i].reshape(-1, 1)

  # Spliting
  X_train, X_test, y_train, y_test = train_test_split(X_feature, y, test_size=0.2, random_state=42)

  # Training
  model = LinearRegression()
  model.fit(X_train, y_train)

  # Predictions
  y_pred = model.predict(X_test)

  # Calculate R2 score and mean squared error score
  r2 = r2_score(y_test, y_pred)
  mse = mean_squared_error(y_test, y_pred)

  # Print the results
  print(f"Feature {i} has R2 score: {r2}")
  print(f"Feature {i} has MSE score: {mse}\n")

# R2 the closer to 1 the better the fit
# MSE the closer to 0 the better the fit
# We can look at the R2 score and MSE for each feature and choose the one that has the best fit. Multiple linear regression generally leads to better predictions as it utilizes more data.
# The best fit for our data is Feature 0