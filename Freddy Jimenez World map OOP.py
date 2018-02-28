class Room(object):
    def __init__(self, name, description, north, west, east, south, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]

ENTRANCE = Room('Freddy Fazbear Entrance',
                'Your at the entrance of the new place where your going to work. The place is called'
                'Freddy Fazbear pizzaera',
                True, False, True, False, False, False)
               )
SECURITY_PUPPET_ROOM = Room(('security puppet room',
                             'This room will protect children who are trying to leave without their parent.'
)

#current_node = rooms
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']
other_direction = ['UP', 'DOWN']
while True:
    print(current_node['NAME']) # change
    print(current_node['DESCRIPTION']) # change
    command = input('>_')
    if command == 'quit':
        quit(0)

    if command in direction and other_direction:
        try:
           # change
        except KeyError:
            print("Are you a baka, there is nothing there")
    else:
        print("Command unknown, are you a baka")


