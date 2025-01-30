def process_characters():
    # Read the value from the text file
    with open('inputTest.txt', 'r') as file:
        cell_value = file.read().strip()
    
    # Initialize variables
    result = ""
    odd_counter = 0
    char_count = len(cell_value)
    
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
    
    # Write the result to a text file
    with open('outputTest.txt', 'w') as output_file:
        output_file.write(result)

# Call the function
process_characters()
