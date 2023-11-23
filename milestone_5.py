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
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            return False
        return True
    
    def ask_for_input(self):
        if not self.list_of_guesses:  # Check if the list_of_guesses is empty
            print("This is your word:", ' '.join(self.word_guessed))
        while True:
            guess = input("Guess a single letter in the word: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    print("Current state of word:", ' '.join(self.word_guessed))
                    self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0: 
            game.ask_for_input()
        else: 
            print('Congratulations. You won the game!')
            break

word_list = ['apple', 'pear', 'cherry', 'raspberry', 'clementine']
play_game(word_list)



