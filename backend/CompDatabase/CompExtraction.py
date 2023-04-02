#CompExtraction.py

import sqlite3, os


#initiate connection to database
connection = sqlite3.connect( os.getcwd() + '\CompDatabase\comps.db' )
print('Connected to database successfully.\n')

cursor = connection.cursor()

def SortRows( input_params ):

    querysort = '''
    SELECT * FROM Comps
    WHERE NEIGHBORHOOD = :input_neighborhood
    ORDER BY ABS( AREA - :area ) * 0.12897 +
    ( ZONING - :zone ) * 0.0023718 + 
    ABS( LOTAREA - :lotArea ) * 0.026922 + 
    ( BLDGTYPE - :bldgType ) * 0.000759 +
    (HOUSESTYLE - :houseStyle ) * 0.0013082 +
    ABS( OVERALLQUAL - :overallQual ) * 0.59289 +
    ABS( OVERALLCOND - :overallCond ) * 0.00483392 + 
    ABS( YEARBUILT - :yearBuilt ) * 0.015911 +
    ABS( YEARREMOD - :yearRemod ) * 0.01300 +
    ABS( EXTERIOR1 - :exterior1 ) * 0.004974 + 
    ABS( EXTERQUAL - :exterQual ) * 0.0049744 + 
    ABS( EXTERCOND - :extercond ) * 0.000912 + 
    ( FOUNDATION - :foundation ) * 0.0010156 + 
    ABS( BSMTFIN1 - :bsmtFinType1 ) * 0.005651 +
    ABS( BSMTFINSF1 - :bsmtFindSF1 ) * 0.02748 +
    ABS( HEATINGQC - :heatingQC ) * 0.001328019 + 
    ABS( CENTRALAIR - :centralAir ) * 0.0013249 + 
    ABS( ELECTRICAL - :electrical ) * 0.00019918 +
    ABS( FULLBATH - :fullBath ) * 0.0111825 +
    ABS( HALFBATH - :halfBath ) * 0.0013444 +
    ABS( BEDROOM - :bedroom ) * 0.004744 +
    ABS( KITCHEN - :kitchen ) * 0.0004319 +
    ABS( KITCHENQUAL - :kitchenQual ) * 0.01325 +
    ABS( TOTRMSABVGRADE - :totRmsAbvGrd ) * 0.0046141 +
    (GARAGETYPE - :garageType ) * 0.004635 +
    ABS( GARAGECARS - :garageCars ) * 0.01417 +
    ABS( GARAGEAREA - :garageArea ) * 0.013511 +
    ABS( GARAGEQUAL - :garageQual ) * 0.00050362 +
    ABS( WOODDECKSF - :woodDeckSF ) * 0.0060734 +
    (FENCE - :fence ) * 0.001056
    LIMIT 5;'''

    cursor.execute(querysort, input_params )

    return cursor.fetchall()


#Filter the neighhbourhood first
#if there are 5 entries, return them and exit
#if there are less than 5 entries, return them then run the sort algorithm to fill remaining spaces
#if there are more than 5 entries, run the sort algorithm on the entries to return 5

def FindRow( input_params ):
    sorted_rows = SortRows( input_params )

    fetched_rows_len = len(sorted_rows)

    #TODO: Test the following section
    #TODO: try to simplify query statements

    if fetched_rows_len < 5:
        #The only more complicated case
        #We prioritize the rows that were within the neighborhood, but
        #must populate the remaining space for comps with the next best choices based on the sort

        #count the rows found and add them to a list to return
        row_ctr = 0
        rows_to_return = list()

        for row in sorted_rows:
            row_ctr += 1
            rows_to_return.append(row)

        remaining_rows = 5 - row_ctr

        #now run the query again without filtering to get the remaining amount of rows
        query = '''
        SELECT * FROM Comps
        WHERE NEIGHBORHOOD != :neighborhood 
        ORDER BY ABS( AREA - :area ) * 0.12897 +
        ( ZONING - :zone ) * 0.0023718 + 
        ABS( LOTAREA - :lotArea ) * 0.026922 + 
        ( BLDGTYPE - :bldgType ) * 0.000759 +
        (HOUSESTYLE - :houseStyle ) * 0.0013082 +
        ABS( OVERALLQUAL - :overallQual ) * 0.59289 +
        ABS( OVERALLCOND - :overallCond ) * 0.00483392 + 
        ABS( YEARBUILT - :yearBuilt ) * 0.015911 +
        ABS( YEARREMOD - :yearRemod ) * 0.01300 +
        ABS( EXTERIOR1 - :exterior1 ) * 0.004974 + 
        ABS( EXTERQUAL - :exterQual ) * 0.0049744 + 
        ABS( EXTERCOND - :extercond ) * 0.000912 + 
        ( FOUNDATION - :foundation ) * 0.0010156 + 
        ABS( BSMTFIN1 - :bsmtFinType1 ) * 0.005651 +
        ABS( BSMTFINSF1 - :bsmtFindSF1 ) * 0.02748 +
        ABS( HEATINGQC - :heatingQC ) * 0.001328019 + 
        ABS( CENTRALAIR - :centralAir ) * 0.0013249 + 
        ABS( ELECTRICAL - :electrical ) * 0.00019918 +
        ABS( FULLBATH - :fullBath ) * 0.0111825 +
        ABS( HALFBATH - :halfBath ) * 0.0013444 +
        ABS( BEDROOM - :bedroom ) * 0.004744 +
        ABS( KITCHEN - :kitchen ) * 0.0004319 +
        ABS( KITCHENQUAL - :kitchenQual ) * 0.01325 +
        ABS( TOTRMSABVGRADE - :totRmsAbvGrd ) * 0.0046141 +
        (GARAGETYPE - :garageType ) * 0.004635 +
        ABS( GARAGECARS - :garageCars ) * 0.01417 +
        ABS( GARAGEAREA - :garageArea ) * 0.013511 +
        ABS( GARAGEQUAL - :garageQual ) * 0.00050362 +
        ABS( WOODDECKSF - :woodDeckSF ) * 0.0060734 +
        (FENCE - :fence ) * 0.001056
        LIMIT :remaining_rows;'''

        input_params['remaining_rows'] = remaining_rows

        cursor.execute( query, input_params )

        rows_to_return.append(cursor.fetchall())

        return rows_to_return    
    else:
         return sorted_rows
   


def FindComps(user_input_data):
    # print the Comps we found
    rows = FindRow( user_input_data )
    comp_idx = 1
    for row in rows:
        print("Comp #", comp_idx, ": ", row, "\n")
        comp_idx += 1
    #may need to change format
    return rows
    
connection.close()
