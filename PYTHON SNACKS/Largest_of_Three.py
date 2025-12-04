first_number=float(input("Enter First NUmber: "))
second_number=float(input("Enter Second NUmber: "))
third_number=float(input("Enter Second NUmber: "))

largest=first_number

if first_number > largest:
    largest=second_number
   
if second_number > largest:
    largest=third_number
  
else:
    print(largest) 
