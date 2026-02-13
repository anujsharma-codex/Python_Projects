def remove_extra_spaces(email_list):
    normal_list = []
    for email in email_list:
        normal_list.append(email.strip())
    return normal_list


def extract_usernames(email_list):
    usernames = []
    for email in email_list:
        usernames.append(email.split("@")[0])
    return usernames


def duplicate_elimination(email_list):
    usernames = extract_usernames(email_list)
    eliminated_duplicates = []

    for username in usernames:
        if username not in eliminated_duplicates:
            eliminated_duplicates.append(username)

    return eliminated_duplicates


def duplicates(email_list):
    usernames = extract_usernames(email_list)
    dup_username = {}

    for username in usernames:
        count = usernames.count(username)
        if username not in dup_username:
            dup_username[username] = count

    return dup_username


def sort_usernames(email_list):
    usernames = extract_usernames(email_list)
    return sorted(usernames)


def count_appearance(email_list):
    usernames = extract_usernames(email_list)
    print("Usernames in the list:", usernames)
    target = input("What do you want to count: ")
    return usernames.count(target)


def main():
    emails = [
        "aj@gmail.com",
        "  rahul@yahoo.com ",
        "tina@outlook.com",
        "aj@gmail.com"
    ]

    while True:
        print("\nCurrent Email List:", emails)
        print("""
Menu:
1. Remove extra spaces
2. Extract usernames
3. Identify duplicates
4. Eliminate duplicates
5. Sort usernames alphabetically
6. Count appearance of a username
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(remove_extra_spaces(emails))

        elif choice == 2:
            print(extract_usernames(emails))

        elif choice == 3:
            print(duplicates(emails))

        elif choice == 4:
            print("New list without duplicates:",
                  duplicate_elimination(emails))

        elif choice == 5:
            print(sort_usernames(emails))

        elif choice == 6:
            print(count_appearance(emails))

        else:
            print("Invalid Input")

        cont = input("Do you want to continue (y/n): ")
        if cont.lower() != "y":
            break


if __name__ == "__main__":
    main()