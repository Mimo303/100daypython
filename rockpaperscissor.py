# Rock , paper , scissor game 
from getpass import getpass as input  # its hide your input 
print("""Welcome to Rock , Paper , Scissor game
Select R---- Rock 
Select P------Paper
Select S------Scissor""")
player1_name = input("Enter Player 1 name: ")
print(f"Player 1 name is: {player1_name}")
player2_name = input("Enter Player 2 name: ")
print(f"Player 2 name is: {player2_name}")

while True:
    player1 = input(f"{player1_name} : Your turn(R/P/S) :  ")
    player2 = input(f"{player2_name} : Your Turn(R/P/S) :  ")
    emoji = {"r": "🪨", "p": "📄", "s": "✂️"}

    player1_choice = player1.lower()
    player2_choice = player2.lower()

    if player1_choice == player2_choice:
        print(f"TIE! Both selected {emoji.get(player1_choice, '')}")
    elif player1_choice == "r" and player2_choice == "s":
        print(f"{player1_name} selects Rock {emoji['r']}, {player2_name} selects Scissor {emoji['s']}")
        print(f"The winner is : {player1_name}")
    elif player1_choice == "s" and player2_choice == "p":
        print(f"{player1_name} selects Scissor {emoji['s']}, {player2_name} selects Paper {emoji['p']}")
        print(f"The winner is : {player1_name}")
    elif player1_choice == "p" and player2_choice == "r":
        print(f"{player1_name} selects Paper {emoji['p']}, {player2_name} selects Rock {emoji['r']}")
        print(f"The winner is : {player1_name}")
    elif player2_choice == "r" and player1_choice == "s":
        print(f"{player1_name} selects Scissor {emoji['s']}, {player2_name} selects Rock {emoji['r']}")
        print(f"The winner is : {player2_name}")
    elif player2_choice == "s" and player1_choice == "p":
        print(f"{player1_name} selects Paper {emoji['p']}, {player2_name} selects Scissor {emoji['s']}")
        print(f"The winner is : {player2_name}")
    elif player2_choice == "p" and player1_choice == "r":
        print(f"{player1_name} selects Rock {emoji['r']}, {player2_name} selects Paper {emoji['p']}")
        print(f"The winner is : {player2_name}")
    else:
        print("Invalid input")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
