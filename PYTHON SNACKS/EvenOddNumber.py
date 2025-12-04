number = input("Please Enter a number: ")

if not number.isdigit():  
    print("Invalid Input, Please try again")
else:
    number=int(number)
    if number%2 == 0:
        print("The Number", number, "is EVEN")
    else:
        print("The Number", number, "is ODD")
