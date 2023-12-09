from puzzle_input import getFilePath

#Dictionary to hold lower case letters and subsequent values
alphabet = {
    "a": 1, 
    "b": 2, 
    "c": 3, 
    "d": 4, 
    "e": 5, 
    "f": 6, 
    "g": 7, 
    "h": 8, 
    "i": 9, 
    "j": 10, 
    "k": 11, 
    "l": 12, 
    "m": 13, 
    "n": 14, 
    "o": 15, 
    "p": 16, 
    "q": 17, 
    "r": 18, 
    "s": 19, 
    "t": 20, 
    "u": 21, 
    "v": 22, 
    "w": 23, 
    "x": 24, 
    "y": 25,
    "z": 26
}

# Solution 1
def taskOne():
    sum = 0
    with open(getFilePath()) as f: 
        # Iterate through each line of the file
        for line in f: 
            # Remove \n
            data = line.strip()
            
            # Get length of line -> split line in half
            halfway = len(data)//2            
            firstHalf = list(data[:halfway])
            secondHalf = list(data[halfway:])
            
            # Place first half and last half of line into seperate sets
            s= {*firstHalf}
            a = {*secondHalf}
            
            # Get the intersect (Shared value) of these sets
            intersect = s.intersection(a)
            interVal = intersect.pop()
            
            # If the value is a capital, add 26 to corresponding lower case in the dictionary 
            if(interVal.isupper()):
                interVal = interVal.lower()
                sum += alphabet[interVal] + 26
            else:
                sum+= alphabet[interVal]

            # Clear sets and lists
            s.clear()
            a.clear()
            firstHalf.clear()
            secondHalf.clear() 
    return sum
 
 # Solution 2
def taskTwo():
    k = 0
    sum = 0
    with open(getFilePath()) as f:  
        # Gets every line in the file, places into a list
        lines = f.readlines() 
        # Iterates until end of the list
        while(k < len(lines)):
            # Remove \n and places in a set
            data = lines[k].strip()  
            a = {*data}
            data = lines[k+1].strip()  
            b = {*data}
            data = lines[k+2].strip()  
            c = {*data}
            # Gets intersect of all three sets
            intersect = a.intersection(b,c)
            interVal = intersect.pop() 
            # If the value is a capital, add 26 to corresponding lower case in the dictionary 
            if(interVal.isupper()):
                interVal = interVal.lower()
                sum += alphabet[interVal] + 26
            else:
                sum+= alphabet[interVal]
            # Clear sets and lists
            a.clear()
            b.clear()
            c.clear()
            k+=3
    return sum

print(taskOne())
print(taskTwo())