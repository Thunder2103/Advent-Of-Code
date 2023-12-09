from puzzle_input import getFilePath

# Solution 1
def taskOne():
    cycle = 1 
    x = 1
    sum = 0
    with open(getFilePath()) as f:
        input = [] 
        for line in f: # For each line in f
                line = line.strip().split(" ")  
                if(line[0] == "addx"):
                    cycle+=1 
                    if(cycle == 20 or ((cycle / 20) % 2 == 1 and (cycle / 20) <= 11)): sum += (x * cycle)
                    x += int(line[1])
                    cycle+=1
                else: cycle+=1
                if(cycle == 20 or ((cycle / 20) % 2 == 1 and (cycle / 20) <= 11)): sum += (x * cycle)
    return sum      


# Solution two
def taskTwo():
    cycle = 1 
    x = 1
    screen = []
    screen = ["." for i in range(40)]

    with open(getFilePath()) as f:
        input = [] 
        for line in f: # For each line in f
                line = line.strip().split(" ")
                if(abs(x - (cycle-1)) <= 1): screen[(cycle) - 1] = "#"
                if(line[0] == "addx"):
                    cycle+=1  
                    if(abs(x - (cycle-1)) <= 1): screen[(cycle) - 1] = "#"
                    if(cycle == 40):
                        print("".join(screen))
                        screen = ["." for item in screen]
                        cycle = 0
                    x += int(line[1])
                    cycle+=1
                else: cycle+=1
                if(cycle == 40):
                    print("".join(screen))
                    screen = ["." for item in screen]
                    cycle = 0
                

print(taskOne()) 
taskTwo()

            
            




