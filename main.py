import os 
import importlib
import random

DIRPATH = "../Advent-Of-Code"

if(__name__ != "__main__"): 
    print("This has nothing to import")
    exit()


AOCYEARS = [dir for dir in os.listdir(DIRPATH) if dir.isnumeric()] 
def intro():
    print("Weclome to Tom's Advent of Code solutions!")
    n = len(AOCYEARS)
    for index, year in enumerate(AOCYEARS):
        if(index == n - 1): print(f" and {year}", "\n")
        elif(index == 0): print(f"Available years: {year}", end="")
        else: print(f", {year}", end="")
    yearCommands()

def yearCommands():
    print("Type one of the commands below:")
    for year in AOCYEARS:
        print(f"\t - {year} -> solutions for {year}")
    print("\t - song -> Recommend a song Tom likes")    
    print("\t - exit -> close the program")
    
    while(True):
        commandInput = input("Command: ") 
        if(commandInput in AOCYEARS): break
        elif(commandInput == "exit"): exit() 
        elif(commandInput == "song"): recommendSong()
    dayCommands(commandInput)

def dayCommands(year):
    puzzleFiles = [file for file in os.listdir(f"{DIRPATH}/{year}/code") if file.endswith(".py") and file != "puzzle_input.py" and file != "__init__.py"] 
    print("\nType one of the commands below:")
    for i, _ in enumerate(puzzleFiles):
        print(f"\t - {i+1} -> Solutions for day {i+1}")
    print("\t - back -> return to year selection")
    print("\t - exit -> close the program")

    while(True):
        commandInput = input("Command: ")
        if(f"day_{commandInput}.py" in puzzleFiles): outputDay(year, f"day_{commandInput}", commandInput)
        elif(commandInput == "back"): yearCommands()
        elif(commandInput == "exit"): exit()

def outputDay(year, day, dayNumber):
    print(f"Solutions for Day {dayNumber}:")
    day = importlib.import_module(f"{year}.code.{day}")

def recommendSong():
    song = random.choice(open("songs.txt").read().splitlines())
    print(f"Tom recommends: {song}" )
intro()