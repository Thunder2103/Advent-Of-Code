from puzzle_input import getFilePath
import re

def parse(line):
    lst = []
    nums =  re.sub("^Card\s\d:\s", "", line).rstrip().split("|")
    for section in nums:
        section = re.sub("^[\s]+|[\s]+$", "", section).split(" ") 
        lst.append(set([i for i in section if i != ""]))
    return lst

def taskOne():
    total = 0
    with open(getFilePath()) as file:
        for line in file:
            numbers = parse(line)
            matches = len(numbers[0].intersection(numbers[1]))
            if(matches): total += 2 ** (matches - 1) 
    return total

def taskTwo():
    total = 0
    matches = {}
    scratchCards = {}
    with open(getFilePath()) as file:
        for index, line in enumerate(file):
            numbers = parse(line)
            matches[index] = len(numbers[0].intersection(numbers[1]))
            scratchCards[index] = 1
        for key, value in matches.items():
            for i in range(1, value + 1):
                scratchCards[key + i] += scratchCards[key]
            total += scratchCards[key]
        return total    
print(taskOne())
print(taskTwo())