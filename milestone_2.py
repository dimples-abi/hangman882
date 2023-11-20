import random

fruit_word_list = ['apple', 'pear', 'cherry', 'raspberry', 'clementine']

random_word = random.choice(fruit_word_list)

user_guess = input('Enter a single letter: ')
if len(user_guess) == 1 and user_guess.isalpha():
    if user_guess in random_word:
        print("Good guess!")
    else:
        print("Oops! That letter is not in the word.")
else:
    print("Oops! That is not a valid input.")