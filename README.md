# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word at random from a preset list of words and the user tries to guess it. The aim of this project was for me to apply all of the Python coding skills I have learned so far into a practical project. Through completing this project, I have learned how useful defining functions and classes is to making code modular and user friendly. I have also improved my confidence in using the Python techniques used so far - especially in using loops and when to include certain commands inside or outside.

Installation instructions
The program was originally written in Python 3.12.0, so the user is advised to use a suitably up to date version of Python.

Usage instructions
When you run the program, the user will initially be shown how many letters are in the word using underscores. For example, if the word were "apple", the user would initially be shown " _ _ _ _ _ ". The user is then asked to guess individual letters. The program will check if the letters match the randomised word. If they match, the program will replace an underscore with the correct letters in the relevant position. Once all of the letters of the selected word have been guessed, a congratulatory message will be printed. If any incorrect letters are guessed or an invalid character is inputted, a relevant message will be printed. The user is only given 5 opportunities to guess an incorrect letter, otherwise they will be informed of losing the game.

File Structure
The file is structured in an easy to understand format, where under the Hangman class, methods for asking for the input and checking the guesses are initialised and defined. A function for playing the game is then defined.

License information
There is no license attached to this programme. 
