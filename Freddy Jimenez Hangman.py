import random


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
letter = ("abcdefghijklmnopqrstuvwxyz")
letter_used = []
listTwo = []
for letter in strOne:
    if letter != ' ':
        listTwo.append("*")
    else:
        listTwo.append(" ")

print("let's play a game of hangman")
print("you're going to have 10 guess to guess the word.")
while len(strOne) != 0:
    print(listTwo)
    guess = input("letter >")
    guess = guess.lower()
    guesses -= 1
    print(guess)

    for guess in range(len(word)):
        if guess != strOne in word:
            print("guess again")
            print(guesses)
        else:
            print("you found a letter")
        if guess == listOne:
            letter_used.append(guess)
        if guess == strOne in letter:
            print(listTwo.remove(guess))
        if guesses == 0:
            print("you lost")
        else:
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
