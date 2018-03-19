inventory = []
print("there a mic on the ground")
command = input(":").lower()

class Item(object):
    def __init__(self, name,desciption, pick_up, room):
        self.name = name
        self.desciption = desciption
        self.Pickup = pick_up
        self.fromroom = room


    

    # def Pick_up(self):
    #     if command == "pickup %s" % self.name:
    #         print("you pick up %s" % self.name)
    #         inventory.append(command)
    #
    # if command == "inventory":
    #    print(inventory)
#