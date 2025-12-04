guess = input("Guess my favourite number, Enter a number: ")

if not guess.isdigit():  
    print("Invalid Input, Please try again")
else:
   
    if guess == 7:
        print("That's my favourite Number, Thumbs up!")
    else:
        print("Nice Try, Guess again!")
