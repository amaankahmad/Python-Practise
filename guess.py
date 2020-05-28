from random import randint
import time

valid = 1

print("\nWelcome to the Guessing Game where I will pick a number from 1 to 9, you have to try guess it!\n")

while valid == 1:
    # Check if player wants to play:
    z = input("Ready to play?"+" ")
    # Convert all inputs to lower case in case user input differs from specified
    if z.lower() == "yes" or z.lower() == "yep" or z.lower() == "yeah" or z.lower() == "yh" or z.lower() == "yeh":
        valid = 1
    else:
        break

    # Loading Time 
    time.sleep(0.5)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

    # Computer pick a random number between 1 to 9
    computer_random = randint(1,9)
    # User first guess
    user_guess = int(input(("Guess my number!"+" ")))

    # Track number of guesses
    number_of_guesses = 1

    # Check guess
    if user_guess>0 and user_guess < 10:
        while user_guess != computer_random:
            number_of_guesses +=1
            if user_guess < computer_random:
                user_guess = int(input("Too low!\nGuess again:"+ " "))
            elif user_guess > computer_random:
                user_guess = int(input("Too high!\nGuess again:"+ " "))
        print("\nCongrats you have guessed correctly in", number_of_guesses, "guesses!\n\nPlay again:")
    # Check if input valid
    else:
        print("\nInvalid input - try again!\n")