import re
from functools import reduce

inputDemo = 'day3/inputDay3.txt'
outputDemo = "day3/outputDay3.txt"

def day3(inputDemo, outputDemo):
    results = []
    
    # Open and read the input file
    with open(inputDemo) as file:
        for line in file:
            # Process each line if needed
            results.append(line.strip())
    
    # Write results to the output file
    with open(outputDemo, 'w') as outfile:
        for result in results:
            outfile.write(result + "\n")
    
    return results

# Call the function and print the results
print(day3(inputDemo, outputDemo))
