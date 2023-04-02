//Code adapted from:
//https://videlais.com/2018/12/12/c-with-sqlite3-part-2-creating-tables/

#include <stdio.h>
#include <iostream>
#include <string>

#include "sqlite3.h"

int DropTable(sqlite3* database);
static int CreateTableCallback(void *NotUsed, int argc, char ** argv, char **azColName );
int PrintSelectCallback(void* NotUsed, int argc, char** argv, char** azColName);

int main() 
{
    // Pointer to SQLite connection
    sqlite3* compsDB;
    
    // Save any error messages;
    char* errorMessage = 0;

    std::string sqlStatement;

    // Save the result of opening the file
    int rc = sqlite3_open("comps.db", &compsDB);

    if( rc )
    {
        // Show an error message
        std::cout << "DB Error: " << sqlite3_errmsg( compsDB ) << std::endl;

        //Close the connection
        sqlite3_close( compsDB );
        
        //Return an error
        return( 1 );
    }


    // Close the SQL connection
    sqlite3_close(compsDB);

    return 0;
}


static int CreateTableCallback(void *NotUsed, int argc, char ** argv, char **azColName )
{
    //return successful
    return 0;
}

int PrintSelectCallback(void* NotUsed, int argc, char** argv, char** azColName) {

    // int argc: holds the number of results
    // (array) azColName: holds each column returned
    // (array) argv: holds each value

    for (int i = 0; i < argc; i++) {

        // Show column name, value, and newline
        std::cout << azColName[i] << ": " << argv[i] << std::endl;

    }
    // Insert a newline
    std::cout << std::endl;

    // Return successful
    return 0;
}

int DropTable(sqlite3* database)
{
    std::string dropTableStatement = "DROP TABLE Comps;";
    char* errorMessage = 0;
    int dropTableResult = sqlite3_exec(database, dropTableStatement.c_str(), CreateTableCallback, 0, &errorMessage);
    if (dropTableResult) std::cout << "drop table: " << errorMessage << std::endl;

    return dropTableResult;
}