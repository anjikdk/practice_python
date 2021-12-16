class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def test(self):
        print(self.address)

    def __str__(self):
        return "Name: "+ self.name+ ", Phone: "+str(self.phone)+ ", Address: "+ self.address

    # def __repr__(self):
        # return "Name: "+ self.name+ ", Phone: "+str(self.phone)+ ", Address: "+ self.address

    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

c = Customer("Ram", 1234, "ATP")
# c.test()
   
