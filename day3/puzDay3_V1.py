import re
from functools import reduce

inputDemo = 'day3/inputDay3.txt'
outputDemo = "day3/outputDay3.txt"

def day3(inputDemo):
    # Open and read the input file
    with open(inputDemo) as file:
        memory = file.read()
        # Declare pattern
        pattern = 'mul\(\d+,\d+\)'
        matches = re.findall(pattern, memory)
        pattern = '\d+'
        nums = [list(map(int, y)) for y in (re.findall(pattern, x) for x in matches)]
        return sum(map(lambda z: reduce(lambda x, y: x * y, z), nums))

if __name__ == '__main__':
    result = day3(inputDemo)
    print(result)
    
    # Save the result to outputDay3.txt
    with open(outputDemo, 'w') as outfile:
        outfile.write(str(result))
