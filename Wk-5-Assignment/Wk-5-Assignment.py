# OOP Concepts: Classes, Objects, Inheritance
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def call(self):
        return f"{self.brand} {self.model} is making a call 📞"
    
    def charge(self):
        return f"{self.model} is charging... 🔋"

# Inheritance Example
class GamingPhone(Smartphone):
    def play_game(self):
        return f"{self.model} is playing a high-end game 🎮"
    


#Activity 2: Polymorphism Challenge!
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing ⛵"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
# Testing the classes

