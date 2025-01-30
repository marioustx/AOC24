from icecream import ic

# Define the grid with the given data
grid = [
    [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    [".", ".", ".", "#", ".", ".", ".", ".", "0", ".", ".", "."],
    ["#", ".", ".", ".", "#", "0", ".", ".", ".", ".", "#", "."],
    [".", ".", "#", ".", ".", ".", ".", "0", ".", ".", ".", "."],
    [".", ".", ".", ".", "0", ".", ".", ".", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", ".", "A", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."]
]

# Function to print the grid using icecream's ic
def print_grid(grid):
    for row in grid:
        ic("".join(row))

# Function to calculate the distance between antennas and add antinodes
def add_antinodes(grid, antenna_char):
    # Concatenate all rows to form one string
    concatenated_grid = "".join("".join(row) for row in grid)
    
    # Find all positions of the antennas
    antenna_positions = [i for i, char in enumerate(concatenated_grid) if char == antenna_char]
    
    if len(antenna_positions) < 2:
        return grid  # If less than two antennas are found, return the original grid
    
    # Calculate distances between each pair of antennas
    distances = [antenna_positions[j] - antenna_positions[i] for i in range(len(antenna_positions)) for j in range(i + 1, len(antenna_positions))]
    
    # Add antinodes based on the distances
    for distance in distances:
        for pos in antenna_positions:
            # Antinode left to the antenna
            if 0 <= pos - distance < len(concatenated_grid):
                concatenated_grid = concatenated_grid[:pos - distance] + '$' + concatenated_grid[pos - distance + 1:]
            # Antinode right to the antenna
            if 0 <= pos + distance < len(concatenated_grid):
                concatenated_grid = concatenated_grid[:pos + distance] + '$' + concatenated_grid[pos + distance + 1:]
    
    # Convert the concatenated string back to a grid
    grid_with_antinodes = [list(concatenated_grid[i:i+12]) for i in range(0, len(concatenated_grid), 12)]
    
    return grid_with_antinodes

# Add antinodes for each type of antenna
grid_with_antinodes = add_antinodes(grid, '0')
grid_with_antinodes = add_antinodes(grid_with_antinodes, 'A')
grid_with_antinodes = add_antinodes(grid_with_antinodes, '1')

# Print the grid with antinodes
print_grid(grid_with_antinodes)

# Write the output to a file named 'Output.txt'
with open('day8\\Output.txt', 'w') as f:
    for row in grid_with_antinodes:
        f.write("".join(row) + "\n")
