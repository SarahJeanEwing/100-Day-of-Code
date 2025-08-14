import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if user_choice not in ["0","1","2"]:
  print("\nYou entered an invalid choice. You lose")

else:
  computer_choice = random.randint(0,2)
  user_choice = int(user_choice)
  print(options[user_choice])
  
  print("Computer chose:")
  
  print(options[computer_choice])
  
  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == 0 and computer_choice == 1:
    print("You lose")
  elif user_choice == 1 and computer_choice == 2:
    print("You lose")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose")
  else:
    print("You win!")
  