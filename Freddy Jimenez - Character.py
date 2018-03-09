class Character(object):
    def __init__(self, name, description, inventory, stats, items, action, jump_scare):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.items = items
        self.action = action
        self.jump_scare = jump_scare

    def jump_scare(self):
        print("you become blind and paralyzed")

    # def person(self, name):
    #     print("Your name is %s" % name)
    #
    # def profile(self):
    #    print("you took this job because you needed money. Your wife and three kids just wanted to have a better life."
    #           "you found this job on ebay? what. What wrong with you ")
    #
    # def thing(self):
    #     print("you only got a flashlight")


person1 = Character('Jeff',
                    "you took this job because you needed money. Your wife and three kids just wanted to have a better"
                    "life."
                    "you found this job on ebay? what. What wrong with you ",
                    'Flashlight',
                    ' H = 100, S = 100',
                    None, None, None)
Bonnie = Character('Bonnie',
                   "Bonnie is a fun bunny which bring joy around the pizzaria. But then again it smell like a dead bod-"
                   "something",
                   None,', H = 100 s = 0', 'guitar',
                   'play the guitar', "you become blind and paralyzed")
Freddy = Character('Freddy Fazbear',
                   "Freddy is the most loveable bear in the whole pizzaria. He liked the star of the band. But every"
                   "time he sing there like a dead man crying trying to get out. but who knows.",
                   None,'H = 100, s = 0','Mic', 'Sing', "you become blind and paralyzed")
Chica = Character('Chica', "Chica is a duck like animatronics who soul purpose is to give out cupcake. but we don't"
                  "know what inside of those cupcake maybe bloo-. its made organic.;)",
                  None, 'H = 100, S = 0', 'Cupcake', "give out cupcakes", "you become blind and paralyzed.")
Foxy = Character('Foxy', "Foxy is in the back stage most of the time because he's shy. his fur is always red but it"
                         " used to be white. We think that an employee colored it red. But it started to smell.",
                 None,'H = 100, S = 0',"a Hook", None,"you become blind and paralyzed.")


print(Foxy.description,)
print(Chica.description)
command = input(":")


