def readFile(path):
    
    with open(path, encoding="utf-8") as file:
        return file.readlines()
    
def replaceNA(lines):
    newLines = []

    for line in lines:
        newLine = line.split(" ")

        for index, number in enumerate(newLine):
            if number == "N/A":
                newLine[index] = (newLine[index-1] + (int(newLine[index+1])))
            else:
                newLine[index] = int(number)
        newLines.append(newLine)

    return newLines

def filtering(lines):
    
    filteredLines = []

    for line in lines:
        newLine = list(filter(lambda n: n%3 == 0, line))
        filteredLines.append(newLine)

    return filteredLines

def sumOfEachLine(lines):
    listOfSums = []

    for line in lines:
        sum = 0
        for number in line:
            sum += number
        listOfSums.append(sum)
    
    return listOfSums

def writeToFile(path, result):
    with open(path, "w") as file:
        for number in result:
            file.write(f"{number}\n")

lines = readFile("./data/third_task.txt")
replacedNA = replaceNA(lines)
filteredLines = filtering(replacedNA)
sums = sumOfEachLine(filteredLines)
writeToFile("./results/third_task_results.txt", sums)