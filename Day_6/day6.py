#Checks if character appears more then once in a string 
def unique_char(string):
    for char in string:
        if(string.count(char) > 1):
            return False
    return True 

#solution 1
with open("day6.txt") as f:
    myArray = [] 
    for line in f:
        data = line.strip()
        for i in range(len(data)):
            string = data[i:i+4]
            if(unique_char(string)  == False):
                continue 
            else:
                print("Solution 1:",i+4, string) 
                break
            
#solution 2
with open("day6.txt") as f:
    myArray = [] 
    for line in f:
        data = line.strip()
        for i in range(len(data)):
            string = data[i:i+14]
            if(unique_char(string)  == False):
                continue 
            else:
                print("Solution 2",i+14, string) 
                break
          
         
            




                
        