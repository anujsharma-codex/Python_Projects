def sandwich_summary(bread, *fillings, **details):
    print(f"\nMaking a {bread} sandwich with:")
    for item in fillings:
        print(f"- {item}")
    if details:
        print("Extra details:")
        for key, value in details.items():
            print(f"  {key}: {value}")
# Function calls with different arguments
sandwich_summary(
    "Whole Wheat",
    "Cheese", "Tomato")
sandwich_summary(
    "Sourdough",
    "Chicken", "Lettuce", "Mayonnaise",
    salt="low")
sandwich_summary(
    "Ciabatta",
    "Paneer", "Onion", "Capsicum", "Sauce",
    grill=True,
    oil="less",
    spice_level="medium")