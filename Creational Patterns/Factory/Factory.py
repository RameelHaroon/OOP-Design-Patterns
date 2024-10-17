class Vehicle:

    def typeOfVehicle(self):
        print("This is a vehicle")

class Bike (Vehicle):
    def typeOfVehicle(self):
        print("This is a Bike")

class Sedan (Vehicle):
    def typeOfVehicle(self):
        print("This is a Sedan")

class SUV (Vehicle):
    def typeOfVehicle(self):
        print("This is a SUV")
    
class VehicleFactory:

    def getVehicle(self, type):

        if type.lower() == "bike":
            return Bike()
        elif type.lower() == "sedan":
            return Sedan()
        elif type.lower() == "suv":
            return SUV()
        else:
            return None
            

def main():
    
    factory = VehicleFactory()

    vehicleOne = factory.getVehicle("Bike")
    vehicleOne.typeOfVehicle()

    vehicleTwo = factory.getVehicle("sedan")
    vehicleTwo.typeOfVehicle()

    vehicleThree = factory.getVehicle("suv")
    vehicleThree.typeOfVehicle()


if __name__=="__main__":
    main()