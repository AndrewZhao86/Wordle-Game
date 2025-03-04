import random
import sys
from valid_words import valid_words

SECRET_WORD = random.choice(valid_words)
MAX_ATTEMPTS = 6

class Color:
	PREFIX = '\033'
	RESET = "\033[0m"
	GREY = "\033[90m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	PRIORITY_COLORS = [RED, GREEN]

class WordGuess:
	attempt_number = 1
	previous_guesses = []
	letter_map = {char: char for char in "abcdefghijklmnopqrstuvwxyz"}

	def __init__(self, user_input: str):
		self.user_input = user_input.lower()
		self.char_list = list(self.user_input)
		self.formatted_guess = ""

	def increment_attempt(self):
		WordGuess.attempt_number += 1

	def is_valid(self):
		if len(WordGuess.previous_guesses) > 0:
			print(f"Previous Guess(es): {WordGuess.previous_guesses}")
		if len(self.user_input) != 5:
			print("Each guess must be 5 letters long. Please input a 5-letter word.")
			return False
		elif self.user_input not in valid_words:
			print("Your word does not exist. Please enter a valid word.")
			return False
		elif self.user_input in WordGuess.previous_guesses:
			print(f"You have already guessed '{self.user_input}'. Please try a new word.")
			return False
		return True

	def apply_correct_positions(self):
		for index, _ in enumerate(self.char_list):
			correct_char = SECRET_WORD[index]
			guessed_char = self.char_list[index]
			if correct_char == guessed_char:
				colored_char = f"{Color.GREEN}{correct_char}{Color.RESET}"
				self.char_list[index] = colored_char
				self.update_letter_map(correct_char, colored_char)

	def apply_misplaced_positions(self):
		for index, _ in enumerate(self.char_list):
			guessed_char = self.char_list[index]
			if guessed_char in SECRET_WORD:
				colored_char = f"{Color.YELLOW}{guessed_char}{Color.RESET}"
				self.char_list[index] = colored_char
				self.update_letter_map(guessed_char, colored_char)
			else:
				colored_char = f"{Color.RED}{guessed_char}{Color.RESET}"
				self.update_letter_map(guessed_char, colored_char)

	def update_letter_map(self, letter, colored_letter):
		if letter not in WordGuess.letter_map:
			return

		current_value = WordGuess.letter_map.get(letter, "")
		if not any(color in current_value for color in Color.PRIORITY_COLORS):
			WordGuess.letter_map[letter] = colored_letter

	def process_guess(self):
		self.apply_correct_positions()
		self.apply_misplaced_positions()
		self.formatted_guess = "".join(self.char_list)
		WordGuess.previous_guesses.append(self.user_input)
		print(self.formatted_guess)

	def check_win(self):
		if self.user_input == SECRET_WORD:
			print(f"Congratulations! You solved Wordle in {WordGuess.attempt_number} guesses!")
			print("Your guesses were: ")
			for guess in WordGuess.previous_guesses:
				print(guess)
			sys.exit(0)

	def check_loss(self):
		if WordGuess.attempt_number > MAX_ATTEMPTS:
			print(f"You lost the game. The correct word was '{SECRET_WORD}'.")
			print("Your guesses were: ")
			for guess in WordGuess.previous_guesses:
				print(guess)
			sys.exit(0)
