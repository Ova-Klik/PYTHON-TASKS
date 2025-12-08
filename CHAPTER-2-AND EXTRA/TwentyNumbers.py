
sum_odd = 0
sum_even = 0
counter = 1

print("Enter your numbers:")

while counter <= 20:
    number = int(input(f"Number {counter}: ")) 

    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

    counter += 1  

print("The sum of even number is: ", sum_even, " and the sum of odd number is: ", sum_odd)

