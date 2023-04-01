import pandas as pd
import json
from post.models import Listing


# get most recent listing in database, return in form of python dict
def get_database_data():
    # * may want to change getting all data from database to getting only most recent entry
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
