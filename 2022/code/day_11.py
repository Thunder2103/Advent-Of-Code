from puzzle_input import getFilePath

class Monkey:
    def __init__(self):
        self.item = [] 
        self.operationOp = 0
        self.operationNum = 0 
        self.throwTrue = 0
        self.throwFalse = 0
        self.test = 0
        pass

def taskOne():
    product = 1
    monkeys = [Monkey() for i in range(8)] 
    inspected = [0 for i in range(8)]

    with open(getFilePath()) as f: 
        for x in range(len(monkeys)):  
            for line in f: 
                line = line.split()
                if(len(line) == 0):
                    break
                if(line[0] == "Monkey"):
                    continue 
                if(line[0] == "Starting"):
                    for i in range(2, len(line)):
                        monkeys[x].item.append(int(line[i].replace(",", "")))
                    continue
                if(line[0] == "Operation:"):
                    if(line[4] == "*"):
                        monkeys[x].operationOp = 1
                    if(line[5] == "old"):
                        continue
                    else:
                        monkeys[x].operationNum = int(line[5])
                        continue    
                if(line[0] == "Test:"):
                    monkeys[x].test = int(line[3])      
                    product *= int(line[3])
                    continue
                if(line[0] == "If"):
                    monkeys[x].throwTrue = int(line[-1])
                    line = f.readline().split()
                    monkeys[x].throwFalse = int(line[-1])
                    continue    

    for x in range(20):
        for y in range(len(monkeys)): 
            while(len(monkeys[y].item) > 0): 
                inspected[y] +=1
                currentItem = monkeys[y].item.pop(0)
                if(monkeys[y].operationOp == 0):
                    currentItem += monkeys[y].operationNum 
                if(monkeys[y].operationOp == 1):
                    if(monkeys[y].operationNum == 0):
                        currentItem*= currentItem
                    else:
                        currentItem *= monkeys[y].operationNum  
                currentItem //= 3
                if(currentItem % int(monkeys[y].test) == 0):
                    monkeys[monkeys[y].throwTrue].item.append(currentItem)
                else:
                    monkeys[monkeys[y].throwFalse].item.append(currentItem)

    inspected = sorted(inspected)    
    return inspected[-2] * inspected[-1] 

def taskTwo():
    product = 1
    monkeys = [Monkey() for i in range(8)] 
    inspected = [0 for i in range(8)]
    with open(getFilePath()) as f: 
        for x in range(len(monkeys)):  
            for line in f: 
                line = line.split()
                if(len(line) == 0):
                    break
                if(line[0] == "Monkey"):
                    continue 
                if(line[0] == "Starting"):
                    for i in range(2, len(line)):
                        monkeys[x].item.append(int(line[i].replace(",", "")))
                    continue
                if(line[0] == "Operation:"):
                    if(line[4] == "*"):
                        monkeys[x].operationOp = 1
                    if(line[5] == "old"):
                        continue
                    else:
                        monkeys[x].operationNum = int(line[5])
                        continue    
                if(line[0] == "Test:"):
                    monkeys[x].test = int(line[3])      
                    product *= int(line[3])
                    continue
                if(line[0] == "If"):
                    monkeys[x].throwTrue = int(line[-1])
                    line = f.readline().split()
                    monkeys[x].throwFalse = int(line[-1])
                    continue             

    for x in range(10000):
        for y in range(len(monkeys)): 
            while(len(monkeys[y].item) > 0): 
                inspected[y] +=1
                currentItem = monkeys[y].item.pop(0)
                if(monkeys[y].operationOp == 0):
                    currentItem += monkeys[y].operationNum 
                if(monkeys[y].operationOp == 1):
                    if(monkeys[y].operationNum == 0):
                        currentItem*= currentItem
                    else:
                        currentItem *= monkeys[y].operationNum   
                currentItem %= product 
                if(currentItem % monkeys[y].test == 0):
                    monkeys[monkeys[y].throwTrue].item.append(currentItem)
                else:
                    monkeys[monkeys[y].throwFalse].item.append(currentItem)

    inspected = sorted(inspected)    
    return inspected[-2] * inspected[-1] 

print(taskOne())
print(taskTwo())