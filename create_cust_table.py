import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "storage"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE cust (name VARCHAR(255), phone int, address VARCHAR(255))")
print("Table created...")