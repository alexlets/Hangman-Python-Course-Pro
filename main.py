import random
#import hangman_words
from hangman_words import word_list
from hangman_art import stages, logo


lives = 6

print(logo)

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""

for i in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)
display = ["_"] * len(chosen_word)
guesses = []

while True:
    print(" ".join(display))
    print(f"You have {lives} lives remaining")
    print(stages[lives])
    found = False
    if lives == 0:
        print("You lose")
        break
    while True:
        guess = input("Enter a letter")
        if len(guess) == 1 and guess.isalpha():
            guess = guess.lower()
            break
        print("Invalid Input! Please enter exactly one letter.")
    if guess not in guesses:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                found = True
                guesses.append(guess)
        if not found :
            lives-=1
            guesses.append(guess)
            print(f"You guessed {guess} that's not in the word. You lose a life.")
    else :
        print(f"You already made this guess({guess})!")
    if "_" not in display:
        print("You found the word!")
        break



