def readFile(path):
    
    with open(path, encoding="utf-8") as file:
        return file.readlines()


def linesToWords(lines):

    words = []

    for line in lines:
        newLine = line.replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace("-", " ").replace(",", " ").lower().strip()
        words += newLine.split(" ")
    
    return words
    

def calcFreq(words):
    wordFreq = {}

    for word in words:
        if len(word) == 0: continue
        if word in wordFreq:
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1

    return sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)


def writeToFile(path, output):
    with open(path, "w", encoding="utf-8") as file:
        for key, val in output:
            file.write(f"{key}:{val}\n")

lines = readFile("./data/first_task.txt")
words = linesToWords(lines)
wordFreq = calcFreq(words)
writeToFile("./results/first_task_result.txt", wordFreq)
