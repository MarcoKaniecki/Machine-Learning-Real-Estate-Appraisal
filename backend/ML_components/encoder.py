import globals
from database_tools.tools import remove_key, rename_keys


# encode data for use in ML model
def encode_data(data):
    # remove id from data because it is not a feature
    if 'id' in data.keys():
        data = remove_key(data, 'id')
    
    # check if data length matches feature length
    if len(data) != len(globals.ALL_FEATURES):
        print('data length does not match feature length')
        return 0
    
    # rename keys to match feature names
    data = rename_keys(data, globals.ALL_FEATURES)

    # encode ordinal and nominal values
    for key, value in data.items():
        # skip if key is not in ordinal or nominal mapping
        if key in globals.ORDINAL_MAPPING.keys():
            data[key] = globals.ORDINAL_MAPPING[key][value]
        elif key in globals.NOMINAL_MAPPING.keys():
            data[key] = globals.NOMINAL_MAPPING[key][value]

        # convert all values to int
        data[key] = int(data[key])

    return data
