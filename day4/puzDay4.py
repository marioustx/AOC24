import re
from functools import reduce

inputDemo = 'day4/inputDay4.txt'
outputDemo = "day3/outputDay3.txt"
lines = open('day4/inputDay4.txt').read().split("\n")
print(lines)

grid = [list(line) for line in lines]
print([grid])
cell1_1 = grid[8][9]
print([cell1_1])


