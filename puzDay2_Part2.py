inputDemo = "input_v1.txt"
outputDemo = "outputPart13.txt"
from icecream import ic
ic("disable")

def day2(inputDemo, outputDemo):
    def check_increase_decrease(report):
        temp = [i - j for i, j in zip(report[:-1], report[1:])]
        increase = all(map(lambda x: (x >= 1 and x <= 3) if x > 0 else False, temp))
        decrease = all(map(lambda x: (x >= -3 and x <= -1) if x < 0 else False, temp))
        return increase, decrease

    with open(inputDemo) as file:
        count = 0
        results = []
        for line in file.readlines():
            report = list(map(int, line.strip().split()))
            if len(report) != len(set(report)):
                # More than one duplicate
                results.append(f"{line.strip()} Increase: False Decrease: False")
                continue

            increase, decrease = check_increase_decrease(report)
            if increase or decrease:
                results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
                count += 1
                continue

            # Handle duplicates
            for i in range(len(report)):
                if report.count(report[i]) == 2:
                    # Remove first occurrence and check
                    temp_report = report[:i] + report[i+1:]
                    increase, decrease = check_increase_decrease(temp_report)
                    if increase or decrease:
                        results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
                        count += 1
                        break
                    # Remove second occurrence and check
                    temp_report = report[:report.index(report[i], i+1)] + report[report.index(report[i], i+1)+1:]
                    increase, decrease = check_increase_decrease(temp_report)
                    if increase or decrease:
                        results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
                        count += 1
                        break
            else:
                # No duplicates or no valid increase/decrease found
                for i in range(len(report)):
                    temp_report = report[:i] + report[i+1:]
                    increase, decrease = check_increase_decrease(temp_report)
                    if increase or decrease:
                        results.append(f"{line.strip()} Increase: {increase} Decrease: {decrease}")
                        count += 1
                        break
                else:
                    results.append(f"{line.strip()} Increase: False Decrease: False")

    with open(outputDemo, 'w') as outfile:
        outfile.write(f"Count: {count}\n")
        for result in results:
            outfile.write(result + "\n")
    
    return count

print(day2(inputDemo, outputDemo))
