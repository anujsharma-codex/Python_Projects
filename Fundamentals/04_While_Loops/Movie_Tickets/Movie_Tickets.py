print("Movie Ticket Pricing Based on Age")
print("Enter your age to see the ticket price.\n")
while True:
    user_input = input("Enter your age (type 'quit' to stop): ").strip()
    if user_input.lower() == "quit":
        print("Enjoy your show.")
        break
    try:
        age = int(user_input)
    except ValueError:
        print("Invalid input. Please enter your age as a number.")
        continue
    if age <= 0:
        print("Invalid age.")
    elif age < 3:
        print("Ticket price: Free")
    elif age <= 12:
        print("Ticket price: $10")
    else:
        print("Ticket price: $15")