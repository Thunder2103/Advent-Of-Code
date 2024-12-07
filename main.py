import os 
import importlib
import random
import re 
import sys

if(__name__ != "__main__"): 
    print("This has nothing to import")
    exit()

DIRPATH = "../Advent-Of-Code"
AOCYEARS = [dir for dir in os.listdir(DIRPATH) if dir.isnumeric()] 


def main():
    print("Weclome to Tom's Advent of Code solutions!")
    n = len(AOCYEARS)
    for index, year in enumerate(AOCYEARS):
        if(index == n - 1): print(f" and {year}", "\n")
        elif(index == 0): print(f"Available years: {year}", end="")
        else: print(f", {year}", end="")
    yearCommands()


def printYearCommands():
    print("Type one of the commands below:")
    for year in AOCYEARS:
        print(f"\t - {year} -> solutions for {year}")  
    print("\t - exit -> Close the program")
    print("\t - help -> Print a list of commands")  
    print("\t - song -> Recommend a song Tom likes")  


def yearCommands():
    printYearCommands()
    while(True):
        commandInput = input("Command: ").replace(" ", "") 
        if(commandInput in AOCYEARS): break
        elif(commandInput == "exit"): exit() 
        elif(commandInput == "song"): recommendSong()
        elif(commandInput == "help"): printYearCommands()
    dayCommands(commandInput)


def getDayCommands(puzzleFiles): 
    dayToCommands = {}
    for file in puzzleFiles:
        dayNum = re.findall("[0-9]{1,2}",file)[0]
        dayCommand = "".join(re.split("day_|\\.py", file))
        if(int(dayNum) not in dayToCommands):
            dayToCommands[int(dayNum)] = [] 
        dayToCommands[int(dayNum)].append(dayCommand) 
    return dayToCommands


def printDayCommands(puzzleFiles):
    dayCommands = getDayCommands(puzzleFiles) 
    print(dayCommands)
    print("\nType one of the commands below:")
    for day in sorted(list(dayCommands.keys())): 
        for command in dayCommands[day]:
            if("CLI" in command): 
                print(f"\t - {command} -> Visualiser for day {day} (Test Data Only)")
            else: print(f"\t - {command} -> Solutions for day {day}")
    
    print("\t - back -> Return to year selection")
    print("\t - exit -> Close the program")
    print("\t - help -> Print a list of commands")


def dayCommands(year):
    puzzleFiles = [file for file in os.listdir(f"{DIRPATH}/{year}/code") 
                   if "day" in file]   
    
    printDayCommands(puzzleFiles)

    while(True):
        commandInput = input("Command: ").replace(" ", "") 
        if(f"day_{commandInput}.py" in puzzleFiles): outputDay(year, f"day_{commandInput}", commandInput)
        elif(commandInput == "back"): yearCommands()
        elif(commandInput == "exit"): exit()
        elif(commandInput == "help"): printDayCommands(puzzleFiles)


def outputDay(year, day, dayNumber):
    print(f"Solutions for Day {dayNumber}:")
    module_name = f"{year}.code.{day}"
    importlib.import_module(module_name)
    del sys.modules[module_name]


def recommendSong():
    song = random.choice(open("songs.txt").read().splitlines())
    print(f"Tom recommends: {song}" )

if(__name__ == "__main__"): main()