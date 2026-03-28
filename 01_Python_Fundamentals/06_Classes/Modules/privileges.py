class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        if not self.privileges:
            print("- No privileges assigned")
        for privilege in self.privileges:
            print(f"- {privilege}")
