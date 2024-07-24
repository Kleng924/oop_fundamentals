# City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python 
# to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, 
# methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and 
# demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.
# Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script 
# showing the creation of Vehicle objects and updating their owners.


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"New owner: {new_owner} for vehicle with registration number {self.registration_number}")

if __name__ == "__main__":
    vehicle1 = Vehicle("ABC123", "Car", "Yuki")
    vehicle2 = Vehicle("DEF456", "Truck", "Otto")
    
    print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")
    
    vehicle1.update_owner("Nina T.")
    vehicle2.update_owner("Nico T.")
    
    print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")



# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the 
# current count.

# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count
    
event = Event("Conference", "2024-07-24")
event.add_participant()
event.add_participant()
print(event.get_participant_count())





