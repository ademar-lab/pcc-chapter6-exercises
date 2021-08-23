# Store the characteristics of a person in a dictionary
alex = {"first_name": "alex", "last_name": "nájera", "age": 17,
        "city": "salamanca", "height": 175}

print("This are Alex's characteristics")
for key, value in alex.items():
    print(f"\t{key}: {value}")