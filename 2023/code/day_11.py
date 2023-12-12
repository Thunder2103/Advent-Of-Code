if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

def taskOne():
    galaxies = []
    emptyRows = []
    with open(getFilePath()) as file:
        columnsGalaxyCount = [0 for _ in range(len(file.readline().rstrip()))]
        file.seek(0)
        for i, line in enumerate(file):
            galaxyCount = 0
            for j, char in enumerate(line.rstrip()):
                if(char == "#"): 
                    galaxyCount += 1
                    galaxies.append([i, j]) 
                    columnsGalaxyCount[j] += 1
            if(galaxyCount == 0): emptyRows.append(i) 
    emptyColumns = [index for index, i in enumerate(columnsGalaxyCount) if i == 0]
    for galaxy in galaxies:
        rowIncrease = 0
        columnIncrease = 0
        for column in emptyColumns:
            if(galaxy[1] > column): columnIncrease += 1
        for row in emptyRows: 
            if(galaxy[0] > row): rowIncrease += 1
        galaxy[0] += rowIncrease
        galaxy[1] += columnIncrease 
    total = 0
    n = len(galaxies)
    for i in range(n):
        for j in range(i + 1, n):
            total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) 
    return total

def taskTwo():
    galaxies = []
    emptyRows = []
    with open(getFilePath()) as file:
        columnsGalaxyCount = [0 for _ in range(len(file.readline().rstrip()))]
        file.seek(0)
        for i, line in enumerate(file):
            galaxyCount = 0
            for j, char in enumerate(line.rstrip()):
                if(char == "#"): 
                    galaxyCount += 1
                    galaxies.append([i, j]) 
                    columnsGalaxyCount[j] += 1
            if(galaxyCount == 0): emptyRows.append(i) 
    emptyColumns = [index for index, i in enumerate(columnsGalaxyCount) if i == 0]
    for galaxy in galaxies:
        rowIncrease = 0
        columnIncrease = 0
        for column in emptyColumns:
            if(galaxy[1] > column): columnIncrease += 999999
        for row in emptyRows: 
            if(galaxy[0] > row): rowIncrease += 999999
        galaxy[0] += rowIncrease
        galaxy[1] += columnIncrease 
    total = 0
    n = len(galaxies)
    for i in range(n):
        for j in range(i + 1, n):
            total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) 
    return total 

print(taskOne())
print(taskTwo())