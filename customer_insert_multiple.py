import dbconncetion

mydb = dbconncetion.getDBConnection()

myCursor = mydb.cursor()
sql = "insert into customer (name, address) values (%s, %s)"
values = [
    ("abc","chennai"),
    ("xyz","vizag"),
    ("Rajesh","ATP")
]

myCursor.executemany(sql, values)
mydb.commit()
print("Multiple values are inserted...")