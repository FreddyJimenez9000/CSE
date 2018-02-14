'''world_map = {
    'WESTHOUSE': {
        'MAME': 'West of House',
        'DESCRIPTION':'You are west of a whit house',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'

        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}'''

Five_Night_Freddy = {
    'ENTRANCE': {
        'NAME': 'FreddyFazbear Entrance',
        'DESCRIPTION': 'Your at the entrance of the new place where your going to work. The place is called Freddy'
                       'Fazbear pizzaera.',
        'PATHS': {
            'EAST': 'Security Puppet Room',
            'NORTH': 'Waiting room'
         }
    },
    'SECURITY PUPPET ROOM': {
        'NAME': 'Security Puppet Room',
        'DESCRIPTION': 'This room will protect children who are trying to leave without their parent.',
        'PATHS': {
            'WEST': 'Entrance'
        }
    },
    'WAITING ROOM': {
        'NAME': 'WAITING ROOM',
        'DESCRIPTION': 'This place is were people will wait until they could get a bracelet.',
        'PATHS': {
            'NORTH': 'DINNER ROOM',
            'WEST': 'WAITING ROOM',
            'EAST': 'BATHROOM'
        }
    },

}


current_node = Five_Night_Freddy['ENTRANCE']
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)

    if command in direction:
        try:
            name_of_node = current_node['PATHS'][command]
            print(name_of_node)
            current_node = Five_Night_Freddy[name_of_node]
        except KeyError:
            print("Are you a baka, there is nothing there")
    else:
        print("Command unknown, are you a baka")
