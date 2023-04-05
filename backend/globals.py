import numpy as np


ALL_FEATURES = [
    'area', 'MS.Zoning', 'Lot.Area', 'Utilities', 'Neighborhood',
    'Bldg.Type', 'House.Style', 'Overall.Qual', 'Overall.Cond', 'Year.Built',
    'Year.Remod.Add', 'Exterior.1st', 'Exter.Qual', 'Exter.Cond', 'Foundation',
    'BsmtFin.Type.1', 'BsmtFin.SF.1', 'Total.Bsmt.SF', 'Heating',
    'Heating.QC', 'Central.Air', 'Electrical',
    'Full.Bath', 'Half.Bath', 'Bedroom.AbvGr', 'Kitchen.AbvGr',
    'Kitchen.Qual', 'TotRms.AbvGrd', 'Garage.Type', 'Garage.Cars',
    'Garage.Area', 'Garage.Qual', 'Wood.Deck.SF', 'Fence'
]

NOMINAL_MAPPING = {
    'MS.Zoning': {'A (agr)': 0, 'C (all)': 1, 'FV': 2, 'I (all)': 3, 'RH': 4, 'RL': 5, 'RM': 6},
    'Neighborhood': {'Blmngtn': 0, 'Blueste': 1, 'BrDale': 2, 'BrkSide': 3, 'ClearCr': 4, 'CollgCr': 5, 'Crawfor': 6,
                     'Edwards': 7, 'Gilbert': 8, 'Greens': 9, 'GrnHill': 10, 'IDOTRR': 11, 'Landmrk': 12, 'MeadowV': 13,
                     'Mitchel': 14, 'NAmes': 15, 'NPkVill': 16, 'NWAmes': 17, 'NoRidge': 18, 'NridgHt': 19,
                     'OldTown': 20, 'SWISU': 21, 'Sawyer': 22, 'SawyerW': 23, 'Somerst': 24, 'StoneBr': 25,
                     'Timber': 26, 'Veenker': 27},
    'Bldg.Type': {'1Fam': 0, '2FmCon': 1, 'Duplex': 2, 'Twnhs': 3, 'TwnhsE': 4},
    'House.Style': {'1.5Fin': 0, '1.5Unf': 1, '1Story': 2, '2.5Fin': 3, '2.5Unf': 4, '2Story': 5, 'SFoyer': 6, 'SLvl': 7},
    'Exterior.1st': {'AsbShng': 0, 'AsphShn': 1, 'BrkComm': 2, 'BrkFace': 3, 'CBlock': 4, 'CemntBd': 5, 'HdBoard': 6,
                     'ImStucc': 7, 'MetalSd': 8, 'Plywood': 9, 'PreCast': 10, 'Stone': 11, 'Stucco': 12, 'VinylSd': 13,
                     'Wd Sdng': 14, 'WdShing': 15},
    'Foundation': {'BrkTil': 0, 'CBlock': 1, 'PConc': 2, 'Slab': 3, 'Stone': 4, 'Wood': 5},
    'Heating': {'Floor': 0, 'GasA': 1, 'GasW': 2, 'Grav': 3, 'OthW': 4, 'Wall': 5},
    'Central.Air': {'N': 0, 'Y': 1},
    'Garage.Type': {'2Types': 0, 'Attchd': 1, 'Basment': 2, 'BuiltIn': 3, 'CarPort': 4, 'Detchd': 5, np.nan: 6},
}

ORDINAL_MAPPING = {
    'Utilities': {'AllPub': 4, 'NoSewr': 3, 'NoSeWa': 2, 'ELO': 1, np.nan: 0},
    'Exter.Qual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0},
    'Exter.Cond': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0},
    'BsmtFin.Type.1': {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'NA': 0, np.nan: 0},
    'Heating.QC': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0},
    'Electrical': {'SBrkr': 5, 'FuseA': 4, 'FuseF': 3, 'FuseP': 2, 'Mix': 1, np.nan: 0},
    'Kitchen.Qual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0},
    'Garage.Qual': {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, np.nan: 0},
    'Fence': {'GdPrv': 4, 'MnPrv': 3, 'GdWo': 2, 'MnWw': 1, np.nan: 0},
}

