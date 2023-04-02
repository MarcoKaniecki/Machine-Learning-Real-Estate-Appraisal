import sys, sqlite3, csv, os
import ColumnNames

argCount = len(sys.argv)

connection = sqlite3.connect( os.getcwd() + '\\backend\CompDatabase\comps.db' )
print('Connected to database successfully.\n')

cursor = connection.cursor()

if argCount == 1:
    print('Include the CSV file(s) to add to the database as command line arguments when running InsertDataFromCSV.py.')
    sys.exit()

def ReadCSVFile(filename):

    #column indices that are used in the database
    selected_columns = [0, 2, 3, 5, 7, 12, 15, 18, 19, 20, 21, 22, 
                        23, 26, 30, 31, 32, 36, 37, 41, 42, 43, 44,
                        45, 51, 52, 53, 54, 55, 56, 60,
                        63, 64, 65, 68, 75]
    
    #encode ordinal data
    encoding_mappings = {
        12: {'AllPub': 3, 'NoSewr': 2, 'NoSeWa': 1, 'ELO': 0},                # UTILITIES
        (30, 31, 43, 55, 65): {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0},  # QUALS/CONDS
        36: {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0, 'NA': -1},          # BSMTFIN1
        44: {'Y': 1, 'N': 0},                                                 # CENTRALAIR
        45: {'Mix': 1.5, 'FuseP': 0, 'FuseF': 1, 'FuseA': 2, 'SBrkr': 3},     # ELECTRICAL
        75: {'GdPrv': 4, 'MnPrv': 3, 'GdWo': 2, 'MnWw': 1, 'NA': 0}           # FENCE
    }

    # Open the CSV file and read the data
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip the header row
        
        # Generate the SQL statement to insert the selected columns into the database
        col_names = ColumnNames.ColumnNames
        sql_statement = "INSERT INTO Comps ({}) VALUES ({})".format(", ".join(col_names), ", ".join(['?']*len(selected_columns)))

        #TODO: handle sql errors 

        # Iterate through each row, encode the selected column values, and insert them into the database
        row_count = 0
        for row in csv_reader:
            # Encode the values in the selected columns using the corresponding encoding mappings
            encoded_values = []
            for i in selected_columns:
                value = row[i]
                if i in encoding_mappings:
                    value_encoding = encoding_mappings[i]
                    encoded_value = value_encoding.get(value, value)
                    encoded_values.append(encoded_value)
                else:
                    encoded_values.append(value)
            # Insert the selected and encoded values into the database
            connection.execute(sql_statement, encoded_values)

            row_count += 1
    return row_count


remainingArgs = argCount
#TODO: test for multiple file inputs at once
rows_processed = 0
while remainingArgs > 1:
    rows_processed += ReadCSVFile(os.getcwd() + sys.argv[argCount - remainingArgs + 1])
    remainingArgs -= 1
print("Rows added to Comps Table: " + str(rows_processed))
connection.commit()
connection.close()