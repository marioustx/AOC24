# Open the text file and read its content
with open('day7\InputDay7.txt', 'r') as file:
    lines = file.readlines()

# Split the first row to get the headers
headers = lines[0].strip().split()



# Initialize a list to store the rows of values
data = []

# Process each row of values
for line in lines[1:]:
    # Split the line by spaces and convert each value to the appropriate type
    values = [int(value) if value.isdigit() else float(value) if '.' in value else value for value in line.strip().split()]
    data.append(values)

# Print the headers and data for verification
print("Headers:", headers)
print("Data:")
for row in data:
    print(row)
