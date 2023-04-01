import pandas as pd
import numpy as np
from post.models import Listing
import json
import globals
import joblib


# get data from database, return in form of python dict
def get_database_data():
    posts = Listing.objects.all()  # get all data from database
    df = pd.DataFrame(posts.values())  # convert to dataframe
    data = df.to_json(orient='records')  # convert to json
    data = json.loads(data)  # convert to python dict
    # return most recent entry in database
    return data[-1]


# remove key from dictionary
def remove_key(dictionary, key):
    r = dict(dictionary)
    del r[key]
    return r


# rename keys for encoding
def rename_keys(dictionary, new_keys):
    return dict(zip(new_keys, dictionary.values()))


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
    print('calculating the price of this data:', data)
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