class Character(object):
    def __init__(self, name, description, inventory, stats, items, pickup, jump_scare):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.items = items
        self.pickup = pickup
        self.jump_scare = jump_scare

    def jump_scare(self):
        print("you become blind and paralized")

    # def person(self, name):
    #     print("Your name is %s" % name)
    #
    # def profile(self):
    #    print("you took this job because you needed money. Your wife and three kids just wanted to have a better life."
    #           "you found this job on ebay? what. What wrong with you ")
    #
    # def thing(self):
    #     print("you only got a flashlight")


person1 = Character('jeff',
                    "you took this job because you needed money. Your wife and three kids just wanted to have a better"
                    "life."
                    "you found this job on ebay? what. What wrong with you ",
                    'Flashlight',
                    'H = 100, S = 100',
                    None, None, None)

print(person1.name, person1.stats,)
command = input(":")


