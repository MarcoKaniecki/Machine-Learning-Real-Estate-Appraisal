import pandas as pd
import globals
import joblib

from database_tools.tools import remove_key, rename_keys



# encode data for use in ML model
def encode_data(data):
    # remove id from data because it is not a feature
    if 'id' in data.keys():
        data = remove_key(data, 'id')
    
    # minus 1 because we are not encoding the price
    if len(data) != len(globals.ALL_FEATURES) - 1:
        print('data length does not match feature length')
        return 0
    
    # rename keys to match feature names except for price
    data = rename_keys(data, globals.ALL_FEATURES[1:])

    # encode ordinal and nominal values
    for key, value in data.items():
        # skip if key is not in ordinal or nominal mapping
        if key in globals.ORDINAL_MAPPING.keys():
            data[key] = globals.ORDINAL_MAPPING[key][value]
        elif key in globals.NOMINAL_MAPPING.keys():
            data[key] = globals.NOMINAL_MAPPING[key][value]

    return data


# compute predicted price
def calc_predicted_price(data):
    # Load the model from the file
    loaded_rf = joblib.load('random_forest_regression_model.joblib')
    
    # Convert the dictionary to a dataframe
    encoded_df = pd.DataFrame.from_dict([data])
    X = encoded_df.values
    X = [[int(i) for i in X[0]]] # convert to int and 2D array
    
    # Make prediction
    y_pred = loaded_rf.predict(X)

    # y_pred is in form of array, so we need to convert to int
    return int(y_pred[0])