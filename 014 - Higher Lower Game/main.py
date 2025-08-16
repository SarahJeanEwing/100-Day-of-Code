import random
import art
import game_data
import os

def output(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def determine_correct_answer(a, b):
    if a['follower_count'] > b['follower_count']:
        return "a"
    elif b['follower_count'] > a['follower_count']:
        return "b"

score = 0
game_over = False
a = random.choice(game_data.data)
b = random.choice(game_data.data)
while b == a:
    b = random.choice(game_data.data)

while not game_over:
    os.system('clear')
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    output(a, b)
    
    choice = ""
    while choice.lower() not in ['a', 'b']:
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice.lower() not in ['a', 'b']:
            print("Invalid choice, please try again.")

    correct_answer = determine_correct_answer(a, b)
    if choice == correct_answer:
        score += 1
        a = b
        b = random.choice(game_data.data)
        while b == a:
            b = random.choice(game_data.data)
    else:
        game_over = True

os.system('clear')
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
        