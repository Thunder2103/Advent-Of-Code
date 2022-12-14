#This one doesn't run as slow as other days, that's good I guess
#Solution 1
rocks = set()
sand = set()
abyss = 0
lowest = 0

with open("day14.txt") as f:
    for line in f:
        line = line.strip().split("->")
        
        for x in range(len(line) - 1):
            current = list(map(int, line[x].strip().split(",")))
            next = list(map(int,line[x+1].strip().split(",")))
            #On same x level
            if(current[0] == next[0]):
                x = min(current[1], next[1])
                while(x <= max(current[1], next[1])):
                    rocks.add((current[0], x))
                    x+=1 
            #Handling Y-level
            else:
                x = min(current[0], next[0])
                while(x <= max(current[0], next[0])):
                    rocks.add((x, current[1])) 
                    x+=1 
            if(max(current[1], next[1]) > lowest):
                lowest = max(current[1], next[1])
while not abyss:
    settled = 0
    x = 500 
    y = 0
    while not settled:
        #Handling the abyss
        if(y + 1 > lowest):
            settled = 1
            abyss  = 1 
        y+=1 
        
        #In sand or rocks
        if((x, y+1) in rocks or (x, y+1) in sand):
          
            if((x-1, y+1) in rocks or (x-1, y+1) in sand):
                #Obstructed right
                if((x+1, y+1) in rocks or (x+1, y+1) in sand):
                    sand.add((x,y))
                    settled = 1
                else:
                    x+=1
                   
            else:
                x-=1
           
print("Solution 1:", len(sand)) 

#Solution 2
rocks = set()
sand = set()
lowest = 0
floor = 0

with open("day14.txt") as f:
    for line in f:
        line = line.strip().split("->")
        
        for x in range(len(line) - 1):
            current = list(map(int, line[x].strip().split(",")))
            next = list(map(int,line[x+1].strip().split(",")))
            #On same x level
            if(current[0] == next[0]):
                x = min(current[1], next[1])
                while(x <= max(current[1], next[1])):
                    rocks.add((current[0], x))
                    x+=1 
            #Handling Y-level
            else:
                x = min(current[0], next[0])
                while(x <= max(current[0], next[0])):
                    rocks.add((x, current[1])) 
                    x+=1 
            if(max(current[1], next[1]) > lowest):
                lowest = max(current[1], next[1]) 
            
lowest+=2
while not floor:
    settled = 0
    x = 500 
    y = 0
    while not settled:
        if(y + 1 == lowest):
            sand.add((x,y))
            settled = 1
            break 
        if((x,y+1) in rocks or (x, y+1) in sand):
            if((x-1, y+1) in rocks or (x-1, y+1) in sand):
                if((x+1,y+1) in rocks or (x+1, y+1) in sand):
                    sand.add((x,y))
                    settled = 1
                    if(x == 500 and y == 0):
                        floor = 1
                    break 
                else:
                    x+=1
                    y+=1
                    continue
            else:
                x-=1
                y+=1 
                continue 
        y+=1
                        
print("Solution 2", len(sand))
      


