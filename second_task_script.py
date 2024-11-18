import math

def readFile(path):
    
    with open(path, encoding="utf-8") as file:
        return file.readlines()

def calcRoots(lines):

    sumOfRoots = []

    for index, line in enumerate(lines):
        newLine = line.split(" ")
        currentSum = 0

        for numberStr in newLine:
            number = int(numberStr)
    
            if number > 0:
                currentSum += math.sqrt(number)
        
        sumOfRoots.append(int(currentSum))

    return sumOfRoots

def writeToFile(path, result):
    with open(path, "w") as file:
        for value in result:
            file.write(f"{value}\n")

        file.write(f"\n{max(result)}\n{min(result)}")

lines = readFile("./data/second_task.txt")
sumOfRoots = calcRoots(lines)
writeToFile("./results/second_task_result.txt", sumOfRoots)

