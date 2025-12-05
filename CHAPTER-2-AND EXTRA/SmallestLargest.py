number_one = float(input("Please enter number: "))
number_two = float(input("Please enter number: "))
number_three = float(input("Please enter number: "))


print(f"\nThe smallest of the three numbers is: {min(number_one, number_two, number_three)}")


print(f"The largest of the three numbers is: {max(number_one, number_two, number_three)}\n")


total = number_one + number_two + number_three
print(f"The Sum of the three numbers is: {total}\n")


average = total / 3
print(f"The Average of the three numbers is: {average}\n")


product = number_one * number_two * number_three
print(f"The Product of the three numbers is: {product}\n")

