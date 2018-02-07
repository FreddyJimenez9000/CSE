import random
import string

# this is a guide of how to make hangman
# 1. make a word bank - 10 items
# 2. Select a random guess
# 3. take in a letter and add it to a list of letters_guess
# 4. reveal letters based on input
# 5. create win/lose condition

word = ['death', 'math', 'homework', 'money', 'games', 'stuff', 'Family Guy', 'school is fun', 'Edison Tigers', 'Gaston']
guess = 10
strOne = random.choice(word)
strOne = strOne.lower()
listOne = list(strOne)
listTwo = []
for letter in strOne:
    if letter != ' ':
        listTwo.append("*")
    else:
        listTwo.append(" ")

print(strOne)
print(listTwo)
print("let's play a game of hangman")
print("you're going to have 10 guess to guess the word.")
while guess != 0:
    print(listOne)
    print(listTwo)
    stuff = input("letter >")
    if guess in listTwo:
        if stuff != letter in listTwo:
            print(listTwo.append(string.ascii_letters))
        if stuff == letter in listTwo:
            print(listTwo.append(string.ascii_letters))













        # print(string.ascii_letters)
        # print(string.ascii_lowercase)
        # print(listOne)
        # l1 = ['d', 'e', 'a', 't', 'h']
        # print("". join(l1))