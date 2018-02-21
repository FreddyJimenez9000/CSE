# Defining a class
class CheeseBurger(object):
    def __init__(self, patty_type, cheese): # Two underscores before and after
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("you cut the cheeseburger")

    def eat(self):
        print("you eat the cheeseburger")
        self.eaten = True


burger1 = CheeseBurger("beef", "swiss cheese")
burger2 = CheeseBurger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

class car(object):
    def __init__(self, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name


