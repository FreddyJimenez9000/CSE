import random

print(random.randint(0, 50))

guess = (7)


num = (6)

print(guess = num)

guess == num

input(">_")

def guess(num):
  if guess == num:
    print("correct")
  elif guess < num:
    print("higher")
  elif guess > num :
    print("lower")

input(">_")


        # generate a number, ask the user for an input(number), does the guess match the number?  #  add "higher" or "lower" , add 5 guesses