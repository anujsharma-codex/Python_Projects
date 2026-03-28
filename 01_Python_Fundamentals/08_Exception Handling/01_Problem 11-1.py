x=input("Enter 1st number: ")
y=input("Enter 2nd number; ")
try:
    print("Addition:", x + y)
except ValueError:
    print("Both should be numbers in digits!")
else:
    print("Addition of these numbers is: ",x+y)