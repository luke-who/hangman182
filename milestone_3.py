import random

# Define the list of possible words.
word_list = ["apple", "jackfruit", "blueberry", "popmogranate", "watermelon"]
# for word in word_list:
#     print(word)

# Chooose a random word from the list.
word = random.choice(word_list)


# Check whether the guess is in the word
def check_guess(guess):
    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again!")

# Iteratively check if the input is a valid guess
def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()