from post.models import Listing
from django.forms import model_to_dict


# get most recent listing in database, return in form of python dict
# return 0 if database is empty
def get_database_data():
    # check if database contains any data
    if Listing.objects.exists():
        listing = Listing.objects.last()  # get most recent listing
        listing = model_to_dict(listing)  # convert model to dict
        return listing
    return 0


# remove key from dictionary
def remove_key(dictionary, key):
    r = dict(dictionary)
    del r[key]
    return r


# rename keys for encoding
def rename_keys(dictionary, new_keys):
    return dict(zip(new_keys, dictionary.values()))
