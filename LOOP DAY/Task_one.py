even = []
odd = []
sum_of_even = 0
sum_of_odd = 0
sum_of_all_numbers = 0
sum_of_even_square = 0
sum_of_odd_square = 0
square_even = []
square_odd = []
count = 0

number = ""
square = ""


for num in range(1,11):
    number = int(input("Enter numbers: "))

    sum_of_all_numbers += number
    square_of_all_numbers = sum_of_all_numbers * sum_of_all_numbers
    count +=1
    mean = sum_of_all_numbers / count
    
    if number % 2 == 0:
        even.append(number)
        square_even.append(number)
        sum_of_even += number
    else:
        odd.append(number)
        sum_of_odd += number
        square_odd.append(number)
        
print()
        
        
for even_number in even:
    print(f"The even numbers are: {even_number}") 
print()   
    
for odd_number in odd:
    print(f"The odd numbers are: {odd_number}")  
print()

for s_even in square_even:
    square = s_even * s_even
    sum_of_even_square += square
    print(f"the square of even number are: {square}")
print(f"The sum of all even sqaure: {sum_of_even_square}")
print()
      
for s_odd in square_odd:
    square = s_odd * s_odd
    sum_of_odd_square += square
    print(f"the square of odd number are: {square}")
print(f"The sum of all even sqaure: {sum_of_odd_square}")
print()
      

print(f"The total sum of even numbers: {sum_of_even}")
print()

print(f"THe mean of all the numbers: {mean}")

print(f"The total sum of odd numbers: {sum_of_odd}")
print()

print(f"The total sum of numbers: {sum_of_all_numbers}")
print(f"The total square of numbers: {square_of_all_numbers}")






        

        
