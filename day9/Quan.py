index = 0
block_type = 1
num_char = 0
arr = []
with open('Day9\InputDay9Full.txt', 'r') as input:
    for line in input.readlines():
        for item in line.strip().replace('\n', ''):
            if block_type == 1:
                for i in range(0, int(item)):
                    arr.append(index)
                    num_char += 1
                block_type = 0
                index += 1
            elif block_type == 0:
                for i in range(0, int(item)):
                    arr.append('.')
                block_type = 1

last = len(arr) - 1
for i in range(0, num_char):
    for j in range(last, 0, -1):
        if arr[i] == '.' and arr[j] != '.':
            arr[i] = arr[j]
            arr[j] = '.'
            last = j
            break

 

 # Write the final result to a text file
    with open('day9\Array.txt', 'w') as output_file:
        output_file.write(str(arr))
index = 0
sum = 0
for i in arr:
    if i != '.':
        sum += index * i
    index += 1
print(sum)  # 6471961544878
