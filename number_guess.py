import random

def guess_num():
    print("Welcome to the Number Guessing Game.")
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")
    print("Game rules:\nI'm thinking of a number between 1 and 100. You have 10 attempts to guess the number \nLet's begin, Good luck!")
    while True:
        rand_num = random.randint(1, 100)
        attempts = 10
        for attempt in range(1, attempts + 1):
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            if guess < rand_num:
                print("Too low!.Guess a higher number")
            elif guess > rand_num:
                print("Too high!.Guess a lower number")
            else:
                print(f"Congratulations, {name}! You guessed the number correctly in {attempt} attempts.")
                break
        else:
            print(f"Oops Game over! The correct number was {rand_num}.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thank you for playing. Goodbye!")
            break
guess_num()



