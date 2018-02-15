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
            'EAST': 'SECURITY PUPPET ROOM',
            'NORTH': 'WAITING ROOM'
         }
    },
    'SECURITY PUPPET ROOM': {
        'NAME': 'Security Puppet Room',
        'DESCRIPTION': 'This room will protect children who are trying to leave without their parent.',
        'PATHS': {
            'WEST': 'ENTRANCE'
        }
    },
    'WAITING ROOM': {
        'NAME': 'WAITING ROOM',
        'DESCRIPTION': 'This place is were people will wait until they could get a bracelet.',
        'PATHS': {
            'NORTH': 'DINNING ROOM',
            'WEST': 'WAITING ROOM',
            'EAST': 'BATHROOM'
        }
    },
    'OFFICE ROOM': {
        'NAME': 'OFFICE ROOM',
        'DESCRIPTION': 'This place is were people will wait until they could get a bracelet.',
        'PATHS': {
            'WEST': 'WAITING ROOM',
            'EAST': 'DATA BASE'
        }
    },
    'BATHROOM': {
        'NAME': 'BATHROOM',
        'DESCRIPTION': 'LOL',
        'PATHS': {
            'EAST': 'WAITING ROOM',
            'DOWN': 'BELOW BUILDING'
        }
    },

    'DINNING ROOM': {
        'NAME': 'DINNING ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'STAGE ',
            'WEST': 'GAME ROOM',
            'EAST': 'FOOD ROOM',
            'SOUTH': 'WAITING ROOM'
        }
    },
    'GAME ROOM': {
        'NAME': 'GAME ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'WEST': 'FOXY ROOM',
            'EAST': 'DINNING ROOM'
        }
    },
    'FOXY ROOM': {
        'NAME': 'FOXY ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'EAST': 'GAME ROOM'
        }
    },
    ' FOOD ROOM': {
        'NAME': 'FOOD ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'WEST': 'DINNING ROOM'
        }
    },
    'STAGE': {
        'NAME': 'STAGE',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING',
            'WEST': 'STORAGE ROOM',
            'SOUTH': 'DINNING ROOM'
        }
    },
    'STORAGE ROOM': {
        'NAME': 'STORAGE ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING ',
            'EAST': 'STAGE'
        }
    },
    'BACK OF THE BUILDING': {
        'NAME': 'BACK OF THE BUILDING',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'SECURITY ROOM',
            'WEST': 'STORAGE ROOM',
            'EAST': 'STAFF ROOM',
            'SOUTH': 'STORAGE ROOM'
        }
    },
    'SECURITY ROOM': {
        'NAME': 'SECURITY ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'BACK OF THE BUILDING'
        }
    },
    'STAFF ROOM': {
        'NAME': 'STAFF ROOM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING',
            'EAST': 'ANIMATRONICS ROOM'
        }
    },
    'ANIMATRONICS': {
        'NAME': 'ANIMATRONICS',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'CLOSED OF ROOM',
            'WEST': 'STAFF ROOM',
            'SOUTH': 'DATA BASE'
        }
    },
    'DATA BASE': {
        'NAME': 'DATA BASE',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'ANIMATRONICS ROOM',
            'SOUTH': 'OFFICE'
        }
    },
    'BELOW BUILDING': {
        'NAME': 'BELOW BUILDING',
        # 'DESCRIPTION': '',
        'PATHS': {
            'UP': 'BATHROOM',
            'EAST': 'ELEVATOR'
        }
    },
    'ELEVATOR': {
        'NAME': 'ELEVATOR',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'CONTROL ROOM',
            'WEST': 'BELOW BUILDING',
            'EAST': 'NOTHING',
            'SOUTH': 'WINDOW'
        }
    },
    'WINDOW': {
        'NAME': 'WINDOW',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'ELEVATOR'
        }
    },
    'NOTHING': {
        'NAME': 'NOTHING',
        # 'DESCRIPTION': '',
        'PATHS': {
            'WEST': 'ELEVATOR'
        }
    },
    'CONTROL PANEL': {
        'NAME': 'CONTROL PANEL',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'CONTROL PANEL 2',
            'EAST': 'BALLORA AUDITORIUM',
            'SOUTH': 'ELEVATOR'
        }
    },
    'BALLORA AUDITORIUM': {
        'NAME': 'BALLORA AUDITORIUM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'NORTH': 'FUNTIME AUDITORIUM',
            'WEST': 'CONTROL PANEL'
        }
    },
    'FUNTIME AUDITORIUM': {
        'NAME': 'FUNTIME AUDITORIUM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'WEST': 'FOXY AUDITORIUM',
            'SOUTH': 'BALLORA AUDITORIUM'
        }
    },
    'FOXY AUDITORIUM': {
        'NAME': 'ELEVATOR',
        # 'DESCRIPTION': '',
        'PATHS': {
            'EAST': 'FUNTIME AUDITORIUM'
        }
    },
    'CONTROL PANEL 2': {
        'NAME': 'CONTROL PANEL FOR BABY',
        # 'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'CONTROL PANEL'
        }
    },
    'BABY AUDITORIUM': {
        'NAME': 'BABY AUDITORIUM',
        # 'DESCRIPTION': '',
        'PATHS': {
            'SOUTH': 'CONTROL PANEL 2'
        }
    },
}

current_node = Five_Night_Freddy['ENTRANCE']
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']
other_direction = ['UP', 'DOWN']
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
