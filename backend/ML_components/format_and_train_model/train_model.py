import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# load data
file_name = "formatted_ames.csv"
formatted_df = pd.read_csv(file_name)

# split dataframe into X (features) and y (price)
X = formatted_df.iloc[:, 1:]  # predictors
y = formatted_df.iloc[:, 0]  # target variable

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Create a RandomForestRegressor object
rf = RandomForestRegressor(n_estimators=300, max_features='sqrt', warm_start=True)

# train model
rf.fit(X_train, y_train)

joblib.dump(rf, 'random_forest_model.joblib')
