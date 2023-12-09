if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

def nextReading(histroy: list):
    if(all(x == 0 for x in histroy)): return 0
    else: return histroy[-1] + nextReading([histroy[i + 1] - histroy[i] for i in range(len(histroy) - 1)]) 

def previousReading(histroy: list):
    if(all(x == 0 for x in histroy)): return 0
    else: return histroy[0] - previousReading([histroy[i + 1] - histroy[i] for i in range(len(histroy) - 1)]) 

def taskOne():
    with open(getFilePath()) as file:
        readings = [list(map(int, line.rstrip().split(" "))) for line in file]
    total = 0
    for histroy in readings:  
        total += nextReading(histroy)    
    return total

def taskTwo():
    with open(getFilePath()) as file:
        readings = [list(map(int, line.rstrip().split(" "))) for line in file]
    total = 0
    for histroy in readings:  
        total += previousReading(histroy)    
    return total

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")