import random
inventory = []
invCapacity = 8
# fix inventory


class Item(object):
    def __init__(self, name, description, room):
        self.name = name
        self.description = description
        self.from_room = room
        self.isTaken = False

    def take(self):
        if bag_of_holding in inventory:
            inventory.append(self)
            self.isTaken = True
            print("You took the item")
        else:
            if len(inventory) == 8:
                print("You are holding too much stuff")
            else:
                inventory.append(self)
                self.isTaken = True
                print("You took the item")

    def drop(self):
        inventory.remove(self)
        self.isTaken = False
        print("You drop the item")


##
class Weapon(Item):
    def __init__(self, name, description, damage_ratio, room, magazine):
        super(Weapon, self).__init__(name, description, room)
        self.damage = damage_ratio
        self.magazine = magazine
##


class Consumable(Item):
    def __init__(self, name, description, room):
        super(Consumable, self). __init__(name, description, room)
        self.eaten = False
# Fix this


class Wearable(Item):
    def __init__(self, name, description, room, ):
        super(Wearable, self). __init__(name, description, room)
        self.Worn = False
    # method for wear

    def wear(self):
        if Wearable in inventory:
            print("would you like to wear %s" % self.name)
        else:
            if Wearable not in len(inventory):
                print("You can't wear that, what is wrong is you ")


class Range(Weapon):
    def __init__(self, name, description, room, damage_ratio, magazine):
        super(Range, self).__init__(name, description, damage_ratio, room, magazine)
        self.magazine = magazine


class Arcade_machine(Item):
    def __init__(self, name, description, room, action,):
        super(Arcade_machine, self).__init__(name, description ,room)
        self.action = action


class Melee(Weapon):
    def __init__(self, name, description, room, damage_ratio):
        super(Melee, self).__init__(name, description, damage_ratio, room, None)


class Crowbar(Melee):
    def __init__(self, name, description, room, damage_ratio):
        super(Crowbar, self).__init__(name, description, room, damage_ratio)

    def open_hatch(self):
        print("You have open the hatch. You hesitate to go down")

    def cr_attack(self):
        if crow_bar in command:
            print(crow_bar.damage)


class Knife(Melee):
    def __init__(self, name, description, room, damage_ratio):
        super(Knife, self).__init__(name, description, room, damage_ratio)

    def action(self):
        print("You use the knife to defend yourself but failed. You lost your will to live.")

    def kn_attack(self):
        if knife in command:
            print(crow_bar.damage)


class Flare_gun(Range):
    def __init__(self, name, description, room, damage_ratio, magazine):
        super(Flare_gun, self).__init__(name, description, room, damage_ratio, magazine)

    def signal(self):
        print("You shot at the sky to get signal your position. You're save")


class Flare_ammo(Item):
    def __init__(self, name, description, room,):
        super(Flare_ammo, self).__init__(name, description, room)

    def reload(self):
        print("you inputted a shell")


class Ball_pit(Item):
    def __init__(self, name, description, room):
        super(Ball_pit, self).__init__(name, description , room)


class Flashlight(Item):
    def __init__(self, name, description, room):
        super(Flashlight, self).__init__(name, description, room)

    def turn_on(self):
        print("You turn on the flashlight")

    def turn_off(self):
        print("You turn off your flashlight")


class Battery(Item):
    def __init__(self, name, description, room):
        super(Battery, self).__init__(name, description, room)

    def reload(self):
        print("you use the battery to charge your flashlight")


class Mic(Item):
    def __init__(self, name, description, room):
        super(Mic, self).__init__(name, description, room)


class Cupcake_fake(Item):
    def __init__(self, name, description, room):
        super(Cupcake_fake,self).__init__(name, description, room)


class Guitar(Item):
    def __init__(self, name, description, room ):
        super(Guitar, self).__init__(name, description, room)


class Potion(Item):
    def __init__(self, name, description, room, affect):
        super(Potion, self).__init__(name, description, room)
        self.affect = affect


class Strenth_potion(Potion):
    def __init__(self, name, description ,room , affect):
        super(Strenth_potion, self).__init__(name, description, room, affect)

    def drink(self):
        print("Your strength increase dramatically")


class Night_vision_potion(Potion):
    def __init__(self, name, description, room, affect):
        super(Night_vision_potion, self).__init__(name, description, room, affect)

    def drink(self):
        print("You're able to see the dark for a brief time")


class Bag_of_holding(Wearable):
    def __init__(self, name, description, room,):
        super(Bag_of_holding, self).__init__(name, description, room,)


class Pizza(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Pizza,self).__init__(name, description, room)

    def eat(self):
        print("You ate the pizza")
        self.eaten = True


