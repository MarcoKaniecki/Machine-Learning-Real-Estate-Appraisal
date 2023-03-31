import sys, sqlite3, csv, os
import ColumnNames

argCount = len(sys.argv)

#uncomment once done
#if argCount == 1:
#    print('Include the CSV file(s) to add to the database as command line arguments when running InsertDataFromCSV.py.')
#    sys.exit()

connection = sqlite3.connect( os.getcwd() + '\\backend\database\comps.db' )
print('Connected to database successfully.\n')

expectedColumnCount = 42 #can change
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM pragma_table_info('Comps');")
print(cursor.fetchall())

#For ordinal column types that contain text data, this must be converted to ints
#centralair is a bool but data is in Y/N format
#Ordinal types: Fence, 



def ReadCSVFile(filename):


    selected_columns = [0, 2, 3, 5, 7, 12, 15, 18, 19, 20, 21, 22, 
                        23, 26, 30, 31, 32, 36, 37, 41, 42, 43, 44,
                        45, 46, 47, 51, 52, 53, 54, 55, 56, 60,
                        63, 64, 65, 68, 75]
    
    encoding_mappings = {
        12: {'AllPub': 3, 'NoSewr': 2, 'NoSeWa': 1, 'ELO': 0}, #UTILITIES
        (30, 31, 43, 55, 65): {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0},  # QUALS/CONDS
        36: {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0, 'NA': -1}, #BSMTFIN1
        44: {'Y': 1, 'N': 0},                      # CENTRALAIR
        45: {'Mix': 1.5, 'FuseP': 0, 'FuseF': 1, 'FuseA': 2, 'SBrkr': 3},           # ELECTRICAL
        75: {'GdPrv': 4, 'MnPrv': 3, 'GdWo': 2, 'MnWw': 1, 'NA': 0} #FENCE
    }

    # Open the CSV file and read the data
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # get the header row
        
        # Generate the SQL statement to insert the selected columns into the database
        #col_names = [headers[i] for i in selected_columns]
        col_names = ColumnNames.ColumnNames
        sql_statement = "INSERT INTO Comps ({}) VALUES ({})".format(", ".join(col_names), ", ".join(['?']*len(selected_columns)))

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


#function adapted from https://realpython.com/python-csv/
    # query = "INSERT INTO Comps VALUES ("
    # i = 0
    # while i < expectedColumnCount - 1:
    #     query += "?,"
    #     i += 1
    # query += "? )"

    # with open(filename) as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     column_index = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             for column_idx in row:
    #                 if column_idx in [(0, 2, 5, 7, 12, 15, 18, 19, 20, 21, 22, 
    #                                    23, 26, 30, 31, 32, 36, 37, 41, 42, 44,
    #                                    45, 46, 47, 51, 52, 53, 54, 55, 56, 60,
    #                                    63, 64, 65, 68, 75)]:
                         
    #             print(f'Column names are {", ".join(row)}')
    #             columnCount = len(row)
    #             line_count += 1
    #         else:
    #             #for i in columnCount:
    #             #    values.join({f", ".join(row)})
    #             #connection.execute(f'INSERT INTO Comps VALUES( {", ".join(row)} )')
    #             #print(f'INSERT INTO Comps VALUES( {", ".join(row)} )')
    #           #  print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #             connection.execute(query, row)
    #             line_count += 1
    #     print(f'Processed {line_count} lines.')

remainingArgs = argCount
#while remainingArgs > 1:
#    ReadCSVFile(sys.argv[argCount - remainingArgs + 1])
#    remainingArgs -= 1
rows_processed = ReadCSVFile(os.getcwd() + '\\backend\database\\ames.csv')
print("Rows added to Comps Table: " + str(rows_processed))
connection.commit()
connection.close()