# create a mapping for each feature that isn't numbered by default 
# where the key is the shortend category name of each feature and 
# the value is the expanded form of the category name
DECODE_DATABASE_NAMES = {
    'MS.Zoning': {
        'A (agr)': 'Agriculture', 'C (all)': 'Commercial', 'FV': 'Floating Village Residential', 
        'I (all)': 'Industrial', 'RH': 'Residential High Density', 'RL': 'Residential Low Density', 'RM': 'Residential Medium Density'},
    'Utilities': {
        'AllPub': 'All public Utilities (E,G,W,& S)', 'NoSewr': 'Electricity, Gas, and Water (Septic Tank)', 
        'NoSeWa': 'Electricity and Gas Only', 'ELO': 'Electricity only'},
    'Neighborhood': {
        'Blmngtn': 'Bloomington Heights', 'Blueste': 'Bluestem', 'BrDale': 'Briardale', 'BrkSide': 'Brookside', 'ClearCr': 'Clear Creek',
        'CollgCr': 'College Creek', 'Crawfor': 'Crawford', 'Edwards': 'Edwards', 'Gilbert': 'Gilbert', 'Greens': 'Greens', 'GrnHill': 'Green Hills',
        'IDOTRR': 'Iowa DOT and Rail Road', 'Landmrk': 'Landmark', 'MeadowV': 'Meadow Village', 'Mitchel': 'Mitchell', 'Names': 'North Ames',
        'NoRidge': 'Northridge', 'NPkVill': 'Northpark Villa', 'NridgHt': 'Northridge Heights', 'NWAmes': 'Northwest Ames', 'OldTown': 'Old Town',
        'SWISU': 'South & West of Iowa State University', 'Sawyer': 'Sawyer', 'SawyerW': 'Sawyer West', 'Somerst': 'Somerset', 'StoneBr': 'Stone Brook',
        'Timber': 'Timberland', 'Veenker': 'Veenker'},
    'Bldg.Type': {
        '1Fam': 'Single-family Detached', '2FmCon': 'Two-family Conversion; originally built as one-family dwelling', 
        'Duplex': 'Duplex', 'Twnhs': 'Townhouse End Unit', 'TwnhsE': 'Townhouse Inside Unit'},
    'House.Style': {
        '1.5Fin': 'One and one-half story: 2nd level finished', '1.5Unf': 'One and one-half story: 2nd level unfinished', 
        '1Story': 'One story', '2.5Fin': 'Two and one-half story: 2nd level finished', 
        '2.5Unf': 'Two and one-half story: 2nd level unfinished', '2Story': 'Two story', 'SFoyer': 'Split Foyer', 'SLvl': 'Split Level'},
    'Overall.Qual': {
        '10': 'Very Excellent', '9': 'Excellent', '8': 'Very Good', '7': 'Good', '6': 'Above Average', 
        '5': 'Average', '4': 'Below Average', '3': 'Fair', '2': 'Poor', '1': 'Very Poor'},
    'Overall.Cond': {
        '10': 'Very Excellent', '9': 'Excellent', '8': 'Very Good', '7': 'Good', '6': 'Above Average', 
        '5': 'Average', '4': 'Below Average', '3': 'Fair', '2': 'Poor', '1': 'Very Poor'},
    'Exterior.1st': {
        'AsbShng': 'Asbestos Shingles', 'AsphShn': 'Asphalt Shingles', 'BrkComm': 'Brick Common', 'BrkFace': 'Brick Face', 'CBlock': 'Cinder Block', 'CemntBd': 'Cement Board', 
        'HdBoard': 'Hard Board', 'ImStucc': 'Imitation Stucco', 'MetalSd': 'Metal Siding', 'Plywood': 'Plywood', 'PreCast': 'PreCast', 'Stone': 'Stone', 'Stucco': 'Stucco', 
        'VinylSd': 'Vinyl Siding', 'Wd Sdng': 'Wood Siding', 'WdShing': 'Wood Shingles'
    },
    'Exterior.Qual': {'Ex': 'Excellent', 'Gd': 'Good', 'TA': 'Average/Typical', 'Fa': 'Fair', 'Po': 'Poor'},
    'Exterior.Cond': {'Ex': 'Excellent', 'Gd': 'Good', 'TA': 'Average/Typical', 'Fa': 'Fair', 'Po': 'Poor'},
    'Foundation': {
        'BrkTil': 'Brick & Tile', 'CBlock': 'Cinder Block', 'PConc': 'Poured Contrete', 
        'Slab': 'Slab', 'Stone': 'Stone', 'Wood': 'Wood'},
    'BsmtFin.Type.1': {
        'GLQ': 'Good Living Quarters', 'ALQ': 'Average Living Quarters', 'BLQ': 'Below Average Living Quarters', 
        'Rec': 'Average Rec Room', 'LwQ': 'Low Quality', 'Unf': 'Unfinshed', 'NA': 'No Basement'},
    'Heating': {
        'Floor': 'Floor Furnace', 'GasA': 'Gas forced warm air furnace', 'GasW': 'Gas hot water or steam heat', 
        'Grav': 'Gravity furnace', 'OthW': 'Hot water or steam heat other than gas', 'Wall': 'Wall furnace'},
    'Heating.QC': {'Ex': 'Excellent', 'Gd': 'Good', 'TA': 'Average/Typical', 'Fa': 'Fair', 'Po': 'Poor'},
    'Central.Air': {'N': 'No', 'Y': 'Yes'},
    'Electrical': {
        'SBrkr': 'Standard Circuit Breakers & Romex', 'FuseA': 'Fuse Box over 60 AMP and all Romex wiring (Average)', 
        'FuseF': '60 AMP Fuse Box and mostly Romex wiring (Fair)', 'FuseP': '60 AMP Fuse Box and mostly knob & tube wiring (poor)', 'Mix': 'Mixed'},
    'Kitchen.Qual': {'Ex': 'Excellent', 'Gd': 'Good', 'TA': 'Typical/Average', 'Fa': 'Fair', 'Po': 'Poor'},
    'Garage.Type': {
        '2Types': 'More than one type of garage', 'Attchd': 'Attached to home', 'Basment': 'Basement Garage', 
        'BuiltIn': 'Built-In (Garage part of house - typically has room above garage)', 
        'CarPort': 'Car Port', 'Detchd': 'Detached from home', 'NA': 'No Garage'},
    'Garage.Qual': {'Ex': 'Excellent', 'Gd': 'Good', 'TA': 'Typical/Average', 'Fa': 'Fair', 'Po': 'Poor'},
    'Fence': {'GdPrv': 'Good Privacy', 'MnPrv': 'Minimum Privacy', 'GdWo': 'Good Wood', 'MnWw': 'Minimum Wood/Wire', 'NA': 'No Fence'}
}
