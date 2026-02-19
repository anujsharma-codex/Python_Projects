while True:
    user_input = input("Enter an integer (press Enter to stop): ").strip()

    if user_input == "":
        print("Thank you.")
        break

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")