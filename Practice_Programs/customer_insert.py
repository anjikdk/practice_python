import dbconncetion

mydb = dbconncetion.getDBConnection()

myCursor = mydb.cursor()
sql = "insert into customer (name, address) values (%s , %s)"
value = ("Ram", "Atp")

myCursor.execute(sql, value)
mydb.commit()
print("Data inserted...")