favorite_places = {}
while True:
    name = input("Enter your name: ").strip().title()
    places = []
    print("Enter up to 3 favorite places (type 'done' to stop):")
    count = 0
    while count < 3:
        place = input(f"Favorite place {count + 1}: ").strip()
        if place.lower() == "done":
            break
        if place == "":
            print("Place name cannot be empty.")
            continue
        places.append(place.title())
        count += 1
    favorite_places[name] = places
    more = input("Is anyone left? (y/n): ").strip().lower()
    if more != "y":
        break
#output
print("\nFavorite Places:\n")
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()