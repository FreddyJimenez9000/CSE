import random

D1 = (random.randint(1, 6))
D2 = (random.randint(1, 6))

money = 15
insert = -1
win = 7

while insert < D1:
    print("so do you want to play a game of lucky 7")
    print("just spend a dollar to gamble your money on this rigged game.")
    insert = int(input())

print(D1)
print(D2)

print(D1 + D2)

if (D1 + D2) == 7:
    print("you win here 4 dollars, want to play again")
if (D1 + D2) != win:
    print("you lost want to play again")


if money == 0:
    money = str(0)
    print("the amount of round you played" + 100)