class Cupcake(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Cupcake, self).__init__(name, description, room)

    def eat(self):
        print("You ate the cupcake, nothing happen what did you expected")
        self.eaten = True


class Water_bottle(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Water_bottle, self).__init__(name, description, room)

    def eat(self):
        print("You drink a water bottle, nothing happen")
        self.eaten = True


class Hat(Wearable):
    def __init__(self, name, description, room,):
        super(Hat, self).__init__(name, description, room,)


class Cape(Wearable):
    def __init__(self, name, description, room,):
        super(Cape, self).__init__(name, description, room)


class Bloody_shirt(Item):
    def __init__(self, name, description, room):
        super(Bloody_shirt, self).__init__(name, description, room)


class Telephone(Item):
    def __init__(self, name, description, room):
        super(Telephone, self).__init__(name, description, room)

    def answer(self):
        print("you'll die in three hours")

class Hook(Melee):
    def __init__(self, name, description, damage_ratio):
        super(Hook, self).__init__(name, description, None, damage_ratio)
####


class Character(object):
    def __init__(self, name, description, inventory, stats, items, action, jump_scare,):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.items = items
        self.action = action
        self.jump_scare = jump_scare

person1 = Character('Henry',
                    "you took this job because you needed money. Your wife and three kids just wanted to have a better "
                    "life."
                    "you found this job on ebay? what, What wrong with you ",
                    'Flashlight',
                    ' H = 100',
                    None, None, None)
Bonnie = Character('Bonnie',
                    "Bonnie is a fun bunny which bring joy around the pizzeria. But then again it smell like a dead bod-"
                    "something",
                    None, ', H = 100', 'guitar',
                    'play the guitar', "you become blind and paralyzed")
Freddy = Character('Freddy Fazbear',
                   "Freddy is the most lovable bear in the whole pizzeria. He liked the star of the band. But every"
                   "time he sing it sound like a dead man crying, trying to get out. but who knows.",
                   None, 'H = 100', 'Mic', 'Sing', "you become blind and paralyzed")
Chica = Character('Chica', "Chica is a duck like animatronic who soul purpose is to give out cupcake. but we don't "
                  "know what inside of those cupcake maybe bloo-. its made organic.)",
                  None, 'H = 100', 'Cupcake', "give out cupcakes", "you become blind and paralyzed.")
Foxy = Character('Foxy', "Foxy is in the back stage most of the time because he's shy. His fur is always red but it"
                 " used to be white. We think that an employee colored it red. But it started to smell.",
                 None, 'H = 100', "a Hook", None, "you become blind and paralyzed.")
Ballora = Character('Ballora', "She a fun charter, like to sing, dance, and to put on a show",
                    None, "H = 100", None, "dance", "you become blind and paralyzed.")
Fun_time_Freddy = Character("Fun time Freddy",
                            "He's a lovable character which was used in the last pizzeria but run out"
                            "business because of a weird smell and a disappearance of children.",
                            None, "H = 100", None, "play with children", "you become blind and paralyzed.")
Fun_time_Foxy = Character("Fun Time Foxy", "She's the sister of Foxy but have a few improvement over Foxy. But we "
                          "saw something very strange in the old security camera of a child disappearing and Fun time "
                          "Foxy came out.", None, "H = 100", None, "Dance",
                          "you become blind and paralyzed.")
Baby = Character("Baby",
                 "Baby was made to take care and make kids happy. But they started to disappear when they go "
                 "and play with Baby.", None, "H = 100", None,
                 "dance and sing", "you become blind and paralyzed.")
Puppet = Character("Puppet", "she going to protect all the children from harm, and from you", None, "H = 100", None,
                   "roams around",None)

####
class Room(object):
    def __init__(self, name, description, north, west, east, south, up, down, character, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.items = items
        self.character = character




    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]


####
person1 = person1
bonnie = Bonnie
freddy = Freddy
chica = Chica
foxy = Foxy
ballora = Ballora
fun_time_freddy = Fun_time_Freddy
fun_time_foxy = Fun_time_Foxy
baby = Baby
puppet = Puppet
arcade_machine = Arcade_machine("arcade machine", "This machine is out of order", None, "explode")

crow_bar = Crowbar("crow bar", "You can use this to fight off thing, or open a hatch", None, '25')

knife = Knife("knife", "You use the knife to fight of thing or cook. tee-hee", None, '25')

flare_gun = Flare_gun("flare gun", "You can signal for help or light the way up.", None, '15', '4')

flare_ammo = Flare_ammo("flare ammo", "You can use this to reload your flare gun, There nothing else you can do woth it"
                                      ".", None,)

ball_pit = Ball_pit("ball pit", " Kids love this ball pit, but for some reason kids are going missing.", None)

flashlight = Flashlight("flashlight", "The flashlight is use to light of the wae. It runs out real fast though", None)

