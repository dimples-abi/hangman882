import random

class Hangman: 
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_' for _ in self.word]
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            self.num_letters -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            return False
        return True
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter in the word: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    self.list_of_guesses.append(guess)
                break

game = Hangman(['apple', 'pear', 'cherry', 'raspberry', 'clementine'])



