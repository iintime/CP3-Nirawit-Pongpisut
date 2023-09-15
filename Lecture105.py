class Vehicle:
    license = ""
    serialNumber = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass



car1 = Car()
car1.turnOnAirConditioner()

pickUp = PickUp()
pickUp.turnOnAirConditioner()

van = Van()
van.turnOnAirConditioner()

estateCar = EstateCar()
estateCar.turnOnAirConditioner()