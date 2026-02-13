def remove_all_negative_numbers(data):
    positive_numbers = []
    for i in data:
        if i < 0:
            continue
        else:
            positive_numbers.append(i)
    return positive_numbers


def count_element(data, value):
    return data.count(int(value))


def insert_number(data, position, target, value):
    if target not in data:
        return data

    i = data.index(target)

    if position == "before":
        data.insert(i, value)
    elif position == "after":
        data.insert(i + 1, value)

    return data


def reverse_list(data):
    return data[::-1]


def create_sorted_copy(data):
    copy = data.copy()
    print("Original list:", data)
    return sorted(copy)


def check_existence(data, x):
    if x in data:
        return "It exists"
    else:
        return "It does not exist"


def main():
    print("Data = [10, 20, -5, 30, -2, 40, 20, 50]")

    print("""
Menu:
1. Remove all negative numbers
2. Count how many times a number appears
3. Insert a number before/after a number
4. Reverse the list
5. Create a sorted copy without modifying original
6. Check if a number exists in the list
""")

    while True:
        choice = input("Do you want to continue (y/n): ")
        if choice.lower() != 'y':
            print("End of program")
            break

        data = [10, 20, -5, 30, -2, 40, 20, 50]

        x = int(input("Enter your choice: "))

        if x == 1:
            print(remove_all_negative_numbers(data))

        elif x == 2:
            value = int(input("Enter the element: "))
            print(count_element(data, value))

        elif x == 3:
            position = input("Enter (before/after): ")
            target = int(input("Enter the target number: "))
            value = int(input("Enter the value you want to insert: "))
            print(insert_number(data, position, target, value))

        elif x == 4:
            print(reverse_list(data))

        elif x == 5:
            print(create_sorted_copy(data))

        elif x == 6:
            num = int(input("Enter the number you want to check: "))
            print(check_existence(data, num))

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()