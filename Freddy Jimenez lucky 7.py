import random

number = 0
money = 15
insert = -1
win = 7
while insert < number:
    D1 = (random.randint(1, 6))
    D2 = (random.randint(1, 6))
    print("so do you want to play a game of lucky 7")
    print("you start off with $15 just spend a $1 to gamble your money to play this game.")
    insert = int(input())
    number = number + 1
    print(money - 1)

    print(D1)
    print(D2)

    print(D1 + D2)

    if (D1 + D2) == win:
        print("you win here 4 dollars, want to play again")
        print(" your money is" + str(money + 4))
    elif (D1 + D2) != win:
        print("you lost want to play again, just insert $1")
    elif money == 0:
        number = str(number)
        print("the amount of round you played" + number)
        money = str(money)
        print("also the money you earn" + money)






