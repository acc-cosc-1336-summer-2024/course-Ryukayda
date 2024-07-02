import strings

def keep_going():
    continue_choice = input("Would you like to continue? Y / N")
    continue_choice = continue_choice.upper()

    if continue_choice == "Y":
       user_options()
    else:
        print("Goodbye!")
        return

def handle_hamming_distance():
    hamming_choice = input("Please type in the sequence of the first string you would like to check: ")
    
    hamming_choice_2 = input("Please type in the sequence of the first string you would like to check: ")

    strings.check_if_valid(hamming_choice, hamming_choice_2)

    # Call function if valid and store it into a variable:

    hamming_return = strings.get_hamming_distance(hamming_choice, hamming_choice_2)
    print(f"Hamming distance is: {hamming_return}")


    keep_going()

def handle_dna_rc():
    dna_rc_choice = input("Please type in the desired sequence to check: ")

    dna_rc_return = strings.get_dna_complement(dna_rc_choice)

    print(f"The sequence for the Reverse Complement of {dna_rc_choice} is {dna_rc_return}")
    keep_going()


def main_menu():

    print("1 - Hamming Distance")
    print("2 - Dna Complement")
    print("3 - Exit")


    
def user_options():
        
        main_menu()
        my_choice = int(input("Please select which option you would like to access: "))
        
        if my_choice == 1:
            handle_hamming_distance()
        elif my_choice == 2:
            handle_dna_rc()
        elif my_choice == 3:
            keep_going()
       
def main():
    user_options()

main()
