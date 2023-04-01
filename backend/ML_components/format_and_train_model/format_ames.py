import pandas as pd
import numpy as np
from category_encoders import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

file_path = "ames.csv"  # or path to file
df = pd.read_csv(file_path)  # df means dataframe
# total: 2930 rows × 82 columns

# all features we plan to use in our ML model
# list matches order of features in df
all_features = ['price', 'area', 'MS.Zoning', 'Lot.Area', 'Utilities', 'Neighborhood',
                'Bldg.Type', 'House.Style', 'Overall.Qual', 'Overall.Cond', 'Year.Built',
                'Year.Remod.Add', 'Exterior.1st', 'Exter.Qual', 'Exter.Cond', 'Foundation',
                'BsmtFin.Type.1', 'BsmtFin.SF.1', 'Total.Bsmt.SF', 'Heating',
                'Heating.QC', 'Central.Air', 'Electrical',
                'Full.Bath', 'Half.Bath', 'Bedroom.AbvGr', 'Kitchen.AbvGr',
                'Kitchen.Qual', 'TotRms.AbvGrd', 'Garage.Type', 'Garage.Cars',
                'Garage.Area', 'Garage.Qual', 'Wood.Deck.SF', 'Fence']

# all features we want to remove from the ames dataset
remove_features = [f for f in df.columns if f not in all_features]

# filter out all features we don't want into a new variable
filtered_df = df.drop(remove_features, axis=1)


# ***********************
# Encode Ordinal Features
# ***********************

# specify what's mapped to what
# col represents the features
# may want to add a np.nan field which corresponds to NA number to fill in true missing
# as NA

# Overall.Qual - already mapped from 1 (very poor) to 10 (very excellent)
# Overall.Cond - already mapped from 1 (very poor) to 10 (very excellent)

maplist = [{'col': 'Utilities',
            'mapping': {'AllPub': 4, 'NoSewr': 3, 'NoSeWa': 2, 'ELO': 1, np.nan: 0}},
           {'col': 'Exter.Qual',
            'mapping': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0}},
           {'col': 'Exter.Cond',
            'mapping': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0}},
           {'col': 'BsmtFin.Type.1',
            'mapping': {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'NA': 0, np.nan: 0}},
           {'col': 'Heating.QC',
            'mapping': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0}},
           {'col': 'Electrical',
            'mapping': {'SBrkr': 5, 'FuseA': 4, 'FuseF': 3, 'FuseP': 2, 'Mix': 1, np.nan: 0}},
           {'col': 'Kitchen.Qual',
            'mapping': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0}},
           {'col': 'Garage.Qual',
            'mapping': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0, np.nan: 0}},
           {'col': 'Fence',
            'mapping': {'GdPrv': 4, 'MnPrv': 3, 'GdWo': 2, 'MnWw': 1, 'NA': 0, np.nan: 0}}
           ]

# setup encoder and encode data
enc = OrdinalEncoder(mapping=maplist)
formatted_df = enc.fit_transform(filtered_df)

ordinal_encoded_features = ['Utilities', 'Exter.Qual', 'Exter.Cond',
                            'BsmtFin.Type.1', 'Heating.QC', 'Electrical',
                            'Kitchen.Qual', 'Garage.Qual', 'Fence']


# ***********************
# Encode Nominal Features
# ***********************

# currently using LabelEncoder for simplicity may want to change

nominal_features = ['MS.Zoning', 'Neighborhood', 'Bldg.Type', 'House.Style', 'Exterior.1st',
                    'Foundation', 'Heating', 'Central.Air', 'Garage.Type']

le_list = ['le_zoning', 'le_neighborhood', 'le_Bldg_Type', 'le_house_style', 'le_exterior_1',
           'le_foundation', 'le_heating', 'le_central_air', 'le_garage_type']

# Initialize a LabelEncoder object for each nominal feature
le_zoning = LabelEncoder()
le_neighborhood = LabelEncoder()
le_Bldg_Type = LabelEncoder()
le_house_style = LabelEncoder()
le_exterior_1 = LabelEncoder()
le_foundation = LabelEncoder()
le_heating = LabelEncoder()
le_central_air = LabelEncoder()
le_garage_type = LabelEncoder()

# Fit each LabelEncoder object to the corresponding feature
# Transform each feature in DataFrame using its corresponding LabelEncoder object
formatted_df['MS.Zoning'] = le_zoning.fit_transform(formatted_df['MS.Zoning'])
formatted_df['Neighborhood'] = le_neighborhood.fit_transform(formatted_df['Neighborhood'])
formatted_df['Bldg.Type'] = le_Bldg_Type.fit_transform(formatted_df['Bldg.Type'])
formatted_df['House.Style'] = le_house_style.fit_transform(formatted_df['House.Style'])
formatted_df['Exterior.1st'] = le_exterior_1.fit_transform(formatted_df['Exterior.1st'])
formatted_df['Foundation'] = le_foundation.fit_transform(formatted_df['Foundation'])
formatted_df['Heating'] = le_heating.fit_transform(formatted_df['Heating'])
formatted_df['Central.Air'] = le_central_air.fit_transform(formatted_df['Central.Air'])
formatted_df['Garage.Type'] = le_garage_type.fit_transform(formatted_df['Garage.Type'])

# Fill in missing values with the mean of the column
formatted_df.fillna(formatted_df.mean(), inplace=True)

# Fill in missing values with the median of the column
# formatted_df.fillna(formatted_df.median(), inplace=True)

# changing every type into an integer
for feature in all_features:
    formatted_df[feature] = formatted_df[feature].astype(int)

# switch price and area columns, if area is 0th column
if formatted_df.columns.get_loc('area') == 0:
    formatted_df = formatted_df.iloc[:, [1, 0] + list(range(2, formatted_df.shape[1]))]

# create new file to store the encoded data
formatted_df.to_csv('formatted_ames.csv', index=False)
