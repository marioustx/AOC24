# author: Alex Latch
# 12/05/2024

from icecream import ic
#ic.disable
ic.configureOutput(prefix='Invalid Rule: ')
lines = open("day4/inputDay4.txt").read().split("\n")
grid = [list(line) for line in lines]


def check_direction_for_word(grid, word, start_row, start_col, row_dir, col_dir):
    if start_row + (len(word) - 1) * row_dir < 0:
        return False
    if start_row + (len(word) - 1) * row_dir >= len(grid):
        return False
    if start_col + (len(word) - 1) * col_dir < 0:
        return False
    if start_col + (len(word) - 1) * col_dir >= len(grid[0]):
        return False

    for i in range(len(word)):
        if grid[row + i * row_dir][col + i * col_dir] != word[i]:
            return False

    return True


search_directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
word = "XMAS"
count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        for row_dir, col_dir in search_directions:
            if check_direction_for_word(grid, word, row, col, row_dir, col_dir):
                count = count + 1

print(count)
# Author: alex Latch