# Define the string
outputDemo = "day7/outputDay7.txt"

data = '''Results\tInput1\tInput2\tInput3\tInput4
190\t10\t19\t\t
3267\t81\t40\t27\t
83\t17\t5\t\t
156\t15\t6\t\t
7290\t6\t8\t6\t15
161011\t16\t10\t13\t
192\t17\t8\t14\t
21037\t9\t7\t18\t13
292\t11\t6\t16\t20
30\t11\t19\t\t'''

# Write the string to a text file
with open('data.txt', 'w') as file:
    file.write(data)

# Read the content of the text file and create a grid
grid = []
with open('data.txt', 'r') as file:
    for line in file:
        grid.append(line.strip().split('\t'))

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
header = grid[0] + ['Operator1', 'Operator2', 'Operator3','Operator4']
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
