# print("Hello world")
#
# Mr. Wiebe
#
#
# a = 3
# b = 6
#
# print(3 + 6)
# print(6 - 3)
# print(6 / 3)
# print(3 * 6)
#
# print("Try to solve this type of problem and what it mean")
#
# print(15 % 12)
#
# this "%" sign is a module. It find the remander
#
#
# car_named = "red"
# car_type = "BMW"
# car_cylinder = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's red." % car_named)
# print("I have a car called %s. It's red." % car_named, car_type)
#
# print("What is your named?")
# name = input(">_")
# print("Hello %s." % name)
#
#
# age = input("How old are you?")
#
# print("%s?! That's really old ." % age)
#
# print("what in the world are we doing in here")

# function


def print_hw():
    print("Hello World.")    # Four spaces
    print("Enjoy the day.")


print_hw()


def say_hi(named):        # Named is a "parameter"
    print("Hello %s" % named)
    print("Coding is great!")


say_hi("Bob")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("Next year, % s wil be %d years old" % (name, age))


print_age("Bob", 15)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 *x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# If statements


def grad_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # elif = else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print('grade_calc(59)')


def happy_bday(name):
    print("happy birthday to you" + ",")
    print("happy birthday to you" + ",")
    print("happy birthday dear" + name + ",")
    print("happy birthday to you" + ",")


happy_bday("Bob")


# Loops

for num in range(10):
    print(num + 1)

    # While loops (beware!!!!!!!)

    # This is the condition,
    # it must be true to execute

a = 1

a +=1    # This iterates so that we can break the loop

# Random Numbers
import random   # this should be on line 1
print(random.randint(0, 10))

# Recasting
c = '1'
print(c == 1)  # we have a string and an int
print(int(c) == 1)
print(c == str(1))

# comparisons

print(1 == 1)  # use a double equal sign
print(1 != 2)  # 1 is not equal to 2
print(not False)


