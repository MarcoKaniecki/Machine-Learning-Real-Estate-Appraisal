from backend.CompDatabase import CompExtraction

#depending on configuration, may need to run from terminal using:
#python -m backend.Tests.CompExtractionTest

test_input = {
    "id": 1,
    "area": 1656,
    "zone": "RL",
    "lotArea": 31770,
    "utilities": "AllPub",
    "neighborhood": "NAmes",
    "bldgType": "1Fam",
    "houseStyle": "1Story",
    "overallQual": "6",
    "overallCond": "5",
    "yearBuilt": 1960,
    "yearRemod": 1960,
    "exterior1": "BrkFace",
    "exterQual": "TA",
    "exterCond": "TA",
    "foundation": "CBlock",
    "bsmtFinType1": "BLQ",
    "bsmtFindSF1": 639,
    "totalBsmtSF": 1080,
    "heating": "GasA",
    "heatingQC": "Fa",
    "centralAir": "Y",
    "electrical": "SBrkr",
    "fullBath": 1,
    "halfBath": 0,
    "bedroom": 3,
    "kitchen": 1,
    "kitchenQual": "TA",
    "totRmsAbvGrd": 7,
    "garageType": "Attchd",
    "garageCars": 2,
    "garageArea": 528,
    "garageQual": "TA",
    "woodDeckSF": 210,
    "fence": "NA"
}

comps = CompExtraction.FindComps(test_input)
