number_of_integers = int(input("Enter number of integers: "))

sum_odd = 0
sum_even = 0
counter = 1

print("Enter your numbers:")

while counter <= number_of_integers:
    num = int(input(f"Number {counter}: ")) 

    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

    counter += 1  

print("The sum of even numbers and sum of odd numbers are", sum_even, "and", sum_odd, "respectively")

