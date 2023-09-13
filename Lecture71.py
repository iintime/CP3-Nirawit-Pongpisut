menuList = []
priceList = []

def showBill ():
    total = 0
    print('-------- My Food --------')
    for n in range(len(menuList)) :
        print(menuList[n],priceList[n])
        total = total + int(priceList[n])
    print('-------- total --------')
    print(total)

while True:
    menuName = input("Please Enter Menu")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input('Price :'))
        menuList.append(menuName)
        priceList.append(menuPrice)

print(menuList,priceList)

showBill()