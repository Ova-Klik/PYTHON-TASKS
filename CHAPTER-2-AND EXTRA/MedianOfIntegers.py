#monday is 1/7 the
#sunday is 6

number_one=int(input("Enter a number :\n" ))

number_two=int(input("Enter another number :\n" ))

number_three=int(input("Enter a yet another number :\n" ))

number_four=int(input("Enter a thge last number :\n" ))


smallest = number_one

if smallest>number_two or number_three or number_four:

    smallest=number_two

elif smallest>number_three:

    smallest=number_three

elif smallest>number_four:

    smallest=number_four

median=number_two + number_three/2

print(f"The ascending order is : {number_one},{number_two},{number_three},{number_four}")
print(f"The median of the four number is {median}")



