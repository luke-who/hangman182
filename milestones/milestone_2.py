import random

# Define the list of possible words.
word_list = ["apple", "jackfruit", "blueberry", "popmogranate", "watermelon"]
for word in word_list:
    print(word)

# Chooose a random word from the list.
word = random.choice(word_list)
print(f'\nRandom fruit: {word}')

# Ask the user for an input.
guess = input("Please enter a single letter:")

# Check that the input is a single character.
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

