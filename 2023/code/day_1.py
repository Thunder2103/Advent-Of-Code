import re
if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

def taskOne():
    with open(getFilePath()) as file:
        total = 0
        for line in file:
            total += mergeDigits(re.findall("[0-9]", line))
    return total 


def mergeDigits(nums):
    if(len(nums) > 1):
        return int(nums[0] + nums[-1])
    else:
        return int(nums[0] + nums[0])

def taskTwo():
    digits = {
        "one": "one1one", 
        "two": "two2two", 
        "three": "three3three", 
        "four": "four4four", 
        "five": "five5five", 
        "six": "six6six", 
        "seven": "seven7seven", 
        "eight": "eight8eight", 
        "nine": "nine9nine", 
        "zero": "zero0zero"
    }

    with open(getFilePath()) as file:
        total = 0
        for line in file:
            for digit, numeric in digits.items():
                line = line.replace(digit, numeric)
            total += mergeDigits(re.findall("[0-9]", line))
        return total 
print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")