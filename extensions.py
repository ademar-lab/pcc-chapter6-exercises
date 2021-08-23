# This program takes the people.py file and makes some modifications

# Store characteristics of 3 different people in a dictionary
people = {
    "alex": {
    "first_name": "alex",
    "last_name": "nájera",
    "age": 17,
    "city": "salamanca",
    "height": 175,
    },

    "ademar": {
    "first_name": "ademar",
    "last_name": "de león",
    "age": 17,
    "city": "salamanca",
    "height": 175,
    },

    "miguel": {
    "first_name": "miguel",
    "last_name": "garcía",
    "age": 17, 
    "city": "salamanca",
    "height": 170,
    },
}

# Print each person's characteristics
for person, data in people.items():
    print(f"\nThese are {person.title()}'s characteristics")
    for key, value in data.items():
        print(f"\t{key}: {value}")