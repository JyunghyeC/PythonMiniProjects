print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Your options will be shown in upper cases.")
print("Please make sure to type in your choices in lower case.")

first_answer = input("You are in a maze. Which way do you want to go, LEFT or RIGHT? ").lower()

if first_answer == "left":
    print("You got out of the maze safely.")
    second_answer = input("You encountered a lake. Do you want to wait for a BOAT or SWIM? ").lower()
    if second_answer == "boat":
        print("You have arrived to a new island unharmed.")
        third_answer = input("You've come across three doors. Which door do you want to open: RED, YELLOW or BLUE? ").lower()
        if third_answer == "yellow":
            print("Congratulations! You found the treasure!")
        elif third_answer == "red":
            print("The red room was on fire!\nGame Over.")
        elif third_answer == "blue":
            print("Grrrr! The blue room was full of hungry beasts.\nGame Over.")
        else:
            print("Not an available option.\nGame Over.")
    else:
        print("You are attacked by trouts.\nGame Over.")
else:
    print("Oh no! There was a giant sink hole! You have fallen in to the hole.")
    print("Game Over.")
