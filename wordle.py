import random
import sys
from valid_words import valid_words
from colorama import Fore, Style

SECRET_WORD = random.choice(valid_words)
MAX_ATTEMPTS = 6

class Color:
	RESET = Style.RESET_ALL
	GREY = Fore.LIGHTBLACK_EX
	GREEN = Fore.GREEN
	YELLOW = Fore.YELLOW
	PRIORITY_COLORS = [GREEN, YELLOW]

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

	def count_secret_word_letters(self):
		return {char: SECRET_WORD.count(char) for char in set(SECRET_WORD)}

	def apply_correct_positions(self):
		secret_letter_count = self.count_secret_word_letters()
		for index, guessed_char in enumerate(self.char_list):
			correct_char = SECRET_WORD[index]
			if correct_char == guessed_char:
				colored_char = f"{Color.GREEN}{correct_char}{Color.RESET}"
				self.char_list[index] = colored_char
				self.update_letter_map(correct_char, colored_char)
				secret_letter_count[correct_char] -= 1
		return secret_letter_count

	def apply_misplaced_positions(self, secret_letter_count):
		for index, guessed_char in enumerate(self.char_list):
			if isinstance(guessed_char, str):  # Skip already colored characters
				if guessed_char in SECRET_WORD and secret_letter_count[guessed_char] > 0:
					colored_char = f"{Color.YELLOW}{guessed_char}{Color.RESET}"
					self.char_list[index] = colored_char
					self.update_letter_map(guessed_char, colored_char)
					secret_letter_count[guessed_char] -= 1
				else:
					colored_char = f"{Color.GREY}{guessed_char}{Color.RESET}"
					self.update_letter_map(guessed_char, colored_char)

	def update_letter_map(self, letter, colored_letter):
		if letter not in WordGuess.letter_map:
			return

		current_value = WordGuess.letter_map.get(letter, "")
		if not any(color in current_value for color in Color.PRIORITY_COLORS):
			WordGuess.letter_map[letter] = colored_letter

	def process_guess(self):
		secret_letter_count = self.apply_correct_positions()
		self.apply_misplaced_positions(secret_letter_count)
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