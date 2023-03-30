import pandas as pd
import numpy as np
from post.models import Listing
import json
import globals
import joblib


# get data from database, convert to python dict for use in ML model
def get_database_data():
    # get all data from database
    posts = Listing.objects.all()
    
    # convert to dataframe
    df = pd.DataFrame(posts.values())
    
    # convert to json
    data = df.to_json(orient='records')
    
    # convert to python dict
    data = json.loads(data)
    
    return data


# compute predicted price
def calc_predicted_price():
    # ! Need to encode data before passing to model
    # Load the model from the file
    loaded_rf = joblib.load('random_forest_regression_model.joblib')
    
    # Convert the dictionary to a dataframe
    df = pd.DataFrame.from_dict([globals.PROPERTY_FEATURES])
    
    print(globals.PROPERTY_FEATURES)
    
    # Convert the dataframe to a numpy array
    # X = np.array([list(df.values())])
    # X = np.array([list(input_data.values())])

    # Make prediction
    # y_pred = loaded_rf.predict(X)
    # print('predicted price =', y_pred[0])

    return 0