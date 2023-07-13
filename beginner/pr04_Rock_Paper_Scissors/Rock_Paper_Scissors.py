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

images = [rock, paper, scissors]

print("Welcome to the rock paper scissors game!")

player_choice = int(input("Type in  a number of your choice. 0 is rock, 1 is paper and 2 is scissors.\n"))

if player_choice >= 3 or player_choice < 0:
    print("Invalid number. Try Again.")
else:
    print("You :\n" + images[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer :\n" + images[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice < computer_choice:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
