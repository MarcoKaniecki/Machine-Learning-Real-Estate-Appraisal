# using RandomForestRegressor instead of RandomForestClassifier because the output
# is continuous
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

file_name = "formatted_ames.csv"
formatted_df = pd.read_csv(file_name)

# split dataframe into X (features) and y (price)
X = formatted_df.iloc[:, 1:]  # predictors
y = formatted_df.iloc[:, 0]   # target variable

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Create a random forest regressor model
rf = RandomForestRegressor(n_estimators=100)

# Train the model on the training data
rf.fit(X_train, y_train)

# Predict the prices of the test data
y_pred = rf.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # root mean squared error

print('Root Mean Squared Error:', rmse)

# built in rf.score to compute R^2 may be inaccurate because it assumes a
# linear relationship between the data points.
print('R^2 score:', rf.score(X_test, y_test))


# plot actual vs predicted price
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()
