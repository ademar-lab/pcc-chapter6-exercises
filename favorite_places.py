# Store the favorite places of some people
favorite_places = {
    "ademar": ["taj mahal", "the colosseum"],
    "dana": ["the chichen itza", "machu picchu", "the great wall of china"],
    "violeta": ["christ the redeemer", "petra"],
}

for person, places in favorite_places.items():
    print(f"\nThese are {person.title()}'s favorite places:")
    for place in places:
        print(f"\t{place.title()}")