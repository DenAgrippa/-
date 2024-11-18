def readFile(path):
    
    with open(path, encoding="utf-8") as file:
        return file.readlines()
    
def linesToString(lines):

    string = ""
    for line in lines:
        newLine = line.replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace("-", "").replace(",", "").replace(" ", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").lower().strip()
        string += newLine
        string = list(string)

    return string

def calcFreq(string):
    letterFreq = {}
    vowels = ['a', 'i', 'e', 'o', 'u', 'y']

    for letter in string:
        if letter not in vowels:
            continue
        if letter in letterFreq:
            letterFreq[letter] += 1
        else:
            letterFreq[letter] = 1

    for letter in letterFreq:
        letterFreq[letter] = [letterFreq[letter], ((letterFreq[letter])/letterCount)] #Результат в формате буква:[колличество,доля]
    return sorted(letterFreq.items(), key= lambda x: x[1], reverse=True)

def writeAmountToFile(path, output):
    with open(path, "w", encoding="utf-8") as file:
        for key, val in output:
            file.write(f"{key}:{val}\n")





lines  = readFile("./data/first_task.txt")
string = linesToString(lines)

letterCount = len(string)
letterFreq = calcFreq(string)
writeAmountToFile("./results/first_task_second_part_1.txt", letterFreq)