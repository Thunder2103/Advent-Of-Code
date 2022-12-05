stack1 = []
stack2 = []
stack3 = []
stack4= []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

numArray = []

stackDict = {
    1: stack1,
    2: stack2, 
    3: stack3, 
    4: stack4, 
    5: stack5,
    6: stack6,
    7: stack7, 
    8: stack8, 
    9: stack9
}

x = 1
space = 0
stackVal = 1
i = 0
with open("day5.txt") as f:
    line = f.readline()   
    while(not (line[1].isdigit())):
        while(i < len(line)):
            if(line[i] == "["):
                stackDict[stackVal].append(line[i+1])
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
        stackVal  = 1 
    
    f.readline()
    for line in f:
        data = line.strip().split(" ") 
        loop = int(data[1])
        while(x <= loop):
            popped = stackDict[int(data[3])].pop(0)
            stackDict[int(data[5])].insert(0, popped) 
            x+=1
        x = 1
        
print("Solution 1:",stack1[0], stack2[0], stack3[0], stack4[0], stack5[0], stack6[0], stack7[0], stack8[0], stack9[0]) 
stack1.clear()
stack2.clear()
stack3.clear()
stack4.clear()
stack5.clear()
stack6.clear()
stack7.clear()
stack8.clear()
stack9.clear()  

space = 0
stackVal = 1
i = 0
with open("day5.txt") as f:
    line = f.readline()   
    while(not (line[1].isdigit())):
        while(i < len(line)):
            if(line[i] == "["):
                stackDict[stackVal].append(line[i+1])
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
        stackVal  = 1 
    
    f.readline()
    for line in f:
        data = line.strip().split(" ") 
        loop = int(data[1])
        while(loop > 0):
            popped = stackDict[int(data[3])].pop(loop - 1)
            stackDict[int(data[5])].insert(0, popped) 
            loop -=1
        x = 1 

print("Solution 2:",stack1[0], stack2[0], stack3[0], stack4[0], stack5[0], stack6[0], stack7[0], stack8[0], stack9[0]) 










        
