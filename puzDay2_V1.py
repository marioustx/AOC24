inputDemo = "input_v1.txt"
outputDemo = "outputPart3.txt"
from icecream import ic
ic("disable")

def day2(inputDemo, outputDemo):
    with open(inputDemo) as file:
        count = 0
        results = []
        for line in file.readlines():
            report = list(map(int, line.strip().split()))
            temp = [i - j for i, j in zip(report[:-1], report[1:])]
            increase = all(map(lambda x: (x >= 1 and x <= 3) if x > 0 else False, temp))
            decrease = all(map(lambda x: (x >= -3 and x <= -1) if x < 0 else False, temp))
            #ic(results)
            
            results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
            count += 1 if increase or decrease else 0
    
    with open(outputDemo, 'w') as outfile:
        outfile.write(f"Count: {count}\n")
        for result in results:
            outfile.write(result + "\n")
    
    return count

print(day2(inputDemo, outputDemo))
