# Store the characteristics of 3 different pets
pets = []
sushi = {
    "kind_of_animal": "tortoise",
    "name": "sushi",
    "owner": "fernanda",
    "age": 1,
}
pets.append(sushi)

keisha = {
    "kind_of_animal": "dog",
    "name": "keisha",
    "owner": "ademar",
    "age": 7,
}
pets.append(keisha)

la_perris = {
    "kind_of_animal": "dog",
    "name": "la perris",
    "owner": "miguel",
    "age": 5,
}
pets.append(la_perris)

for pet in pets:
    name = pet["name"]
    print(f"\nThis is the information about {name}")
    for key, value in pet.items():
        print(f"\t{key}: {value}")