import mysql.connector

def getDBConnection():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "storage"
    )

    return mydb