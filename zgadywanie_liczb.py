"""
Program that asks user to guess the number randomly chosen by computer.
Computer checks the input and states "Too low" or "Too high" to guide the user.
"""
from random import randint

def draw():
    """
    Function asks the user to provide a number and checks if it is an integer value.
    Repeats the request if it is not.
    :rtype: int
    :return: number provided by the user as int
    """
    while True:
        try:
            number_1 = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return number_1


def check():
    """
    Function checks if number provided by user matches the one drawn by computer
    """
    number_2 = randint(1,10)
    get_number = draw()
    while get_number != number_2:
        if get_number < number_2:
            print("Too small!")
        else:
            print("Too big!")
        get_number = draw()
    print("You win!")


check()
