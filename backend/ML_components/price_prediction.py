import joblib
import globals
import pandas as pd


# compute predicted price
def calc_predicted_price(data):
    # Load the model from the file
    loaded_rf = joblib.load('random_forest_regression_model.joblib')
    
    # Convert the dictionary to a dataframe
    encoded_df = pd.DataFrame.from_dict([data])
    X = encoded_df[globals.ALL_FEATURES]
    
    # Make prediction
    y_pred = loaded_rf.predict(X)

    # y_pred is in form of array, so we need to convert to int
    return int(y_pred[0])
