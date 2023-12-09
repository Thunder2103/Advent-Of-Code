from puzzle_input import getFilePath

# Solution one
def taskOne():

    # Gets values from line and seperates by space, each word is index, can be used for ints to 
    i = 0 
    index = 0
    sum = 0
    with open(getFilePath()) as f:
        for line in f: # For each line in f 
                index = 0  
                i = 0
                data = line.strip().split(",")
                string = str(data[0])
                while(string[i] != "-"):
                    index+=1 
                    i+=1
                i = 0  
                firstRangeL = int(string[:index])
                firstRangeH = int(string[index+1:])
                string = str(data[1]) 
                index = 0
                while(string[i] != "-"):
                    index+=1
                    i+=1  
                secondRangeL = int(string[:index])
                secondRangeH = int(string[index+1:])  
                if(firstRangeL >= secondRangeL and firstRangeH <= secondRangeH):
                    sum +=1 
                elif(secondRangeL >= firstRangeL and secondRangeH <= firstRangeH):
                    sum+=1
    return sum

# Solution 2
def taskTwo():
    # Gets values from line and seperates by space, each word is index, can be used for ints to 
    i = 0 
    index = 0
    sum = 0 
    with open(getFilePath()) as f:
        for line in f: # For each line in f 
            index = 0  
            i = 0
            data = line.strip().split(",")
            string = str(data[0])
            while(string[i] != "-"):
                index+=1 
                i+=1
            i = 0  
            firstRangeL = int(string[:index])
            firstRangeH = int(string[index+1:])
            index = 0
            string = str(data[1])
            while(string[i] != "-"):
                index+=1
                i+=1  
            secondRangeL = int(string[:index])
            secondRangeH = int(string[index+1:])  
            if(firstRangeL >= secondRangeL and firstRangeH <= secondRangeH):
                sum +=1 
            elif(secondRangeL >= firstRangeL and secondRangeH <= firstRangeH):
                sum+=1
            elif(firstRangeH - secondRangeL >=0 and firstRangeH - secondRangeH <= 0):
                sum+=1
            elif(secondRangeH - firstRangeL >=0 and secondRangeH - firstRangeH <=0):
                sum+=1
    return sum
  
print(taskOne())
print(taskTwo())

