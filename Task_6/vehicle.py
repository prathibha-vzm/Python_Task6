#Question 3

#Base Class
class Vehicle():
    #Constructor with two arguments empty name and rental rate as 0
    def __init__(self,model="",rental_rate=0):
        self.model=model
        self.rental_rate=rental_rate

    #Method to calculate rental
    def calculate_rental(self):
        pass #not using

#Subclass with parent class Vehicle
class car(Vehicle):
    def __init__(self):
        #Getting the model name
        print("Choose the Model\nLuxury\nSUV\nEconomy")
        self.model=input()
        self.rental_rate = 0

    # Method Over-riding
    def calculate_rental(self):
        #Getting Rental hour
        print("Enter Rental hour")
        rental_hour=int(input())

        #Checking the condition according to the input and calculating the rental rate
        if self.model=="Luxury":
            self.rental_rate=5000*rental_hour
            print(f"Luxury Car Rent: {rental_hour}--${self.rental_rate}")

        elif self.model=="SUV":
            self.rental_rate = 500 * rental_hour
            print(f"SUV Car Rent:{rental_hour}--${self.rental_rate}")

        elif self.model=="Economy":
            self.rental_rate = 50 * rental_hour
            print(f"Economy Car Rent:{rental_hour}--${self.rental_rate}")

#Subclass with parent class Vehicle
class bike(Vehicle):
    def __init__(self):
        # Getting the Model name
        print("Choose the Model\nElectric\nScooter\nHybrid")
        self.model = input()
        self.rental_rate=0

    def calculate_rental(self):
        # Getting Rental Days
        print("Number of Rental Days")
        rental_day = int(input())

        # Checking the condition according to the input and calculating the rental rate
        if self.model=="Electric":
            self.rental_rate=500*rental_day
            print(f"{self.model} {rental_day}--${self.rental_rate}")

        elif self.model=="Scooter":
            self.rental_rate = 250 * rental_day
            print(f"{self.model} {rental_day}--${self.rental_rate}")

        elif self.model=="Hybrid":
            self.rental_rate = 450 * rental_day
            print(f"{self.model} {rental_day}--${self.rental_rate}")

#Subclass with parent class Vehicle
class truck(Vehicle):
    def __init__(self):
        # Getting the Model name
        print("Choose the Model\nClosed_Van\nOpen_Truck\n6_Wheeler")
        self.model = input()
        self.rental_rate=0

    def calculate_rental(self):
        # Getting Kilometers travelled
        print("Number of Kilometers")
        rental_km = int(input())

        # Checking the condition according to the input and calculating the rental rate
        if self.model=="Closed_Van":
            self.rental_rate=40*rental_km
            print(f"{self.model} {rental_km}--${self.rental_rate}")

        elif self.model=="Open_Truck":
            self.rental_rate=35*rental_km
            print(f"{self.model} {rental_km}--${self.rental_rate}")

        elif self.model=="6_Wheeler":
            self.rental_rate = 30 * rental_km
            print(f"{self.model} {rental_km}--${self.rental_rate}")

#Creating an Object for the parent class
Vehicle_object=Vehicle()

#Asking to choose the vehicle type
print("Guvi Rental\nChoose the type of Vehicle\n1. Car\n2. Bike\n3. Truck")
vehicle_option=int(input())

#Creating object for the subclasses and Calling the method according to the input
if vehicle_option==1:
    car_object = car()
    car_object.calculate_rental()
elif vehicle_option==2:
    bike_object = bike()
    bike_object.calculate_rental()
elif vehicle_option==3:
    truck_object = truck()
    truck_object.calculate_rental()
else:
    print("Enter Valid option")