battery = Battery("battery", "It a battery what else can you use it for", None)

mic = Mic("mic", "Property of Freddy", None)

cupcake_fake= Cupcake_fake("the plastic cupcake", "This is one of the missing cupcake of Chika collection. If you give "
                                                  "it to her then you get a prized of dea-, of good things.", None)

guitar = Guitar("guitar", "This guitar have something on it like blo- red paint.", None)

strength_potion = Strenth_potion("strength potion", "This potion is one of a kind very rare very useless.", None, "you "
                                 "got stronger. ")

night_vision_potion = Night_vision_potion("night vision potions", "You will be able to see in the dark once you drank "
                                                                  "the potion.", None, "you can see in the dark")

bag_of_holding = Bag_of_holding("bag of holding", "You could hold endless amount of item but at a cost of 10 health.",
                                None)

pizza = Pizza("pizza", "this pizza is made from the top chief in the garbage. *Don't eat it*", None)

cupcake = Cupcake("cupcake", "This is a very treat from the most lovable character in the pizzaia death", None)

water_bottle = Water_bottle("water bottle", "This is the most freshest water bottle you will every see in the world."
                                            "It's from our very own toilet. ", None)
hat = Hat("hat", "This hat said to belong to a child who have gone missing for a month. There even a name. *Run*", None)

cape = Cape("cape", "This 'cape' said to give you magical power but there just blood.", None)

bloody_shirt = Bloody_shirt("bloody shirt", "Who knows where this shirt came from.", None)

telephone = Telephone("telephone", "This telephone is my only way to escape. There seem to be a battery missing.", None)

hook = Hook("hook", "The hook was made from the dead bodies of children, what.", "you deal 25 damage")

ENTRANCE = Room('Freddy Fazbear Entrance',
                'Your at the entrance of the new place where your going to work. The place is called '
                'Freddy Fazbear pizzaera',
                'WAITING_ROOM', None, 'SECURITY_PUPPET_ROOM', None, None, None, person1 ,None )

SECURITY_PUPPET_ROOM = Room('security puppet room',
                            'This room will protect children who are trying to leave without their parent.',
                            None, 'ENTRANCE', None, None, None, None, puppet, [flashlight])
WAITING_ROOM = Room('Waiting Room',
                    'This place is were people will wait until they could get a bracelet to enter the playhouse.',
                    'DINNING_ROOM', 'BATHROOM', 'OFFICE_ROOM', 'ENTRANCE', None, None, None, [water_bottle])
OFFICE_ROOM = Room('Office Room',
                   'This place is were the manger is going work. maybe',
                   None, 'WAITING_ROOM', 'DATA_BASE', None, None, None, freddy,[knife])
BATHROOM = Room('Bathroom',
                "You know why you're here. There seem to be a hatch in one of the stalls. would you like to open it?",
                None, None, 'WAITING_ROOM', None, None, 'BELOW_BUILDING', None, [flare_gun])
DINNING_ROOM = Room('Dinning Room',
                    'Here were your going to eat after or before you go into the buffet.',
                    'STAGE', 'GAME_ROOM', 'FOOD_ROOM', 'WAITING_ROOM', None, None, chica, [pizza, cupcake])
GAME_ROOM = Room('Game Room',
                 'This place is were your children going to play games.',
                 None, 'FOXY_ROOM', 'DINNING_ROOM', None, None, None, None, [arcade_machine])
FOXY_ROOM = Room('Foxy Room',
                 'Foxy is the most lovable character.',
                 None, None, 'GAME_ROOM', None, None, None, foxy, [strength_potion])
FOOD_ROOM = Room('Food Room',
                 'Do you not known why we use this place.',
                 None, 'DINNING_ROOM', None, None, None, None, None, [water_bottle, cupcake_fake])
