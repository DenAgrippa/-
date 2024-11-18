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








lines = readFile("./data/third_task.txt")
print(replaceNA(lines))