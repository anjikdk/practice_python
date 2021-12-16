import dbconncetion

mydb = dbconncetion.getDBConnection()

myCursor = mydb.cursor()
myCursor.execute("select * from customer")
myresult = myCursor.fetchall()

for customer in myresult:
    print(customer[0]+" : "+ customer[1])