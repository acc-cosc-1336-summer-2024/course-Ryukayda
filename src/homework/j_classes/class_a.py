import random

class Die:
    def __init__(self):
        self.__my_roll = 0

    def roll(self):
        self.__my_roll = random.randint(1, 6)

    def get_rolled_value(self):
        return self.__my_roll

    def __str__(self):
        return f"The rolled value is {self.__my_roll}"
