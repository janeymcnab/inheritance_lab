
class Animal:
   def __init__(self, name): 
    self.name = name
   

class Cat(Animal):
    def __init__(self, name, fur, kittens):
        super().__init__(name)
        self.fur = fur
        self.kittens = kittens
    
    def meow(self):
        return "Meow"


class Chicken(Animal):
    def __init__(self, name, feathers, eggs):
        super().__init__(name)
        self.feathers = feathers
        self.eggs = eggs
    
    def lay_eggs(self):
        return f"Wow! {chicken.name} has laid {chicken.eggs} eggs today!"


cat = Cat ("Mittens", "Tabby", 4)
chicken = Chicken("Gingey", "Ginger", 10)

print(cat.name)
print(chicken.lay_eggs())


class Musician:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take_a_bow(self):
        return "You've been a great crowd"

class Guitarist(Musician):
    def __init__(self, name, age, guitar):
        super().__init__(name, age)
        self.guitar = guitar

    def perfom_solo(self):
        return "Woooohoooo"


class Singer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def stage_dive(self):
        return "Ouch my neck"


singer = Singer("Anthony", 55)
guitarist = Guitarist("John", 50, "Fender")

print(singer.name)
print(singer.stage_dive())
print(guitarist.guitar)

class Boat:
    def __init__(self, name, speed, passengers):
        self.name = name
        self.speed = speed
        self.passengers = passengers
    
    def passenger_count(self):
        return f"The {self.name} holds {self.passengers} passengers on board."
        

class SpeedBoat(Boat):
    def __init__(self, name, speed, passengers, cost_to_hire):
        super().__init__(name, speed, passengers)
        self.cost_to_hire = cost_to_hire
    
    def price(self):
        return f"Speedboat hire from £{speedboat.cost_to_hire} per hour."



class Yacht(Boat):
    def __init__(self, name, speed, passengers, destinations):
        super().__init__(name, speed, passengers)
        self.destinations = destinations
    
    def yacht_passenger_count(self):
        return f"{self.name} holds {self.passengers} passengers on board."

    def list_destinations(self):
        return f"{yacht.name} will stop at the following locations: {yacht.destinations}"

yacht = Yacht ("The Unsinkable", "3 boat miles an hour", 1000, ["France", "Spain", "Portugal"])
speedboat = SpeedBoat("Zoom Zoom", "27 boat miles an hour", 3, 28)

print(speedboat.price())
print(yacht.list_destinations())
print(yacht.yacht_passenger_count())
print(speedboat.passenger_count())



class Doctor:
    def __init__(self, last_name, scrubs):
        self.last_name = last_name
        self.scrubs = scrubs
    
    def wash_hands(self):
        return "30 seconds"

    def doctor_says(self):
        return "I'm going to refer you to a specialist."

class Surgeon(Doctor):
    def __init__(self, last_name, scrubs, number_of_scalpels):
        super().__init__(last_name, scrubs)
        self.number_of_scalpels = number_of_scalpels
    
    def doctor_says(self):
        return "We're going to need to operate."

class GP(Doctor):
    def __init__(self, last_name, scrubs, computer):
       super().__init__(last_name, scrubs) 
       self.computer = computer
    

surgeon = Surgeon("Smith", "Green", 3)
gp = GP("MacLeod", "Blue", "MacBook")

print(surgeon.doctor_says())
print(f"Dr {gp.last_name} wears {gp.scrubs.lower()} scrubs.")



