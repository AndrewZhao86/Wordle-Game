import wordle
import os

# Clear terminal screen
os.system("cls") if os.name == "nt" else os.system("clear")

welcome_message = """
Welcome to Wordle!!!
You have 6 guesses to find the correct word.
"""
print(welcome_message)

if __name__ == '__main__':
	with open("answer.txt", "w") as f:
		f.write(wordle.SECRET_WORD)

	while True:
		guess = wordle.WordGuess(
			user_input=input(f"Guess [{wordle.WordGuess.attempt_number}]: ")
		)

		if guess.is_valid():
			guess.process_guess()
			guess.check_win()
			guess.increment_attempt()
			guess.check_loss()
