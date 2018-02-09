import random


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

count = 0
print("let's play a game of hangman")
print("you're going to have 10 guess to guess the word.")
while count < len(listOne):
    print(listTwo)
    stuff = input("letter >")
    stuff = stuff.lower()
    guess = guess - 1
    print(guess)

    for i in range(len(listOne)):
        if listOne[i] == stuff in stuff in listTwo:
            listTwo[i] = stuff
            stuff.append = listTwo[i]
            count = count + 1
            print(guess)
            print(count)
            listTwo.remove(stuff)
            print("you guess the word")

        if guess == 0:
            print("your man is dead")



    # if stuff in listTwo:
    #     if stuff != listTwo in word:
    #         print(guess - 1)














        # print(string.ascii_letters)
        # print(string.ascii_lowercase)
        # print(listOne)
        # l1 = ['d', 'e', 'a', 't', 'h']
        # print("". join(l1))