STAGE = Room('Stage',
             'This is were the animatronic is going to perform. We have Freddy, Bonnie, and chika. there a hat on the '
             'ground',
             'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None, [freddy, bonnie, chica], [hat])
STORAGE_ROOM = Room('Storage Room',
                    'This is were we keep extras stuff. Like a dead bo- dead battery.',
                    'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None, None, [crow_bar])
BACK_OF_THE_BUILDING = Room('Back of the building',
                            'There nothing here but blo- balloons.',
                            'SECURITY_ROOM', 'STORAGE_ROOM', 'STAFF_ROOM', 'STORAGE_ROOM', None, None, None,
                            [bloody_shirt])
SECURITY_ROOM = Room('Security Room',
                     'This is were your going to work.',
                     None, None, None,'BACK_OF_THE_BUILDING', None, None, None,[flashlight, flare_gun])
STAFF_ROOM = Room('Staff Room',
                  'Other staff will take a break in here.',
                  'BACK_OF_THE_BUILDING', None, 'ANIMATRONICS', None, None, None, None, [flare_ammo])
ANIMATRONICS = Room('Animatronics room',
                    "There are 4 animatronics that are a work in progress.",
                    None, 'STAFF_ROOM', None, 'DATA_BASE', None, None, None, [mic, battery])
DATA_BASE = Room('Data base',
                 'This is were we controlled the animatronics.',
                 'ANIMATRONICS', 'OFFICE', None, None, None, None, None, [hook])
BELOW_BUILDING = Room('Below building',
                      'You fell and found a strange place. it dark.',
                      None, None, 'ELEVATOR', None, 'BATHROOM', None, None, None)
ELEVATOR = Room('Elevator',
                'It seem the elevator take you below or up. Would you like to go up or down?',
                'CONTROL_ROOM', 'BELOW_BUILDING', 'NOTHING', None, 'BATHROOM', 'CONTROL_PANEL', None, None)
NOTHING = Room('Nothing',
               'There nothing here but rocks.',
               None, 'ELEVATOR', None, None, None, None, None, [bag_of_holding])
CONTROL_PANEL = Room('Control panel',
                     'There seem to be a button that does something.',
                     'CONTROL_PANEL_2', None, 'BALLORA_AUDITORIUM', 'ELEVATOR', None, None, None, [cape])
BALLORA_AUDITORIUM = Room('Ballora Auditorium',
                          "'There seem to be something there but can't make out what it is.",
                          'FUN_TIME_AUDITORIUM', 'CONTROL_PANEL', None, None, None, None, ballora, None)
FUN_TIME_AUDITORIUM = Room('Fun time Auditorium',
                           "There also something there but can't make out what it is",
                           None, 'FOXY_AUDITORIUM', None, 'BALLORA_AUDITORIUM', None, None, fun_time_freddy, [guitar])
FOXY_AUDITORIUM = Room('Foxy Auditorium',
                       'You hear something but was to fainted to figure out.',
                       None, None, 'FUN_TIME_AUDITORIUM', None, None, None, fun_time_foxy, None)
CONTROL_PANEL_2 = Room('Control Panel for Baby',
                       'There are a lot of button that does something. but what?',
                       None, None, None, 'CONTROL_PANEL', None, None, None)
BABY_AUDITORIUM = Room('Baby Auditorium',
                       'you find something very odd, familiar, but    there something     very     disturbing.',
                       None, None, None, 'CONTROL_PANEL_2', None, None, baby, [telephone])

current_node = ENTRANCE
direction = ['north', 'south', 'east', 'west', 'up', 'down']
short_direction = ['n', 's', 'e', 'w', 'u', 'd']
print(person1.description)
print(current_node.name)
print(current_node.description)
while True:
    random_number = random.randint(1, 3)
    print(person1.stats)
    for list_items in current_node.items:
        if list_items.isTaken is False:
            print(list_items.name)
    command = input(':').lower().strip()
    if command == 'quit':
        quit(0)
    if command in short_direction:
        pos = short_direction.index(command)
        command = direction[pos]
    if command in direction:
        try:
            current_node.move(command.lower())
            print(current_node.name)
            print(current_node.description)
        except KeyError:
            print("Are you a baka, there is nothing there")
    elif "pick up" in command:
        for item in current_node.items:
            if item.name in command:
                item.take()
                break
            else:
                print("You can't take that.")
                break
    elif "drop" in command:
        if not inventory:
            print("There nothing in your inventory")
        else:
            for item in inventory:
                if item.name.lower() in command:
                    item.drop()
                else:
                    print("what are you saying there nothing inside your inventory.")
# fix the drink, and eat
    elif "drink" in command:
        if Consumable in inventory:
            print("would you want a drink.")
            for item in inventory:
                if item.name.lower() in command:
                    print("You drank the item.")
    elif "look at" in command:
        for item in inventory:
            if item.name.lower() in command:
                print(item.name)
                print(item.description)
    # elif "take all" in command:
    #     for item in current_node.items:
    #         if item.name in command:
    #             print("You took everything.")

    elif command == "win game":
        print("You won the game")
        break
    elif command == "look up":
        print("Type in win game")
    elif command == "inventory":
        for item in inventory:
            print(item.name)
    elif command == "shoot":
        print(random_number)
        if random_number == 2:
            print("You're able to land a hit.")
            print("You dealt %s" % flare_gun.damage)
        elif flare_gun not in inventory:
            print("you can't fire anything")
        elif flare_gun.magazine == 0:
            print("you can't fire anything")
        else:
            print("you missed the shot.")

    elif command == "look":
        print(current_node.name)
        print(current_node.description)
    else:
        print("Command unknown, are you a baka")





