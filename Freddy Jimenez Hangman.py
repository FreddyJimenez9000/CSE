import random
import string

# this is a guide of how to make hangman
# 1. make a word bank - 10 items
# 2. Select a random guess
# 3. take in a letter and add it to a list of letters_guess
# 4. reveal letters based on input
# 5. create win/lose condition

word = ['death', 'math', 'homework', 'money', 'games', 'stuff', 'Family', 'school', 'Edison', 'Gaston']
guesses = 10
strOne = random.choice(word)
strOne = strOne.lower()
listOne = list(strOne)
letter_used = []
display = []
for letter in strOne:
    if letter != ' ':
        display.append("*")
    else:
        display.append(" ")

print("let's play a game of hangman")
print("you're going to have 10 guess to guess the word.")
while 0 < guesses:
    print(display)
    guess = input("letter >")
    guess = guess.lower()
    guesses -= 1
    print(guess)
    for guess in range(len(word)):
        if guess != strOne in string.ascii_letters:
            print("guess again")
        else:
            print("you found a letter")
            print(display.append(guess))
    if guess == word in listOne:
        print(display)
    if guesses == 0:
        print("you lost")
        break




"""


    # if stuff in listTwo:
    #     if stuff != listTwo in word:
    #         print(guess - 1)


    # listTwo[i] = guess
    # guess.append = listTwo[i]

"""










    # print(string.ascii_letters)
        # print(string.ascii_lowercase)
        # print(listOne)
