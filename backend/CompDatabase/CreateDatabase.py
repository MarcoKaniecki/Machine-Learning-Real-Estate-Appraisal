#Created to setup the database for REAML
import os 
import sqlite3
print(sqlite3.sqlite_version)


connection = sqlite3.connect( os.getcwd() + '/backend/CompDatabase/comps.db' )

print( "Connected to database successfully.\n" )

# may need to remove some columns (at least temporarily) for simplicity's sake
# TODO finish constraining the required columns
connection.execute("""CREATE TABLE IF NOT EXISTS Comps ( 
ID INT PRIMARY KEY NOT NULL, 
AREA INT NOT NULL CHECK (AREA >= 0),
SALEPRICE REAL CHECK( SALEPRICE > 0 ),
ZONING TEXT,
LOTAREA INT,
UTILITIES INT,
NEIGHBORHOOD TEXT,
BLDGTYPE TEXT,
HOUSESTYLE TEXT,
OVERALLQUAL INT,
OVERALLCOND INT,
YEARBUILT INT,
YEARREMOD INT,
EXTERIOR1 TEXT,
EXTERQUAL INT,
EXTERCOND INT,
FOUNDATION TEXT,
BSMTFIN1 INT,
BSMTFINSF1 REAL CHECK( BSMTFINSF1 >= 0 ),
TOTALBSMTSF REAL CHECK( TOTALBSMTSF >= 0),
HEATING TEXT,
HEATINGQC INT,
CENTRALAIR BOOL,
ELECTRICAL REAL,
FULLBATH INT,
HALFBATH INT,
BEDROOM INT,
KITCHEN INT,
KITCHENQUAL INT,
TOTRMSABVGRADE INT,
GARAGETYPE TEXT,
GARAGECARS INT,
GARAGEAREA REAL,
GARAGEQUAL INT,
WOODDECKSF REAL,
FENCE INT);""")

# Creating cursor object using connection object - check that the columns were created correctly
cursor = connection.cursor()
cursor.execute( "PRAGMA table_info('Comps')")
print(cursor.fetchall())
cursor.execute("SELECT COUNT(*) FROM pragma_table_info('Comps');")
print("Columns added: ", cursor.fetchall(), "\n")
print("done.\n")
connection.commit()
