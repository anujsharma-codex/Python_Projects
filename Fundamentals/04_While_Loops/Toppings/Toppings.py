toppings = []
print("Let's add toppings to your pizza.")
print("Type 'quit' when you are done.\n")
while True:
    topping = input("Enter a topping: ").strip()

    if topping.lower() == "quit":
        break
    if topping == "":
        print("Topping cannot be empty.")
        continue
    toppings.append(topping.title())
    print(f"I will add {topping.title()} to your pizza.")

print("\nYour pizza will have the following toppings:")
for index, topping in enumerate(toppings, start=1):
    print(f"{index}. {topping}")
