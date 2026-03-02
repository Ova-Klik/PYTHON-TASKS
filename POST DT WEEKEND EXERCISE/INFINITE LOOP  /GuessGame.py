import random


counter = 0
numbers = random.randint(1, 20) 
run = "start" 

while run:
    guess_number = int(input("Kindly guess a number between 1 AND 20: "))
    counter += 1

    if guess_number == numbers:
        print(f"\nYou won in {counter} attempts")
        break

    elif guess_number > numbers:
        print("\nToo high")

    elif guess_number < numbers:
        print("\nToo low")



