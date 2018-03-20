
inventory = []
print("there a mic on the ground")
command = input(":").lower()
# head = False
# chest = False
# leg = False
# feet = False


class Item(object):
    def __init__(self, name, description, pick_up, room):
        self.name = name
        self.description = description
        self.Pickup = pick_up
        self.from_room = room


class Weapon(Item):
    def __init__(self, name, description, damage_ratio, room):
        super(Weapon, self).__init__(name, description, damage_ratio, room)
        self.damage = damage_ratio


class Consumable(Item):
    def __init__(self, name, description, pickup ,room):
        super(Consumable, self). __init__(name, description, pickup, room)
        self.eaten = False


class Wearable(Item):
    def __init__(self, name, description, pickup, room):
        super(Wearable, self). __init__(name, description, pickup, room)

    def wear(self):
        if command == "put on %s" % self.name:
            print("You put on the %s" % self.name)








    # def Pick_up(self):
    #     if command == "pickup %s" % self.name:
    #         print("you pick up %s" % self.name)
    #         inventory.append(command)
    #
    # if command == "inventory":
    #    print(inventory)
#


class Range(Weapon):
    def __init__(self, name, description, affect, room, damage_ratio):
        super(Range, self). __init__(name, description, damage_ratio, room )
        self.affect = affect
