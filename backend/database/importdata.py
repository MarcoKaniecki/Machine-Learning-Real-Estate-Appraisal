import sqlite3
print(sqlite3.sqlite_version)

import sqlite3
print(sqlite3.__file__)


connection = sqlite3.connect('comps.db')

print( "Connected to database successfully.\n" )

# TODO define lists that constrain the required columns
connection.execute("""CREATE TABLE IF NOT EXISTS Comps ( 
ID INT PRIMARY KEY NOT NULL, 
PICTURES BLOB, 
ADDRESS TEXT NOT NULL, 
POSTALCODE TEXT NOT NULL,
NEIGHBOURHOOD TEXT,
AREATYPE TEXT CONSTRAINT AREATYPE_CHECK CHECK ( strcmp(AREATYPE, "URBAN" ) || strcmp( AREATYPE, "RURAL") || strcmp(AREATYPE, "SUBURBAN")),
BUILDYEAR INT CONSTRAINT BUILDYEAR_INPAST CHECK ( julianday(BUILDYEAR) <= julianday() ),
FLOORINGTYPE TEXT,
INFLOORHEAT BOOL DEFAULT 0,
ELECTRICAL TEXT CONSTRAINT CHECK ( strcmp(ELECTRICAL, "FUSES" ) || strcmp(ELECTRICAL, "BREAKERS")),
HEATING TEXT);""")

# https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/
# Getting all tables from sqlite_master
sql_query = """SELECT name FROM sqlite_master
WHERE type='table';"""
 
# Creating cursor object using connection object
cursor = connection.cursor()
     
# executing our sql query
cursor.execute(sql_query)
print("List of tables\n")
     
# printing all tables list
print(cursor.fetchall())
cursor.execute( "PRAGMA table_info('Comps')")
print(cursor.fetchall())

print("done.\n")
