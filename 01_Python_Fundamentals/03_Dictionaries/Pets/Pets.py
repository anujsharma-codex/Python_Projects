def get_pet_details():
    pet_name = input("Enter pet name: ").strip()
    animal_type = input("Enter pet type: ").strip()
    owner_name = input("Enter owner's name: ").strip()

    return {
        "name": pet_name.title(),
        "animal_type": animal_type.title(),
        "owner": owner_name.title()
    }


def display_pets(pets):
    for index, pet in enumerate(pets, start=1):
        print("\n{}. PET NAME: {}".format(index, pet["name"]))
        print("\tPET TYPE: {}".format(pet["animal_type"]))
        print("\tOWNER: {}".format(pet["owner"]))


def main():
    pets = []

    while True:
        pets.append(get_pet_details())

        choice = input("Do you want to add another pet? (y/n): ").strip().lower()
        if choice != "y":
            break

    display_pets(pets)

main()