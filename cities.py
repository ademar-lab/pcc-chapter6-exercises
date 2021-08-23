# Store some cities and their characteristics
cities = {
    "vancouver": {
        "country": "canada",
        "population": 675_218,
        "fact": "Vancouver was recently ranked as the third most" 
        " \"livable place in the world\"",
    },
    "auckland": {
        "country": "new zeland",
        "population": 1_470_100,
        "fact": "Auckland is home to over 50 volcanoes",
    },
    "tokyo": {
        "country": "japan",
        "population": 37_393_128,
        "fact": "Tokyo is the world's most populous metropolitan area",
    },
}

# Print each city and its characteristics
for city, characteristics in cities.items():
    print(f"\n{city.title()}:")
    for key, value in characteristics.items():
        if value == "canada":
            print(f"\t{key}: {value.title()}")
        else:
            print(f"\t{key}: {value}")