#
import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num = get_valid_input("Enter a number between 1 and 9: ", 1, 9)
            result = get_factorial(num)
            print(f"The factorial of {num} is {result}.")
        
        elif choice == '2':
            num = get_valid_input("Enter a number between 1 and 99: ", 1, 99)
            result = sum_odd_numbers(num)
            print(f"The sum of odd numbers up to {num} is {result}.")
        
        elif choice == '3':
            exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
            if exit_choice in ['yes', 'y']:
                print("Exiting the program. Goodbye!")
                break
            else:
                continue
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
