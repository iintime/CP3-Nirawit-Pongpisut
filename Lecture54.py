def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()
def showMenu():
    print("Welcome to BorntoDev shop")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        return Vat()
    elif userSelected == 2:
        return priceCalculator()
    else:
        return menuSelect()
def vatCalculator(total):
    vat = 1.07
    result = total*vat
    return (result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return (vatCalculator(price1 + price2))

def Vat():
    totalPrice = float(input("Total Price : "))
    vatPrice = 1.07
    resultPrice = totalPrice*vatPrice
    return (resultPrice)

print(login())