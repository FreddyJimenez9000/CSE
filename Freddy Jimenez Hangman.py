import random
import string
# this is a guide of how to make hangman
#
# 1. make a word bank - 10 items
# 2. Select a random guess
# 3. take in a letter and add it to a list of letters_guess
# 4. reveal letters based on input
# 5. create win/lose condition

word = ['death', 'math', 'homework', 'money', 'games', 'stuff', 'Family Guy', 'school is fun', 'Edison Tigers', 'Gaston']

choice = random.choice(word)
guess = 10
strOne = choice
listOne = list(strOne)
if guess != 0:
    print("let's play a game of hangman")
    print("there are going to be 10 word that you're going to guess. You will only have 10 tries to guess the word.")
    print(listOne)
    print(choice)
    stuff = string.ascii_letters
    stuff = input(int())







