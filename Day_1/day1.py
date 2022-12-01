#Solution to part 1
totalCals = 0 
highestCals = 0 

#opens file
with open("day1.txt") as f: 
    for line in f:          #get data from every line
        if(line.strip()):
            data = line.strip()
            totalCals += (int(data))    #sums calories together
        #blank line 
        else:
            if(totalCals > highestCals):
                highestCals = totalCals
            totalCals = 0
print("Largest: ",highestCals) 

#solution to part 2
totalCals = 0 
highest, second, third = 0,0,0 

with open("day1.txt") as f:
    for line in f:
        if(line.strip()):
            data = line.strip()
            totalCals += (int(data)) 
        else:
            #adjusts top 3 highest calories
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
#prints sum of highest three calories
print("Sum of highest three calories: ",highest + second + third)
