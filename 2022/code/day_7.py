if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

dirSize = [] 

def taskOne():
    currentDir = [] 
    runningSize = []
    i = 0 
    sum = 0 
    with open(getFilePath()) as f:
        array = [] 
        for lines in f:
            data = lines.strip().split(" ")
            array.append(data) 
        while (i < (len(array))): 
            if(array[i][1] == "ls"):
                i+=1
                while(i < len(array) and array[i][0] != "$"):
                    if(array[i][0].isnumeric()):
                        sum += int(array[i][0])  
                    i+=1  
                n = 1
                if(len(currentDir) > 1):
                    while(n < len(currentDir)):
                        runningSize[-n] = int(runningSize[-n]) + sum
                        n+=1
                runningSize.append(sum)
                sum = 0
                continue
            elif(array[i][1] == "cd"):
                if(array[i][2] == ".."):
                    dirSize.append(runningSize[-1])
                    runningSize.pop()
                    currentDir.pop(0)
                else:
                    currentDir.insert(0, array[i][2])
            i+=1    
    dirSize.append(runningSize.pop())
    dirSize.append(runningSize.pop())
    sum = 0 
    for num in dirSize:
        if(num < 100000):
            sum += num
    return sum

def taskTwo():
    space = 70000000 - dirSize[-1]
    space = 30000000 - space
    dirSize.sort()
    i = 0 
    for i in range(len(dirSize)):
        if(dirSize[i] > space):
            return dirSize[i]

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")