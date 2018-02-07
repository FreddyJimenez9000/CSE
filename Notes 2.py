# Dictionary = made up of key: value pair
dictionary = {"name": 'bob', 'age': 1000, 'height': 6 * 12 + 6}

# Accessing thing from a dictionary

print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Add a pair to a dictionary
dictionary["profession"] = "telemarketer"

large_dictionary = {
    'CA': 'California',
    'NY': 'New York',
    'AZ': 'Arizona'
}
print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'San Francisco',
        'San Jose'
    ],
    'NY': [
        "New York city",
        "Brooklyn"
    ],
    'AZ': [
        'Phoenix',
        'Tuscon'
    ]
}

print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
print(larger_dictionary['AZ'][0])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada'
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': {
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
         }
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': {
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        }
    }

}
current_node = largest_dictionary['NY']
print(current_node['NAME'])
print(current_node['POPULATION'])















