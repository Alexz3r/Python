class Vehicle:
    def seating_capacity(self, capacity):
        return "The " + self.name + " has a seating capacity of " + str(capacity) + " passengers."


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


# Creating objects of the Bus and Car subclasses
bus = Bus()
bus.name = input("Enter bus name: ")
bus.max_speed = int(input("Enter bus max speed: "))
bus.mileage = int(input("Enter bus mileage: "))

car = Car()
car.name = input("Enter car name: ")
car.max_speed = int(input("Enter car max speed: "))
car.mileage = int(input("Enter car mileage: "))


# Printing attributes of bus
print("Bus: Name=" + bus.name + ", Max Speed=" + str(bus.max_speed) + ", Mileage=" + str(bus.mileage))

# Printing attributes of car
print("Car: Name=" + car.name + ", Max Speed=" + str(car.max_speed) + ", Mileage=" + str(car.mileage))

# Calling the seating_capacity method for bus
print(bus.seating_capacity(50))

# Calling the seating_capacity method for car
print(car.seating_capacity(5))
