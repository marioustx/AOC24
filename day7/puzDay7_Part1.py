# Define the file paths
inputDemo = "day7/InputDay7.txt"
outputDemo = "day7/outputDay7.txt"

# Read the content of the text file and create a grid
grid = []
with open(inputDemo, 'r') as file:
    for line in file:
        grid.append(line.strip().split())  # Corrected split method

# Function to find the operators that result in the given result
def find_operators(inputs, result):
    from itertools import product

    operators = ['+', '*']
    for ops in product(operators, repeat=len(inputs)-1):
        expression = str(inputs[0])
        for i in range(1, len(inputs)):
            if inputs[i] != '':
                expression += ' ' + ops[i-1] + ' ' + str(inputs[i])
        try:
            # Evaluate the expression left to right
            tokens = expression.split()
            total = int(tokens[0])
            for j in range(1, len(tokens), 2):
                op = tokens[j]
                num = int(tokens[j+1])
                if op == '+':
                    total += num
                elif op == '*':
                    total *= num
            if total == result:
                return ops
        except:
            continue
    return None

# Add operator columns to the grid
header = grid[0] + ['Operator1', 'Operator2', 'Operator3', 'Operator4']
new_grid = [header]

for row in grid[1:]:
    inputs = [int(x) if x != '' else '' for x in row[1:]]
    result = int(row[0])
    operators = find_operators(inputs, result)
    if operators:
        new_row = row + list(operators)
    else:
        new_row = row + [''] * (len(inputs) - 1)
    new_grid.append(new_row)

# Print the new grid with operators
for row in new_grid:
    print(row)

# Save the modified grid to a text file
with open(outputDemo, 'w') as outfile:
    for row in new_grid:
        outfile.write(" ".join(row) + "\n")
