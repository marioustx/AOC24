inputDemo = "input_v1.txt"
outputDemo = "output.txt"

def day2(inputDemo, outputDemo):
    with open(inputDemo) as file:
        results = []
        for line in file.readlines():
            report = list(map(int, line.strip().split()))
            temp = [i - j for i, j in zip(report[:-1], report[1:])]
            increase = all(map(lambda x: (x >= 1 and x <= 3) if x > 0 else False, temp))
            decrease = all(map(lambda x: (x >= -3 and x <= -1) if x < 0 else False, temp))
            
            results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
    
    with open(outputDemo, 'w') as outfile:
        for result in results:
            outfile.write(result + "\n")
    
    return results

print(day2(inputDemo, outputDemo))
