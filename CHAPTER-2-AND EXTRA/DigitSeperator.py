

number=int(input("Please enter a single number 5 digits e.g (42339): "))

number_one= number//10000
number_two = (number//1000)%10
number_three = (number//100)%10
number_four = (number//10)%10
number_five =number%10


print( number_one, number_two, number_three, number_four, number_five, sep="   ")


