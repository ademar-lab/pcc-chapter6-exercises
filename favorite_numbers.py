# Store the favorite numbers of 5 people
favorite_numbers = {
    "miguel": [12, 3, 22],
    "ademar": [75, 8],
    "violeta": [33],
    "dana": [2, 99, 76],
    "marco": [7, 3],
    }

# Ask users if they want to take the poll
run = input("Do you want to tell us what is your favorite number?"
             "\nType \"n\" if you don't ")

while run != "n":
    name = input("what is your name? ")
    if name == "n":
        break

    # Ask for their favorite numbers
    favorite_number = ""
    while type(favorite_number) != int:
        favorite_number = input("What is your favorite number? ")
        try:
            int(favorite_number)
        except ValueError:
            if favorite_number == "n":
                break
            else:
                print("\nYou have to introduce a number!")
        else:
            favorite_number = int(favorite_number)

    run = input("Do you want to let more people take the poll?"
                "\nType \"n\" if you don't ")

# End the program
print("\nThese are the results from the poll:")
for person, number in favorite_numbers.items():
    print(f"\t{person}: {number}")
exit()