while True:
    x=input("Enter 1st number: ")
    y=input("Enter 2nd number: ")
    try:
        print("Addition:", int(x) + int(y))
    except ValueError:
        print("Both should be numbers in digits!")
        continue
    else:
        conti=input("Do you want to continue (y/n) : ")
    if conti.strip().lower()!='y':
        break  
    else:
        continue