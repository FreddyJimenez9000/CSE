# Dictionary = made up of key: value pair
dictionary = {"name": 'bob', 'age': 1000, 'height': 6 * 12 + 6}

# Accessing thing from a dictionary

print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

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





















