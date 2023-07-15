import random
import hangman_image
import hangman_word_list


print("Welcome to the Hangman Game!")

# Choosing a random word
answer = random.choice(hangman_word_list.words)
# Total number of tries the user is provided
lives = 6

# Blanks for showing the length of the word
display = []
for i in answer:
    display.append("_")

end_of_game = False

# Game logic
while not end_of_game:
    guess = input("Guess a letter :\n").lower()

    # If guessed right
    if guess in display:
        print("You have already guessed this letter!")
    # Replace blank space with the right letter
    for i in range(len(answer)):
        letter = answer[i]
        if letter == guess:
            display[i] = letter

    # If guessed wrong
    if guess not in answer:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        # The game ends after 6 tries
        if lives == 0:
            end_of_game = True
            print(f"You lose. The answer is '{answer}'")

    print(f"{''.join(display)}")

    # When the user guesses all the letters within 6 tries
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_image.stages[lives])
