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
                'WAITING_ROOM', None, 'SECURITY_PUPPET_ROOM', None, None, None,
                )

SECURITY_PUPPET_ROOM = Room('security puppet room',
                             'This room will protect children who are trying to leave without their parent.',
                             None, 'ENTRANCE', None, None, None, None
                             )
WAITING_ROOM = Room('Waiting Room',
                     'This place is were people will wait until they could get a bracelet.',
                    'DINNING_ROOM', 'BATHROOM', 'OFFICE', None, None, None
                     )
OFFICE_ROOM = Room('Office Room',
                     'This place is were the manger will work. maybe',
                     None, 'WAITING_ROOM', 'DATA_BASE', None, None, None
                     )
BATHROOM = Room('Bathroom',
                     "You know why you're here.",
                     None, None, 'WAITING_ROOM', None, None, 'BELOW_BUILDING'
                     )
DINNING_ROOM = Room('Dinning Room',
                     'Here were your going to eat after or before you go into the buffet.',
                    'STAGE', 'GAME_ROOM', 'FOOD_ROOM', 'WAITING_ROOM', None, None
                     )
GAME_ROOM = Room('Game Room',
                     'This place is were your children going to play games.',
                    None, 'FOXY_ROOM', 'DINNING_ROOM', None, None, None
                     )
FOXY_ROOM = Room('Foxy Room',
                     'Foxy is the most lovable character.',
                    None, None, 'GAME_ROOM', None, None, None
                     )
FOOD_ROOM = Room('Food Room',
                     'Do you not known why we use this place.',
                    None, 'DINNING_ROOM', None, None, None, None
                     )
STAGE = Room('Stage',
                     'This is were the animatronic is going to perform.',
             'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None
                     )
STORAGE_ROOM = Room('Stage',
                     'This is were the animatronic is going to perform.',
             'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None
                     )
BACK_OF_THE_BUILDING = Room('Back of the building',
                     'There nothing here but blo- balloons.',
             'SECURITY_ROOM', 'STORAGE_ROOM', 'STAFF_ROOM', 'STORAGE_ROOM', None, None
                     )
SECURITY_ROOM = Room('Security Room',
                     'This is were your going to work.',
             None, None, None, 'BACK_THE_BUILDING', None, None
                     )
STAFF_ROOM = Room('Staff Room',
                     'Other staff will take a break in here.',
                  'BACK_OF_THE_BUILDING', None, 'ANIMATRONICS', None, None, None
                     )
ANIMATRONICS = Room('Animatronics room',
                     "There are 4 animatronics that are a work in progress.",
                  'CLOSED_OF_ROOM', 'STAFF_ROOM', None, 'DATA_BASE', None, None
                     )
DATA_BASE = Room('Data base',
                     'This is were we controlled the animatronics.',
                  'ANIMATRONICS', None, None, 'OFFICE', None, None
                     )
BELOW_BUILDING = Room('Below building',
                     'You fell and found a strange place. it dark.',
                  None, None, 'ELEVATOR', None, 'BATHROOM', None
                     )
ELEVATOR = Room('Elevator',
                     'It seem the elevator take you below or up. Would you like to go up or down?',
                'CONTROL_ROOM', 'BELOW_BUILDING', 'NOTHING', None, 'BATHROOM', 'CONTROL_PANEL'
                     )
NOTHING = Room('Nothing',
                     'There nothing here but rocks.',
                None, 'ELEVATOR', None, None, None, None
                     )
CONTROL_PANEL = Room('Control panel',
                     'TThere seem to be a button that does something.',
                None, 'ELEVATOR', None, None, None, None
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


