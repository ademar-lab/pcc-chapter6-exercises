# Store 3 major rivers
rivers = {"amazon": "brazil",
          "brahmaputra": "india", 
          "mississippi": "the united states"
         }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nRivers:")
for river in rivers.keys():
    print(f"{river.title()}")

print("\nCountries")
for country in rivers.values():
    print(f"{country.title()}")