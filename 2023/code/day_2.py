import math
import re 
from puzzle_input import getFilePath

def parse(line):
    return re.sub("Game|[,;:]", "", line.strip("\n")).lstrip().split(" ")

def taskOne():
    with open(getFilePath()) as file:
        total = 0
        gamePossible = True
        colorDict = {
            "red" : 12,
            "green": 13,
            "blue": 14
        }
        for line in file:
            line = parse(line)
            for i in range(2, len(line), 2): 
                if(int(line[i - 1]) > colorDict[line[i]]): 
                    gamePossible = False
                    break
                else:
                    gamePossible = True
            if(gamePossible): 
                total += int(line[0])
            gamePossible = True
        return total
    
def taskTwo():
     with open(getFilePath()) as file:
        total = 0
        colorDict = {
            "red" : 0,
            "green": 0,
            "blue": 0
        }
        for line in file:
            line = parse(line)
            for i in range(2, len(line), 2): 
                if(int(line[i - 1]) > colorDict[line[i]]):
                    colorDict[line[i]] = int(line[i - 1])
            total += math.prod(list(colorDict.values()))
            colorDict = dict.fromkeys(colorDict, 0) 
        return total

print(taskOne())
print(taskTwo())

            