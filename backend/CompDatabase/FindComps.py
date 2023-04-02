#FindComps.py

#This program takes the 38 values to search for comps based on as an argument
#To call this script:
#python FindComps.py --propertyinfo AREA ZONING LOTAREA NEIGHBORHOOD BLDGTYPE HOUSESTYLE OVERALLQUAL OVERALLCOND YEARBUILT
#       YEARREMOD EXTERIOR1 EXTQUAL EXTCOND FOUNDATION BSMTFIN1 BSMTFINSF1 TOTALBSMTSF HEATINGQC CENTRALAIR ELECTRICAL
#       FIRSTFLOORSF SECONDFLOORSF FULLBATH HALFBATH BEDROOMABVG KITCHENABVG KITCHENQUAL TOTALRMSABVG GARAGE GARAGECARS
#       GARAGEAREA GARAGEQUAL WOODDECKSF FENCE
#numerical arguments can be provided as numbers, strings can be provided with quotations.
#assuming that CENTRALAIR, ELECTRICAL, QUAL/CONDS, and FENCE will be provided in their decoded format.


import sys, sqlite3, os, argparse

# CLI=argparse.ArgumentParser()

# CLI.add_argument(
#   "--propertyinfo",  # name on the CLI - drop the `--` for positional/required parameters
#   nargs=34,  # 34 or more values expected for the list
#   type=str
# )

#initiate connection to database
connection = sqlite3.connect( os.getcwd() + '\CompDatabase\comps.db' )
#connection = sqlite3.connect( 'C:\\Users\erinc\Documents\\Winter23\\Repo\\backend\CompDatabase\comps.db' )
print('Connected to database successfully.\n')

cursor = connection.cursor()

# parse the command line
#CLIargs = CLI.parse_args()
# access CLI options
# pass in a list with column values for selected columns
#args_dictionary = vars(CLIargs)
#parsed_args = [int(eval(a)) if isinstance(a, str) and a.isdigit() else a for a in CLIargs.propertyinfo]


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

    #TODO: Test this section
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
    # if len(parsed_args) != 34:
    #     print("There are 34 required column values to search for a comp. You have provided ", len(parsed_args), ".\n",
    #         "Please include the required column values of the property and try again.\n")
    #     sys.exit()
    # else:
    #     print("Searching for Comps based on the input data: ", parsed_args, "\n")

    # input_params = {
    # 'input_area': user_input_data["area"],
    # 'input_zoning': parsed_args[1],
    # 'input_lotarea': parsed_args[2],
    # 'input_neighborhood': parsed_args[3],
    # 'input_bldgtype': parsed_args[4],
    # 'input_housestyle': parsed_args[5],
    # 'input_overallqual': parsed_args[6],
    # 'input_overallcond': parsed_args[7],
    # 'input_yearbuilt': parsed_args[8],
    # 'input_yearremod': parsed_args[9],
    # 'input_exterior1': parsed_args[10],
    # 'input_extqual': parsed_args[11],
    # 'input_extcond': parsed_args[12],
    # 'input_foundation': parsed_args[13],
    # 'input_bsmtfin1': parsed_args[14],
    # 'input_bsmtfinsf1': parsed_args[15],
    # 'input_totalbsmtsf': parsed_args[16],
    # 'input_heatingqc': parsed_args[17],
    # 'input_centralair': parsed_args[18],
    # 'input_electrical': parsed_args[19],
    # 'input_firstfloorsf': parsed_args[20],
    # 'input_secondfloorsf': parsed_args[21],
    # 'input_fullbath': parsed_args[22],
    # 'input_halfbath': parsed_args[23],
    # 'input_bedroomabvg': parsed_args[24],
    # 'input_kitchenabvg': parsed_args[25],
    # 'input_kitchenqual': parsed_args[26],
    # 'input_totalrmsabvg': parsed_args[27],
    # 'input_garage': parsed_args[28],
    # 'input_garagecars': parsed_args[29],
    # 'input_garagearea': parsed_args[30],
    # 'input_garagequal': parsed_args[31],
    # 'input_wooddecksf': parsed_args[32],
    # 'input_fence': parsed_args[33]
    # }
    # print the Comps we found
    rows = FindRow( user_input_data )
    comp_idx = 1
    for row in rows:
        print("Comp #", comp_idx, ": ", row, "\n")
        comp_idx += 1
    #may need to change format
    return rows
    
connection.close()
