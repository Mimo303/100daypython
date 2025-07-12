#Name the lyrics game 
print("--Fill in The Blank Lyrics--")
print("Type in the blank lyrics and see if you are right ")

while True:
    attempt = 0
    max_attempts = 3
    
    while attempt < max_attempts:
        print("I'll be __________ if you can't be here, ohhh ,ohhhh  ")
        fill = input("Guess the blank Lyrics: ")
        
        if fill.lower() == "fucked up":
            attempt += 1
            print(f"You finally got it, after {attempt} attempts!")
            break
        else:
            attempt += 1
            if attempt < max_attempts:
                print("Try again")
            else:
                print(f"Sorry, you've used all {max_attempts} attempts. The answer was 'fucked up'")
    
    # Ask if user wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break