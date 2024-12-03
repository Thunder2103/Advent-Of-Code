import re

if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input(task):  
    instructions = [] 
    # Regex for part one
    exp = "mul\\([0-9]+,[0-9]+\\)"
    if(task == 2): 
        # Regex for part two
        exp += "|don't\\(\\)|do\\(\\)"
    # Find occurences of regex in each line
    with open(getFilePath()) as f:
        for line in f.readlines(): 
            instructions.append(re.findall(exp, line.strip())) 
    # Flatten 2D array into 1D and return
    return [j for i in instructions for j in i]
     

def taskOne(): 
    # Valid mul instructions
    valid_instructions = parse_input(1)
    total = 0
    for instruction in valid_instructions: 
        # Extract numbers
        x, y = re.findall("[0-9]*,[0-9]*", instruction)[0].split(",") 
        total += int(x) * int(y)
    return total


def taskTwo():
    # Valid mul, do, don't instructions
    valid_instructions = parse_input(2)
    ignore = False  
    total = 0 
    for instruction in valid_instructions: 
        # Split into instructions and param e.g "mul", "1, 2)"
        instruction, param = instruction.split("(")
        if(instruction == "do"): ignore = False
        if(instruction == "don't"): ignore = True 
        elif(instruction == "mul" and not ignore):
            # Extract Numbers
            x, y = re.findall("[0-9]*,[0-9]*", param)[0].split(",")
            total += int(x) * int(y) 
    return total


print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")