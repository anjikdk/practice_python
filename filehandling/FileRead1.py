from Customer import Customer
import traceback
import mysql.connector

f = open("G:/test.txt", mode='r')
customerList = []
try:
    lines = f.readlines()
    phoneNumbers = []
    for line in lines:
        data = line.split("|")
        customerList.append(Customer(data[0], int(data[1]), data[2]))
        phoneNumbers.append(int(data[1]))
    print(phoneNumbers)
    print("Customer data: ", customerList)
except:
    print("Exception occured")
    print(traceback.format_exc())
finally:
    print("Finally block")
    f.close()

def printCustomerData(customerList):
    for c in customerList:
        print(c)

printCustomerData(customerList)

listTuples = []
for c in customerList:
    tuple = ()
    tuple += (c.getName(), c.getPhone(), c.getAddress())
    print(c.getName())
    print(tuple)
    listTuples.append(tuple)

print(listTuples)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "storage"
)

myCursor = mydb.cursor()
sql = "insert into cust (name, phone, address) values (%s, %s, %s)"

myCursor.executemany(sql, listTuples)
mydb.commit()
print("Multiple values are inserted...")



