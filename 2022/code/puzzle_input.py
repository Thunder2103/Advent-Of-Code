import os
import inspect

if(__name__ == "__main__"): 
     print("This file should be imported only.")
     exit()

def getFilePath():
     puzzleFile = inspect.stack()[1].filename.split(os.sep)[-1].split(".")[0]
     return os.getcwd() + f"{os.sep}2022{os.sep}puzzle_inputs{os.sep}"+puzzleFile+".txt"