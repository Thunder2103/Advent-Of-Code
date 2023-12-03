from puzzle_input import getFilePath

def getNumber(index, engineArray, lineNumber, lineLength):
    number = engineArray[lineNumber][index]
    left = index - 1
    while(left >= 0 and engineArray[lineNumber][left].isnumeric()):
        number = engineArray[lineNumber][left] + number
        left -= 1
    right = index + 1
    while(right < lineLength and engineArray[lineNumber][right].isnumeric()):
        number += engineArray[lineNumber][right] 
        right += 1
    return int(number)

def checkLeft(symbolIndex, lineNumber, engineArray):    
    if(symbolIndex == 0): return False
    if(engineArray[lineNumber][symbolIndex - 1].isnumeric()): 
        return True
    else: return False  


def checkRight(symbolIndex, lineNumber, engineArray, lineLength):
    if(symbolIndex == lineLength - 1): return False
    if(engineArray[lineNumber][symbolIndex + 1].isnumeric()): 
        return True
    else: return False  

def checkUp(symbolIndex, lineNumber, engineArray): 
    if(lineNumber == 0): return False
    if(engineArray[lineNumber - 1][symbolIndex].isnumeric()): 
        return True
    else: return False  

def checkDown(symbolIndex, lineNumber, engineArray, numberLines):
    if(lineNumber == numberLines - 1): return False
    if(engineArray[lineNumber + 1][symbolIndex].isnumeric()): 
        return True
    else: return False  

def taskOne():
    total = 0
    numberLines = 0 
    lineNumber = 0 
    lineLength = 0
    engineArray = []
    symbolsArray = []

    with open(getFilePath()) as file:
        for line in file:
            line = line.rstrip()
            engineArray.append([])
            symbolsArray.append([])
            for index, char in enumerate(line):
                if(not char.isnumeric() and char != "."):
                    symbolsArray[lineNumber].append(index)
                engineArray[lineNumber].append(char)
            lineNumber+=1
            numberLines+=1 
        
        file.seek(0)
        lineLength = len(file.readline().rstrip())

    lineNumber = -1
    for i in range(len(symbolsArray)):
        lineNumber+=1
        if(symbolsArray[i] == []): continue
        for j in range(len(symbolsArray[i])):
            if(checkLeft(symbolsArray[i][j], i, engineArray)):
                total += getNumber(symbolsArray[i][j] - 1, engineArray, i, lineLength)
            if(checkRight(symbolsArray[i][j], i, engineArray, lineLength)):
                total += getNumber(symbolsArray[i][j] + 1, engineArray, i, lineLength)
            if(checkUp(symbolsArray[i][j], i, engineArray)):
                total += getNumber(symbolsArray[i][j], engineArray, i - 1, lineLength)
            else:
                if(checkLeft(symbolsArray[i][j], i - 1, engineArray)): 
                    total  += getNumber(symbolsArray[i][j] - 1, engineArray, i - 1, lineLength)
                if(checkRight(symbolsArray[i][j], i - 1, engineArray, lineLength)):
                    total += getNumber(symbolsArray[i][j] + 1, engineArray, i - 1, lineLength)
            if(checkDown(symbolsArray[i][j], lineNumber, engineArray, numberLines)):
                total += getNumber(symbolsArray[i][j], engineArray, i + 1, lineLength)
            else:
                if(checkLeft(symbolsArray[i][j], i + 1, engineArray)): 
                    total += getNumber(symbolsArray[i][j] - 1, engineArray, i + 1, lineLength)
                if(checkRight(symbolsArray[i][j], i + 1, engineArray, lineLength)):
                    total += getNumber(symbolsArray[i][j] + 1, engineArray, i + 1, lineLength)
    return total

def taskTwo():
    total = 0
    numberLines = 0 
    lineNumber = 0 
    lineLength = 0
    engineArray = []
    gearsArray = []

    with open(getFilePath()) as file:
        for line in file:
            line = line.rstrip()
            engineArray.append([])
            gearsArray.append([])
            for index, char in enumerate(line):
                if(char == "*"):
                    gearsArray[lineNumber].append(index)
                engineArray[lineNumber].append(char)
            lineNumber+=1
            numberLines+=1 
        
        file.seek(0)
        lineLength = len(file.readline().rstrip())

    lineNumber = -1
    for i in range(len(gearsArray)):
        lineNumber+=1
        if(gearsArray[i] == []): continue
        for j in range(len(gearsArray[i])):
            numAdjGear = 0
            ratio = 1
            if(checkLeft(gearsArray[i][j], i, engineArray)):
                ratio *= getNumber(gearsArray[i][j] - 1, engineArray, i, lineLength)
                numAdjGear += 1
            if(checkRight(gearsArray[i][j], i, engineArray, lineLength)):
                ratio *= getNumber(gearsArray[i][j] + 1, engineArray, i, lineLength)
                numAdjGear += 1
            if(checkUp(gearsArray[i][j], i, engineArray)):
                ratio *= getNumber(gearsArray[i][j], engineArray, i - 1, lineLength)
                numAdjGear += 1
            else:
                if(checkLeft(gearsArray[i][j], i - 1, engineArray)): 
                    ratio *= getNumber(gearsArray[i][j] - 1, engineArray, i - 1, lineLength)
                    numAdjGear += 1
                if(checkRight(gearsArray[i][j], i - 1, engineArray, lineLength)):
                    ratio *= getNumber(gearsArray[i][j] + 1, engineArray, i - 1, lineLength)
                    numAdjGear += 1
            if(checkDown(gearsArray[i][j], lineNumber, engineArray, numberLines)):
                ratio *= getNumber(gearsArray[i][j], engineArray, i + 1, lineLength)
                numAdjGear += 1
            else:
                if(checkLeft(gearsArray[i][j], i + 1, engineArray)): 
                    ratio *= getNumber(gearsArray[i][j] - 1, engineArray, i + 1, lineLength)
                    numAdjGear += 1
                if(checkRight(gearsArray[i][j], i + 1, engineArray, lineLength)):
                    ratio *= getNumber(gearsArray[i][j] + 1, engineArray, i + 1, lineLength)
                    numAdjGear += 1
            
            if(numAdjGear == 2): 
                total += ratio
    return total    

print(taskOne())
print(taskTwo())