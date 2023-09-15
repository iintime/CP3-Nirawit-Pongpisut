class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added to ", self.name, self.lastName,"'s cart.")

customer1 = Customer()
customer1.name = "Nirawit"
customer1.lastName = "Pongpisut"
customer1.addCart()

customer2 = Customer()
customer2.name = "Prasit"
customer2.lastName = "Meanmanee"
customer2.addCart()

customer3 = Customer()
customer3.name = "Toucharin"
customer3.lastName = "Tongvol"
customer3.addCart()

customer4 = Customer()
customer4.name = "Kittituch"
customer4.lastName = "Srisit"
customer4.addCart()