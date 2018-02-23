class Room(object):
    def __init__(self, description, name, north, west, east, south, up, down):
        self.description = description
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]


rooms = Room()

current_node = rooms
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


