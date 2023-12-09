if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

# Checks if character appears more then once in a string 
def unique_char(string):
    for char in string:
        if(string.count(char) > 1):
            return False
    return True 

# Solution 1
def taskOne():
    with open(getFilePath()) as f:
        for line in f:
            data = line.strip()
            for i in range(len(data)):
                string = data[i:i+4]
                if(unique_char(string)  == False):
                    continue 
                else:
                    return i + 14
                  
# Solution 2
def taskTwo():
    with open(getFilePath()) as f:
        for line in f:
            data = line.strip()
            for i in range(len(data)):
                string = data[i:i+14]
                if(unique_char(string)  == False):
                    continue 
                else:
                    return i + 14
          
print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")