import re 
import math
if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

def parseTaskOne(line): 
    return re.findall("\d*\d", line)

# Speed = distance / time 
def taskOne():
    total = 1
    with open(getFilePath()) as file:
        times = parseTaskOne(file.readline())
        distance = parseTaskOne(file.readline()) 

    for index, time in enumerate(times):
        waysToFinish = 0
        for i in range(1, int(time)):
            if(((int(time) - i) * i) > int(distance[index])):
                waysToFinish += 1
        if(waysToFinish > 0):
            total *= waysToFinish
    
    return total

def parseTaskTwo(line):
    return int(''.join(re.findall("\d", line)))

def taskTwo():
    with open(getFilePath()) as file:
        time = parseTaskTwo(file.readline())  
        distance = parseTaskTwo(file.readline())
        waysToFinish = 0
        for i in range(1, time):
            if(((time - i) * i) > distance):
                waysToFinish += 1
        return waysToFinish
        
# Optimum solution by calculating the discriminant. 
def optimalTaskTwo():
    with open(getFilePath()) as file:
        time = parseTaskTwo(file.readline())  
        distance = parseTaskTwo(file.readline())
    return int(math.sqrt(time ** 2 - (4 * distance)))

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")