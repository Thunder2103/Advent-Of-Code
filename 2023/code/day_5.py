from puzzle_input import getFilePath
import re

def parseSeeds(line):
    return re.sub("[a-zA-Z]+[:]+[\s]", "", line).split(" ") 

def parse(filePtr):
    spaceCount = 0
    numLst = []
    while(spaceCount < 1):
        line = filePtr.readline()
        if(line == "\n" or line == ""): spaceCount += 1
        if(re.match("[0-9]", line)):
            nums = line.rstrip().split(" ")
            numLst.append([int(nums[1]), int(nums[1]) + int(nums[2]) - 1, int(nums[0]) - int(nums[1])]) 
    return sorted(numLst)

def binSearch(lst, val):
    low = 0 
    high = len(lst) - 1
    while(low <= high): 
        mid = (low + high) // 2
        if(val < lst[mid][0]): 
            high = mid - 1
        elif(val > lst[mid][1]):
            low = mid + 1  
        else: return mid 
    return -1

def mapVals(lst, mappedVal):
    index = binSearch(lst, mappedVal)
    if (index != -1): 
            return mappedVal + lst[index][2] 
    return mappedVal

def taskOne():
    with open(getFilePath()) as file: 
        seeds = parseSeeds(file.readline().rstrip()) 
        file.readline()
        seedsToSoil = parse(file)    
        soilToFertilizer = parse(file)
        fertToWater = parse(file)
        waterToLight = parse(file)
        lightToTemp = parse(file)
        tempToHumid = parse(file)
        humidToLoc = parse(file)
        
        lowestLocation = None 
        for seed in seeds:
            mappedVal = int(seed)
            mappedVal = mapVals(seedsToSoil, mappedVal)
            mappedVal = mapVals(soilToFertilizer, mappedVal) 
            mappedVal = mapVals(fertToWater, mappedVal) 
            mappedVal = mapVals(waterToLight, mappedVal)  
            mappedVal = mapVals(lightToTemp, mappedVal)  
            mappedVal = mapVals(tempToHumid, mappedVal) 
            mappedVal = mapVals(humidToLoc, mappedVal) 
            if(lowestLocation == None or mappedVal < lowestLocation):  lowestLocation = mappedVal
        return lowestLocation

def parseSeedRanges(line):
    seeds = []
    nums = re.sub("[a-zA-Z]+[:]+[\s]", "", line).split(" ") 
    for i in range(0, len(nums) - 1, 2):
        seeds.append([int(nums[i]), int(nums[i]) + int(nums[i + 1]) - 1]) 
    return sorted(seeds)

def splitRanges(splitLst, checkLst):
    i = 0 
    while(i < len(splitLst)):
        for j in range(0, len(checkLst)):
            if(splitLst[i][0] > checkLst[j][1]): continue
            if(splitLst[i][1] < checkLst[j][0]): continue
            if(splitLst[i][0] >= checkLst[j][0] and splitLst[i][1] > checkLst[j][1]): 
                splitLst.append([checkLst[j][1] + 1, splitLst[i][1]])
                splitLst[i][1] = checkLst[j][1]
            elif(splitLst[i][0] < checkLst[j][0] and splitLst[i][1] <= checkLst[j][1]):
                splitLst.append([splitLst[i][0], checkLst[j][0] - 1])
                splitLst[i][0] = checkLst[j][0]
            splitLst[i][0] += checkLst[j][2]
            splitLst[i][1] += checkLst[j][2] 
            break 
        i+=1
    return splitLst

def taskTwo():
      with open(getFilePath()) as file: 
        seeds = parseSeedRanges(file.readline().rstrip()) 
        file.readline()
        seedsToSoil = parse(file)    
        soilToFertilizer = parse(file)
        fertToWater = parse(file)
        waterToLight = parse(file)
        lightToTemp = parse(file)
        tempToHumid = parse(file)
        humidToLoc = parse(file)   

        mappedVal = splitRanges(seeds, seedsToSoil)
        mappedVal = splitRanges(mappedVal, soilToFertilizer)
        mappedVal = splitRanges(mappedVal, fertToWater)   
        mappedVal = splitRanges(mappedVal, waterToLight)
        mappedVal = splitRanges(mappedVal, lightToTemp)
        mappedVal = splitRanges(mappedVal, tempToHumid)
        mappedVal = splitRanges(mappedVal, humidToLoc)
        mappedVal.sort()
        return mappedVal[0][0]
print(taskOne())  
print(taskTwo())