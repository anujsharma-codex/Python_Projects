while True:
    guest_name=input("Enter your name(press Enter to quit): ")
    if guest_name.lower().strip()=="":
        break
    print(f"Welcome {guest_name.title()}")
    with open("guest_book.txt",'a',encoding='utf-8') as file:
        file.write(guest_name.title()+"\n")
with open('guest_book.txt',encoding='utf-8') as file:
    for x in file:
        print(x.strip())