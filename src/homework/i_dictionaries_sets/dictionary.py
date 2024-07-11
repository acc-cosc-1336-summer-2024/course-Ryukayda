

def get_p_distance(list1, list2):

    hamming_distance = 0
    count = 0

    if len(list1) == len(list2):

        for item in list1:
            if item not in list2[count]:
                hamming_distance += 1
            count += 1
    
        p_distance = hamming_distance / count
        
        return p_distance

    
    else:
        print("Mismatch, ERROR")
        return False
    




def get_p_distance_matrix(parameter):
    p_distance_matrix = []
    my_sequences = parameter 

    for dna_sequence in my_sequences:
        dna_sequence_list =[]

        my_value = 0 

        
        while my_value < len(my_sequences) and not my_value > len(my_sequences):
            my_p_distance = get_p_distance(my_sequences[my_value], dna_sequence)
            dna_sequence_list.append(my_p_distance)
            my_value += 1
            
        

        p_distance_matrix.append(dna_sequence_list)
    

    return p_distance_matrix