from dictionary import *

def get_options():
    print("1 - Get p distance matrix")
    print("2 - Exit")

    
def process_exit():
    user_inp = input("Press Y to continue... ")
    user_inp = user_inp.capitalize()

    if user_inp == "Y":
        return True
    else:
        print("Goodbye!")
        return False

   
def my_sequences():

    number_of_sequences_to_create = int(input("Please type the number of sequences you would like to check: "))
    number_of_bases =  int(input("Please enter the number of bases in each sequence: "))
    my_sequences = []

    for i in range(number_of_sequences_to_create):
       
        my_sequence = input(f"Please enter {number_of_bases} bases for each sequence (current sequence {i + 1}): ")
        my_list_sequence = []

        while len(my_sequence) != number_of_bases:
            print(f"Incorrect number of bases please enter {number_of_bases} bases!")
            my_sequence = input(f"Please enter {number_of_bases} bases for each sequence (current sequence {i + 1}): ")

            
        for x in my_sequence:
            my_list_sequence.append(x)

        my_sequences.append(my_list_sequence)
        print(f"Current sequences: {my_sequences}")
    
    return my_sequences




def get_matrix():
    my_sequences_to_test = my_sequences()
    get_distance_mat = get_p_distance_matrix(my_sequences_to_test)
    print("P Distance Matrix: ")
    for i in get_distance_mat:
        print(i)
    return get_distance_mat

def handle_options():
    
    keep_running = True
    
    while keep_running == True: 
        get_options()
        my_choice = int(input("Please select what you would like to do: "))
        
        if my_choice == 1:
            get_matrix()
            keep_running = process_exit()
            
            
        elif my_choice == 2:
           keep_running =  process_exit()



def main():
    handle_options()

if __name__ == "__main__":
    main()