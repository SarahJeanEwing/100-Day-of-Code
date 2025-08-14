import random
import hangman_words
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
already_guessed_list = []

hangman_logo = hangman_art.logo
word_with_dashes = ""
hangman_stage = hangman_art.stages[lives]
message = ""

display = []
for i in range(word_length):
    display.append("_")
    word_with_dashes = f"{' '.join(display)}\n"

def format_output(hangman_logo, word_with_dashes, hangman_stage, message):
    print(f"{hangman_logo}\n{word_with_dashes}\n{hangman_stage}\n{message}")

format_output(hangman_logo, word_with_dashes, hangman_stage, message)

while not end_of_game:
    guess = input(f"Guess a letter: ").lower()
    os.system('clear')

    #Check guessed letter
    if guess in already_guessed_list:
        message = f"You already guessed {guess}"
        format_output(hangman_logo, word_with_dashes, hangman_stage, message)
    else:
        already_guessed_list.append(guess)
        for i in range(0, len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = chosen_word[i]
        word_with_dashes = f"{' '.join(display)}\n"
        
        if guess not in chosen_word:
            lives -= 1
            message = f"You guessed {guess}, that's not in the word. You lose a life."
            if lives == 0:
                end_of_game = True
                message = f"You lose. The correct answer was {chosen_word}"
        else:
            message = ""
    
        hangman_stage = hangman_art.stages[lives]
       
        if "_" not in display:
            end_of_game = True
            message ="You win."
            #format_output(hangman_logo, word_with_dashes, hangman_stage, message)
        #else:
            #format_output(hangman_logo, word_with_dashes, hangman_stage, message)
        format_output(hangman_logo, word_with_dashes, hangman_stage, message)
