# Store people's favorite lenguages
favorite_lenguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
    }

# Store a list of people left to poll
people_to_poll = ["miguel", "sarah", "alex", "jen", "diana"]

for person in people_to_poll:
    if person in favorite_lenguages.keys():
        print(f"Thanks for taking the poll {person.title()}!")
    else:
        favorite_lenguages[person] = print("What is your favorite language? ")