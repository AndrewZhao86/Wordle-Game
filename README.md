# Wordle Game in Terminal

A simple Wordle game that you can play directly in your terminal. You can play as many times as you want!

## Project Directory
```
wordle-game/
│-- main.py          # Entry point to run the Wordle game
│-- wordle.py        # Handles backend functionality of Wordle
│-- valid_words.py   # Contains a list of valid words for the game
│-- answer.txt       # Stores the chosen word for the current game
```
## Installation
Ensure you have **Python** installed on your system. Clone the repository and navigate into the project directory.
```bash
git clone <repository_url>
cd wordle-game
```

## How to Run
Run the game using:
```bash
python main.py
```

## File Descriptions
- **main.py**: Runs the game loop and interacts with the user.
- **wordle.py**: Implements the game logic, checks guesses, and provides feedback.
- **valid_words.py**: Contains a list of words that are valid guesses.
- **answer.txt**: Stores the target word that the player needs to guess.

## How to Play
- The game selects a word from `answer.txt`.
- You have six attempts to guess the correct word.
- Each guess must be a valid word from `valid_words.py`.
- Feedback is provided for each guess:
  - ✅ Correct letter in the correct position.
  - ⚠️ Correct letter in the wrong position.
  - ❌ Letter not in the word.
- Feel free to add more words into valid_words.py to expand our word bank.

Enjoy the game!