import os
import inspect

if(__name__ == "__main__"): 
     print("This file should be imported only.")
     exit()

def getFilePath():
     puzzleFile = inspect.stack()[1].filename.split("\\")[-1].split(".")[0]
 
     return os.getcwd() + "/2022/puzzle_inputs/"+puzzleFile+".txt"