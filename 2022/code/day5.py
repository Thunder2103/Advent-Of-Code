from puzzle_input import getFilePath

# Solution 1
def taskOne():
    value = 9
    stack = [[] for i in range(value)]
    x = 1
    space = 0
    stackVal = 0 
    i = 0
    with open(getFilePath()) as f:
        line = f.readline()   
        while(not (line[1].isdigit())):
            while(i < len(line)):
                if(line[i] == "["):
                    stack[stackVal].append(line[i+1])
                    stackVal+=1
                    i+=2
                    space = 0
                    continue 
                elif(line[i] == " "): 
                    space +=1
                    if(space % 4 == 0):
                        space = 0 
                        stackVal+=1 
                    i+=1
                    continue
                i+=1
            line = f.readline()
            i = 0 
            space = 0
            stackVal  = 0
        f.readline()
        for line in f:
            data = line.strip().split(" ") 
            loop = int(data[1])
            while(x <= loop):
                popped = stack[int(data[3])-1].pop(0)
                stack[int(data[5])-1].insert(0, popped) 
                x+=1
            x = 1
    return [i[0] for i in stack] 

def taskTwo(): 
    value = 9
    stack = [[] for i in range(value)]
    x = 1
    space = 0
    stackVal = 0 
    i = 0
    with open(getFilePath()) as f:
        line = f.readline()   
        while(not (line[1].isdigit())):
            while(i < len(line)):
                if(line[i] == "["):
                    stack[stackVal].append(line[i+1])
                    stackVal+=1
                    i+=2
                    space = 0
                    continue 
                elif(line[i] == " "): 
                    space +=1
                    if(space % 4 == 0):
                        space = 0 
                        stackVal+=1 
                    i+=1
                    continue
                i+=1
            line = f.readline()
            i = 0 
            space = 0
            stackVal  = 0
        f.readline()
        for line in f:
            data = line.strip().split(" ") 
            loop = int(data[1])
            while(loop > 0):
                popped = stack[int(data[3])-1].pop(loop - 1)
                stack[int(data[5])-1].insert(0, popped) 
                loop-=1
    return [i[0] for i in stack] 

print(taskOne())
print(taskTwo())