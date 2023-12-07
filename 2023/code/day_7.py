from puzzle_input import getFilePath

TYPES = 7
SIZEOFHAND = 5

def parse(line):
    return line.rstrip().split(" ")

def insertList(hand, handLst, jokers):
    pokercards = {
        "A": 12, 
        "K": 11, 
        "Q": 10, 
        "J": -1 if jokers else 9, 
        "T": 8, 
        "9": 7,
        "8": 6, 
        "7": 5, 
        "6": 4, 
        "5": 3, 
        "4": 2, 
        "3": 1, 
        "2" : 0, 
    }
    for index, sortedHand in enumerate(handLst):
        for i in range(SIZEOFHAND):
            if(pokercards[hand[i]] < pokercards[sortedHand[0][i]]): return index
            if(pokercards[hand[i]] > pokercards[sortedHand[0][i]]): break
    return len(handLst)

def calculateTotal(handStrengths):
    total = 0
    counter = 1
    for level in handStrengths:
        for hand in level:
            total += int(hand[1]) * counter
            counter += 1
    return total

def taskOne():
    with open(getFilePath()) as file:
        handStrengths = [[] for _ in range(TYPES)]
        hands = [parse(line) for line in file]
   
    for hand in hands:
        charOccurence = {}
        for char in hand[0]:
            if(char not in charOccurence):
                charOccurence[char] = 1
            else:
                charOccurence[char] += 1
        
        pairs = 0
        largestOccurence = 0
        for char, occurence in charOccurence.items():
            if(occurence == 2): pairs += 1
            if(occurence > largestOccurence): largestOccurence = occurence  
        if(largestOccurence <= 2):
            handStrengths[pairs].insert(insertList(hand[0], handStrengths[pairs], False), hand)
        elif(largestOccurence == 3):
            handStrengths[largestOccurence + pairs].insert(insertList(hand[0], handStrengths[largestOccurence + pairs], False), hand)
        else:
            handStrengths[largestOccurence + 1].insert(insertList(hand[0], handStrengths[largestOccurence + 1], False), hand)
    return calculateTotal(handStrengths)

def taskTwo():
    with open(getFilePath()) as file:
        handStrengths = [[] for _ in range(TYPES)]
        hands = [parse(line) for line in file]
   
    for hand in hands:
        charOccurence = {}
        jokers = 0
        for char in hand[0]:
            if(char == "J"): jokers+=1
            elif(char not in charOccurence):
                charOccurence[char] = 1
            else:
                charOccurence[char] += 1 
         
        pairs = 0
        largestOccurence = 0
        for char, occurence in charOccurence.items():
            if(occurence == 2): pairs += 1
            if(occurence > largestOccurence): largestOccurence = occurence      
        if(jokers == 1 and largestOccurence == 1):
            pairs = 1
        elif(jokers == 1 and largestOccurence == 2 and pairs > 0):
            pairs -= 1
        
        largestOccurence += jokers
        if(largestOccurence <= 2):
            handStrengths[pairs].insert(insertList(hand[0], handStrengths[pairs], True), hand)
        elif(largestOccurence == 3):
            handStrengths[largestOccurence + pairs].insert(insertList(hand[0], handStrengths[largestOccurence + pairs], True), hand)
        else:
            handStrengths[largestOccurence + 1].insert(insertList(hand[0], handStrengths[largestOccurence + 1], True), hand)    
    return calculateTotal(handStrengths)

print(taskOne())
print(taskTwo())  