# Store characteristics of 3 different people in a dictionary
people = []
alex = {
    "first_name": "alex",
    "last_name": "nájera",
    "age": 17,
    "city": "salamanca",
    "height": 175,
    }
people.append(alex)

ademar = {
    "first_name": "ademar",
    "last_name": "de león",
    "age": 17,
    "city": "salamanca",
    "height": 175,
    }
people.append(ademar)

miguel = {
    "first_name": "miguel",
    "last_name": "garcía",
    "age": 17, 
    "city": "salamanca",
    "height": 170,
    }
people.append(miguel)

# Print each person's characteristics
for person in people:
    name = person["first_name"].title()
    print(f"\nThese are {name}'s characteristics")
    for key, value in person.items():
        print(f"\t{key}: {value}")