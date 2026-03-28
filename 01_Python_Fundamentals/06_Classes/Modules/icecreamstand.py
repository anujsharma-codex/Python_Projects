class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type ):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=["Chocolate","Vanilla","Strawberry","Kesar Pista","Taj Mahal"]

    def describe_flavors(self):
        print("Flavors: ")
        for flavor in self.flavors:
            print(" -"+flavor)