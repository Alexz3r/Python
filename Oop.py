class Vehicle:
    def seating_capacity(self, capacity):
        return "The " + self.name + " has a seating capacity of " + str(capacity) + " passengers."


# Creating objects of two vehicles and setting attributes using user input
vehicle1 = Vehicle()
vehicle1.name = input("Enter vehicle 1 name: ")
vehicle1.max_speed = int(input("Enter vehicle 1 max speed: "))
vehicle1.mileage = int(input("Enter vehicle 1 mileage: "))

vehicle2 = Vehicle()
vehicle2.name = input("Enter vehicle 2 name: ")
vehicle2.max_speed = int(input("Enter vehicle 2 max speed: "))
vehicle2.mileage = int(input("Enter vehicle 2 mileage: "))

# Printing attributes of vehicle1
print("Vehicle 1: Name: " + vehicle1.name + ", Max Speed: " + str(vehicle1.max_speed) + ", Mileage=" + str(vehicle1.mileage))

# Printing attributes of vehicle2
print("Vehicle 2: Name: " + vehicle2.name + ", Max Speed: " + str(vehicle2.max_speed) + ", Mileage=" + str(vehicle2.mileage))

# Calling the seating_capacity method for vehicle1
print(vehicle1.seating_capacity(4))

# Calling the seating_capacity method for vehicle2
print(vehicle2.seating_capacity(4))
