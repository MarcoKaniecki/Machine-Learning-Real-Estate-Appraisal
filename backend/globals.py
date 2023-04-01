import numpy as np


ALL_FEATURES = ['price', 'area', 'MS.Zoning', 'Lot.Area', 'Utilities', 'Neighborhood',
                'Bldg.Type', 'House.Style', 'Overall.Qual', 'Overall.Cond', 'Year.Built',
                'Year.Remod.Add', 'Exterior.1st', 'Exter.Qual', 'Exter.Cond', 'Foundation',
                'BsmtFin.Type.1', 'BsmtFin.SF.1', 'Total.Bsmt.SF', 'Heating',
                'Heating.QC', 'Central.Air', 'Electrical',
                'Full.Bath', 'Half.Bath', 'Bedroom.AbvGr', 'Kitchen.AbvGr',
                'Kitchen.Qual', 'TotRms.AbvGrd', 'Garage.Type', 'Garage.Cars',
                'Garage.Area', 'Garage.Qual', 'Wood.Deck.SF', 'Fence']

NOMINAL_MAPPING = {
    'MS.Zoning': {'A (agr)': 0, 'C (all)': 1, 'FV': 2, 'I (all)': 3, 'RH': 4, 'RL': 5, 'RM': 6},
    'Neighborhood': {'Blmngtn': 0, 'Blueste': 1, 'BrDale': 2, 'BrkSide': 3, 'ClearCr': 4, 'CollgCr': 5, 'Crawfor': 6,
                     'Edwards': 7, 'Gilbert': 8, 'Greens': 9, 'GrnHill': 10, 'IDOTRR': 11, 'Landmrk': 12, 'MeadowV': 13,
                     'Mitchel': 14, 'NAmes': 15, 'NPkVill': 16, 'NWAmes': 17, 'NoRidge': 18, 'NridgHt': 19,
                     'OldTown': 20, 'SWISU': 21, 'Sawyer': 22, 'SawyerW': 23, 'Somerst': 24, 'StoneBr': 25,
                     'Timber': 26, 'Veenker': 27},
    'Bldg.Type': {'1Fam': 0, '2fmCon': 1, 'Duplex': 2, 'Twnhs': 3, 'TwnhsE': 4},
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