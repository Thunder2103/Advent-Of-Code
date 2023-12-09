import os 
import importlib

DIRPATH = "../Advent-Of-Code"

aocYears = [dir for dir in os.listdir(DIRPATH) if dir.isnumeric()] 
yearOutput = ""
n = len(aocYears)
for index, year in enumerate(aocYears):
    if(index == n - 1): yearOutput += " and " + year
    elif(index == 0): yearOutput += year
    else: yearOutput += ", " + year


#puzzleFiles = [file for file in os.listdir(f"{DIRPATH}/{aocYears[0]}/code") if file.endswith(".py") and file != "puzzle_input.py"] 






