player_one=input('Kindly enter "Rock"or Paper" or "Scissors" to Play: ').lower()
player_two=input('Kindly enter "Rock"or Paper" or "Scissors" to Play: ').lower()

moves = ("rock", "paper", "scissors")

if player_one.isdigit() or player_two.isdigit() or\
         player_one not in moves and\
         player_two not in moves:
    print("Invalid inputs, Try again")

else:
    if player_one == player_two:
        print("It's a TIE")

    elif (player_one == "rock" and player_two == "scissors") or \
         (player_one == "paper" and player_two == "rock") or \
         (player_one == "scissors" and player_two == "paper"):
        print("Player1 wins")

    else:
        print("Player2 wins")
