import art
import random
import os

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5

def adjust_number_of_guesses_by_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_GUESSES
    elif level == "hard":
        return HARD_LEVEL_GUESSES
    else:
        return 0

def is_game_over(guesses_left):
    if guesses_left == 0:
        print("You've run out of guesses, you lose.")
        return True
    else:
        return False
        
play_again = "y"
while play_again == "y":
    
    guesses_left = 0
    random_number = random.randint(1, 100)
    os.system('clear')
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while guesses_left == 0:
        guesses_left = adjust_number_of_guesses_by_difficulty()
        if guesses_left == 0:
            print("Invalid option, please try again.")
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    
    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess < random_number:
            print("Too low.")
            guesses_left -= 1
            game_over = is_game_over(guesses_left)
        elif guess > random_number:
            print("Too high.")
            guesses_left -= 1
            game_over = is_game_over(guesses_left)
        elif guess == random_number:
            print(f"You got it!  The answer was {random_number}.")
            game_over = True

    play_again = input("\nWould you like to play again? Type 'y' for yes or 'n' for no: ")

os.system('clear')
print(art.logo)
print("Thanks for playing!")
