file='guest.txt'
name=input("Enter your name: ")
with open('guest.txt','w') as file:
    file.write(name)
with open('guest.txt') as file:
    print(file.read())