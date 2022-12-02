#Solution 1
rps = [] 
with open("day2.txt") as f:
    for line in f: #for each line in f
            data = line.strip().split(" ") 
            for n in data:
                rps.append(n)
score = 0
elf = ""
i = 0
while(i < len(rps)): 
    if(rps[i] == 'A' and rps[i+1] == 'Y'):
        score+=8
    elif(rps[i] == 'B' and rps[i+1] == 'Z'):
        score+=9
    elif(rps[i] == 'C' and rps[i+1] == 'X'):
        score+=7
    elif(rps[i] == 'A' and rps[i+1] == 'X'):
        score+=4
    elif(rps[i] == 'B' and rps[i+1] == 'Y'):
        score+=5
    elif(rps[i] == 'C' and rps[i+1] == 'Z'):
        score+=6
    elif(rps[i] == 'A' and rps[i+1] == 'Z'):
        score+=3
    elif(rps[i] == 'B' and rps[i+1] == 'X'):
        score+=1
    elif(rps[i] == 'C' and rps[i+1] == 'Y'):
        score+=2
    i+=2
print("Solution 1: ",score) 

#Solution 2 
rps.clear()
with open("day2.txt") as f:
    for line in f: #for each line in f
            data = line.strip().split(" ") 
            for n in data:
                rps.append(n)

score = 0
i = 0
while(i < len(rps)): 
    if(rps[i + 1] == 'X'):
        if(rps[i] == 'A'):
            score+=3
        elif(rps[i] == 'B'):
            score+=1
        elif(rps[i] == 'C'):
            score+=2
    elif(rps[i+1] == 'Y'):
        if(rps[i] == 'A'):
            score+=4
        elif(rps[i] == 'B'):
            score+=5
        elif(rps[i] == 'C'):
            score+=6 
    elif(rps[i + 1] == 'Z'):
        if(rps[i] == 'A'):
            score+=8
        elif(rps[i] == 'B'):
            score+=9
        elif(rps[i] == 'C'):
            score+=7
    i+=2 


print("Solution 2: ",score)