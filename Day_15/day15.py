#This one might take a while, so grab a coffee or something
#A friend helped with part because I was very stuck
import re

#Solution 1
beacons = set()
sensors = []
nobeacons = set() 
y = 2000000

with open("day15.txt") as f:
    for line in f:
        line = re.split("=|:|,", line.strip())

        xOrd = int(line[1])
        yOrd = int(line[3])  
        bx = int(line[5])
        by = int(line[-1])   

        manDist = abs(xOrd - bx) + abs(yOrd - by)  
        sensors.append([(xOrd, yOrd), manDist])
        
        if(by == y):
            beacons.add((bx, by)) 

i = 0
while(i < len(sensors)):
    manDist = sensors[i][1]
    xCord = sensors[i][0][0]
    yCord = sensors[i][0][1]
    if(yCord + manDist < y):
        i+=1 
        continue
    elif(yCord - manDist > y):
        i+=1
        continue
    else:
        if(yCord < y):
            for c in range(manDist - (y - yCord) + 1):
                if((xCord + c, y) not in beacons):
                    nobeacons.add((xCord + c, y)) 
                if((xCord - c, y) not in beacons):
                    nobeacons.add((xCord - c, y))
        elif(yCord > y):
            for c in range(manDist + (y - yCord) + 1):
                if((xCord + c, y) not in beacons):
                    nobeacons.add((xCord + c, y)) 
                if((xCord - c, y) not in beacons):
                    nobeacons.add((xCord - c, y))
        else:
            for c in range(manDist + 1):
                if((xCord + c, y) not in beacons):
                    nobeacons.add((xCord + c, y)) 
                if((xCord - c, y) not in beacons):
                    nobeacons.add((xCord - c, y))
    i+=1

print(len(nobeacons))
sensors.clear()

#Solution 2

with open("day15.txt") as f:
    for line in f:
        line = re.split("=|:|,", line.strip())

        xOrd = int(line[1])
        yOrd = int(line[3])  
        bx = int(line[5])
        by = int(line[-1])   

        manDist = abs(xOrd - bx) + abs(yOrd - by)  
        sensors.append([[xOrd, yOrd], manDist])
    
y  = 0
while(y <= 4000000):
    x = 0 
    while(x <= 4000000):
        beacon = True
        for sensor in sensors:
            print(x)
            if(abs(sensor[0][0] - x) + abs(sensor[0][1] - y) <= sensor[1]):
                x = sensor[0][0] + (sensor[1] - abs(sensor[0][1] - y))
                beacon = False
                break
        if(beacon):
            print(x*4000000 + y)
            exit()
        x+=1
    y+=1








