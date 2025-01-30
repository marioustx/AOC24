from icecream import ic
#ic(disable)
def process_characters():
    # Read the value from the text file
    with open('day9/outputTemp.txt', 'r') as file:
        cell_value = file.read().strip().replace('\n', '')
    
    # Initialize variables
    result = ""
    char_count = len(cell_value)
    num_list = []

    # Loop through each character in the cell value
    for i in range(char_count):
        current_char = cell_value[i]
        
        if current_char.isdigit():
            num = int(current_char)
            num_list.append(num * i)  # Multiply the numerical value by its position index

    # Sum all the elements of the list
   # ic(num_list)
    final_sum = sum(num_list)
    
    # Convert the sum to a string
    final_result = str(final_sum)
    
    # Write the final result to a text file
    with open('day9/outputFinal.txt', 'w') as output_file:
        output_file.write(final_result)

 # Write the final result to a text file
    with open('day9/outputNumList.txt', 'w') as output_file:
        output_file.write(str(num_list))

# Call the function
process_characters()
