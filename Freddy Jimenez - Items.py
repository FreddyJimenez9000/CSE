inventory = []
# print("there a mic on the ground")
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
    def __init__(self, name, description, damage_ratio, room, pick_up):
        super(Weapon, self).__init__(name, description, pick_up, room)
        self.damage = damage_ratio


class Consumable(Item):
    def __init__(self, name, description, pickup ,room):
        super(Consumable, self). __init__(name, description, pickup, room)
        self.eaten = False


class Wearable(Item):
    def __init__(self, name, description, pickup, room, wear):
        super(Wearable, self). __init__(name, description, pickup, room)
        self.wear = wear

    def wear(self):
        if command == "put on %s" % self.name:
            print("You put on the %s" % self.name)


class Range(Weapon):
    def __init__(self, name, description, affect, room, damage_ratio, pick_up):
        super(Range, self).__init__(name, description, damage_ratio, room, pick_up)
        self.affect = affect


class Arcade_machine(Item):
    def __init__(self, name, description, room, action):
        super(Arcade_machine, self).__init__(name, description, None, room)
        self.action = action


class Melee(Weapon):
    def __init__(self, name, description, room, damage_ratio, pick_up):
        super(Melee,self).__init__(name, description, damage_ratio, room, pick_up)


class Crowbar(Melee):
    def __init__(self, name, description, room, purpose, damage_ratio, pick_up):
        super(Crowbar, self).__init__(name, description, room, damage_ratio, pick_up)
        self.purpose = purpose

    def open_hatch(self):
        print("You have open the hatch. You hesitate to go down")


class Knife(Melee):
    def __init__(self, name, description, room, damage_ratio, pick_up):
        super(Knife, self).__init__(name, description, room, damage_ratio, pick_up)

    def action(self):
        print("You use the knife to defend yourself but failed. You lost your will to live.")


class Flare_gun(Range):
    def __init__(self, name, description, room, damage_ratio, pick_up):
        super(Flare_gun, self).__init__(name, description , 'Fire', room, damage_ratio, pick_up)

    def signal(self):
        print("You shot at the sky to get signal your position. You're save")


class Flare_ammo(Item):
    def __init__(self, name, description, pick_up, room):
        super(Flare_ammo, self).__init__(name, description, pick_up, room)

    def reload(self):
        print("you inputted a shell")


class Ball_pit(Item):
    def __init__(self, name, description, room, pick_up):
        super(Ball_pit, self).__init__(name, description , room, pick_up)


class Flashlight(Item):
    def __init__(self, name, description, room, pick_up):
        super(Flashlight, self).__init__(name, description, pick_up, room)

    def turn_on(self):
        print("You turn on the flashlight")

    def turn_off(self):
        print("You turn off your flashlight")


class Battery(Item):
    def __init__(self, name, description, room, pick_up):
        super(Battery, self).__init__(name, description, pick_up, room)

    def reload(self):
        print("you use the battery to charge your flashlight")


class Mic(Item):
    def __init__(self, name, description, room, pick_up):
        super(Mic, self).__init__(name, description, pick_up, room)


class Cupcake_fake(Item):
    def __init__(self, name, description, room, pick_up):
        super(Cupcake_fake,self).__init__(name, description, pick_up, room)


class Guitar(Item):
    def __init__(self, name, description, pick_up, room ):
        super(Guitar, self).__init__(name, description, pick_up, room)


class Potion(Item):
    def __init__(self, name, description, room, pick_up, affect):
        super(Potion, self).__init__(name, description, room, pick_up)
        self.affect = affect


class Strenth_potion(Potion):
    def __init__(self, name, description ,room , pick_up, affect):
        super(Strenth_potion, self).__init__(name, description, room, pick_up, affect)

    def drink(self):
        print("Your strength increase dramatically")


class Night_vision_potion(Potion):
    def __init__(self, name, description, room, pick_up, affect):
        super(Night_vision_potion, self).__init__(name, description, room, pick_up, affect)

    def drink(self):
        print("You're able to see the dark for a brief time")


class Bag_of_holding(Wearable):
    def __init__(self, name, description, pick_up, room, wear):
        super(Bag_of_holding, self).__init__(name, description, pick_up, room, wear)


class Pizza(Consumable):
    def __init__(self, name, description, pick_up, room):
        self.eaten = False
        super(Pizza,self).__init__(name, description, pick_up, room)

    def eat(self):
        print("You ate the pizza")
        self.eaten = True


class Cup_cake(Consumable):
    def __init__(self, name, description, pick_up, room):
        self.eaten = False
        super(Cup_cake, self).__init__(name, description, pick_up, room)

    def eat(self):
        print("You ate the cup_cake, nothing happen what did you expected")
        self.eaten = True







                # def Pick_up(self):
    #     if command == "pickup %s" % self.name:
    #         print("you pick up %s" % self.name)
    #         inventory.append(command)
    #
    # if command == "inventory":
    #    print(inventory)
#



