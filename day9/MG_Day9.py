def process_characters():
    # Read the value from the text file
    with open('day9/inputDay9Full.txt', 'r') as file:
        cell_value = file.read().strip().replace('\n', '')
    
    # Initialize variables
    result = ""
    odd_counter = 0
    char_count = len(cell_value)
    char_count_v1 = int(char_count / 2)
    
    # Loop through each character in the cell value
    for i in range(char_count):
        current_char = cell_value[i]
        
        if current_char.isdigit():
            num = int(current_char)
            
            if (i + 1) % 2 == 0:  # Even position (1-based index)
                result += '.' * num
            else:  # Odd position
                result += str(odd_counter) * num
                odd_counter += 1
            
            # Debugging: Print intermediate results
            print(f"i: {i + 1}, current_char: {current_char}, num: {num}, result: {result}, odd_counter: {odd_counter}")
    
    # Convert result to a list for manipulation
    result_list = list(result)
    
    # Function to find the maximum numerical character from the right
    def find_max_from_right(lst):
        max_num = -1
        max_index = -1
        for i in range(len(lst) - 1, -1, -1):
            if lst[i].isdigit() and int(lst[i]) > max_num:
                max_num = int(lst[i])
                max_index = i
        return max_index
    
    # Initialize pointers for dots
    dot_pointer = 0
    
    # Loop until all dots are swapped with the maximum numerical characters
    while dot_pointer < len(result_list):
        # Find the first dot from the left
        while dot_pointer < len(result_list) and result_list[dot_pointer] != '.':
            dot_pointer += 1
        
        # Find the maximum numerical character from the right
        max_num_index = find_max_from_right(result_list)
        
        # Swap positions if pointers are valid
        if dot_pointer < len(result_list) and max_num_index != -1:
            result_list[dot_pointer], result_list[max_num_index] = result_list[max_num_index], result_list[dot_pointer]
            dot_pointer += 1
    
    # Convert list back to string
    final_result = ''.join(result_list)
    
    # Write the final result to a text file
    with open('day9/outputTemp.txt', 'w') as output_file:
        output_file.write(final_result)

# Call the function
process_characters()
