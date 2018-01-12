import random

D1 = (random.randint(1, 6))
D2 = (random.randint(1, 6))
number = 0
money = 15
insert = -1
win = 7

while insert < number:
    print("so do you want to play a game of lucky 7")
    print("you start off with $15 just spend a $1 to gamble your money to play this game.")
    insert = int(input())
    print(money - 1)
print(D1)
print(D2)

print(D1 + D2)

if (D1 + D2) == win:
    print("you win here 4 dollars, want to play again")
    print(" your money is" + str(money - 1 + 4))
if (D1 + D2) != win:
    print("you lost want to play again, just insert $1")
    insert = int(input())

if money == 0:
    number = str(D1, D2)
    print("the amount of round you played" + number)







