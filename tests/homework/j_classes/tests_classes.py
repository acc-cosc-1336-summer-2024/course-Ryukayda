import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_Die_get_rolled_value(self):
        dice_no = 0
        
        # Create three objects
        my_first_dice = Die()
        my_second_dice = Die()
        my_third_dice = Die()

        # Store 3 dice objects into a list
        my_dice = [my_first_dice, my_second_dice, my_third_dice]

        # For each dice present in my_dice we create a empty list:
        for dice in my_dice:
            my_dice_to_test = []
            dice_no += 1

            # Inner loop to roll the dice three times and append the roll value to the test list
            for i in range(3):
                dice.roll()
                my_dice_to_test.append(dice.get_rolled_value())

            # For each roll value in the test list, check that each value is within the range of 1 to 6
            for roll_value in my_dice_to_test:
                self.assertTrue(1 <= roll_value <= 6, f"Roll value {roll_value} is out of range!")

if __name__ == '__main__':
    unittest.main()
