import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman game.

        Parameters:
        word_list (list): A list of words from which the game will randomly select one.
        num_lives (int): The number of incorrect guesses allowed before the game is over. Default is 5.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks the player's guess against the selected word.

        Parameters:
        guess (str): The letter guessed by the player.

        Returns:
        None: This method modifies the state of the game (updates lives and guessed letters) but does not return a value.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts the player to input a letter guess and validates the input.

        This method continues to ask for input until a valid guess is made. It checks if the guess is a single alphabetical character and if it has not been guessed before.
        If the guess is valid, it calls the check_guess method.

        Returns:
        None: This method does not return a value but modifies the state of the game based on user input.
        """
        guess = input("Please guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    """
    Plays the Hangman game.

    Returns:
    None: This method does not return a value but contains the logic to play the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Example usage
word_list = ["apple", "jackfruit", "blueberry", "pomegranate", "watermelon"]

play_game(word_list)
