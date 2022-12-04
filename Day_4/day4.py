#gets values from line and seperates by space, each word is index, can be used for ints to 
i = 0 
index = 0
index2 = 0 
sum = 0

#Solution 1
with open("day4.txt") as f:
    array = []  
    substring = "-"
    yes = ""
    for line in f: #for each line in f 
            index = 0  
            index2 = 0 
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
print("Solution 1:",sum) 

#Solution 2
sum = 0 
with open("day4.txt") as f:
    for line in f: #for each line in f 
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
print("Solution 2:",sum)

         


