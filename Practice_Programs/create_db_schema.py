import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

myCursor = mydb.cursor()
myCursor.execute("CREATE DATABASE storage")
print("Database crated")