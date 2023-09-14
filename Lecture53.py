price = int(input("Enter your price : "))
def vatCalculate(price):
    totalPrice = price + (price*7/100)
    return totalPrice

print(vatCalculate(price))

