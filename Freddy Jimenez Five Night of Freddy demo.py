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
        'NAME': 'Freddy Fazbear Entrance',
        'DESCRIPTION': 'Your at the, and your started your fist day of work',
        #'LETTER': 'This is the first day of your job hope you enjoy. Your first job is to search the whole place'
        'PATHS': {
            'EAST': 'Security Puppet Room',
            'NORTH': 'Waiting room'
        }
    }
},

