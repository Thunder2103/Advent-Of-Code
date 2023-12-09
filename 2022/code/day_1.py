if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

# Solution to part 1
def taskOne():
    highestCals = 0 
    totalCals = 0
    # Opens file
    with open(getFilePath()) as f: 
        for line in f:          # Get data from every line
            if(line.strip()):
                data = line.strip()
                totalCals += (int(data))    # Sums calories together
            #blank line 
            else:
                if(totalCals > highestCals):
                    highestCals = totalCals
                totalCals = 0
    return highestCals

# Solution to part 2
def taskTwo():
    totalCals = 0 
    highest, second, third = 0,0,0 
    with open(getFilePath()) as f:
        for line in f:
            if(line.strip()):
                data = line.strip()
                totalCals += (int(data)) 
            else:
                # Adjusts top 3 highest calories
                if(highest == 0):
                    highest = totalCals
                elif(totalCals > highest):
                    third = second 
                    second = highest 
                    highest = totalCals
                elif(totalCals > second):
                    third = second
                    second = totalCals 
                elif(totalCals > third):
                    third = totalCals 
                totalCals = 0 
    return (highest + second + third)

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")