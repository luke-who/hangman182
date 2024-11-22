# Hangman
[![python](https://img.shields.io/badge/python-3.10.15-blue?style=plastic&logo=python)](https://www.python.org/downloads/release/python-31015/)

## Table of Contents
- [Description](#description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License](#license)

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Installation Instructions
To run the Hangman game on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/luke-who/hangman182.git
2. Navigate to the project directory and source code folder [hangman182/hangman](/hangman)
   ```bash
   cd hangman182/hangman
   ```
3. Ensure you have Python installed on your machine. Here I have used `Python 3.10.15`
   ```bash
   ❯ python --version
   Python 3.10.15
   ```

## Usage Instructions
To start the Hangman game, run the following command in your terminal:
```bash
python hangman.py
```
Follow the on-screen instructions to guess the letters of the word. You will have a limited number of incorrect guesses before the game ends.
The default value for the number of lives `num_lives` is 5.

## File Structure
```
❯ tree
.
├── LICENSE                        # License information
├── README.md                      # Project documentation
├── hangman                        # Source code folder
│   ├── hangman.py                 # Main game
│   └── hangman_Template.py        # Game template (for reference only)
└── milestones                     # Steps to build the game
    ├── milestone_2.py
    ├── milestone_3.py
    ├── milestone_4.py
    └── milestone_5.py           
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
