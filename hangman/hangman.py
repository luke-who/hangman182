import random

class Hangman:
    """
    A class representing the Hangman game.

    Attributes:
        word (str): The word randomly selected for the game.
        word_guessed (list): The current state of the guessed word as a list of characters (or underscores).
        num_letters (int): The number of unique letters left to guess.
        num_lives (int): The number of incorrect guesses allowed.
        word_list (list): The list of words to choose from.
        list_of_guesses (list): The letters that have already been guessed.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new Hangman game.

        Parameters:
            word_list (list): A list of words from which a word is chosen randomly.
            num_lives (int): The allowed number of incorrect guesses. Default is 5.
        """
        # Choose a random word from the provided list
        self.word = random.choice(word_list)
        # Initialize the guessed word as underscores for each letter
        self.word_guessed = ['_'] * len(self.word)
        # Count unique letters in the word that must be guessed
        self.num_letters = len(set(self.word))
        # Set the number of lives for the game
        self.num_lives = num_lives
        # Store the original word list
        self.word_list = word_list
        # List to track letters that have already been guessed
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates game state accordingly.

        Parameters:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        # If the guessed letter is in the word, update word_guessed
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Iterate over each letter in the word to update the correct positions
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            # Reduce the count of unique letters to be guessed
            self.num_letters -= 1
            print('Current word:', ' '.join(self.word_guessed))
        else:
            # Incorrect guess: decrement number of lives
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print('Current word:', ' '.join(self.word_guessed))

    def ask_for_input(self):
        """
        Prompts the player for a letter guess, validates the input,
        and processes the guess if it is valid.
        """
        guess = input("Please guess a letter: ")
        # Validate that the input is a single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        # Check if the letter has already been guessed
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            # Process the valid guess
            self.check_guess(guess)
            # Record the guess to prevent duplicates
            self.list_of_guesses.append(guess)

def play_game(word_list):
    """
    Runs the game loop for Hangman until the player wins or loses.

    Parameters:
        word_list (list): A list of words to choose from for the game.
    """
    num_lives = 5
    # Create an instance of the Hangman game
    game = Hangman(word_list, num_lives)

    # Game loop continues until win or loss condition is met
    while True:
        # Check for loss condition
        if game.num_lives == 0:
            print("You lost! 💀")
            break
        # Continue the game if there are still letters to guess
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            # Win condition: all letters have been guessed
            print("Congratulations. You won the game! 🎉")
            break

if __name__ == "__main__":
    # Define a list of words for the game
    word_list = ["apple", "jackfruit", "blueberry", "pomegranate", "watermelon"]
    play_game(word_list)
