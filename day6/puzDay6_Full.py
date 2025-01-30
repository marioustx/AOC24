# Define the string to be written to the file
content = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
inputDemo = "day6/gridDay6.txt"
outputDemo = "outputDay6.txt"

# Write the string to a text file
#with open(inputDemo, 'w') as file:
#    file.write(content)

# Read the content from the text file
with open(inputDemo, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

# Find the starting position of '^'
start_pos = None
for i, row in enumerate(grid):
    if '^' in row:
        start_pos = (i, row.index('^'))
        break

# Define directions (up, right, down, left)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_direction = 0  # Start with moving up

# Move and replace dots with X
x, y = start_pos
grid[x][y] = '.'  # Replace '^' with '.'

while True:
    dx, dy = directions[current_direction]
    x += dx
    y += dy

    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        break  # Out of bounds

    if grid[x][y] == '#':
        # Move one position back
        x -= dx
        y -= dy
        current_direction = (current_direction + 1) % 4  # Turn 90 degrees right
    else:
        grid[x][y] = 'X'

print("Modified grid:")
print_grid(grid)

# Save the modified grid to a text file
with open('day6/modified_grid.txt', 'w') as outfile:
    for row in grid:
        outfile.write("".join(row) + "\n")

print("Modified grid saved to day6/modified_grid.txt")
