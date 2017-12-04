import random
print(random.randint(0, 50))

c = '23'


print("Try to Guess a number from one through fifty")


def number_guess(number):
    if number == 34:
        return"correct"
    elif number < 34:
        return"incorrect"
    elif number > 34:
        return"incorrect"


