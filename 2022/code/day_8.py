if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

viewDistance = 0
# Functions
def check_right(trees, i, j): 
    global viewDistance
    for x in range(j+1, len(trees[i])): 
        if(trees[i][j] <= trees[i][x]):
            viewDistance+=1 
            return 0
        viewDistance+=1
    return 1 

def check_left(trees, i, j):
    global viewDistance
    for x in range(j-1, -1, -1):
        if(trees[i][j] <= trees[i][x]):
            viewDistance+=1
            return 0
        viewDistance+=1
    return 1 

def check_column_down(trees, i, j):
    global viewDistance
    for x in range(i+1, len(trees)):
        if(trees[i][j] <= trees[x][j]):
            viewDistance+=1
            return 0 
        viewDistance+=1
    return 1

def check_column_up(trees, i, j): 
    global viewDistance
    for x in range(i-1, -1, -1):
        if(trees[i][j] <= trees[x][j]):
            viewDistance+=1
            return 0 
        viewDistance+=1
    return 1

visible = 0 
with open(getFilePath()) as f:
    trees = [] 
    for line in f:
        data = line.strip()
        trees.append(list(data)) 

    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if(j == 0 or i == 0 or i == len(trees)-1 or j == len(trees[i]) -1): 
                visible+=1
            else: 
                if(check_right(trees, i, j) == 1): 
                    visible+=1  
                    continue
                elif(check_left(trees, i, j) == 1):
                    visible+=1
                    continue 
                elif(check_column_down(trees,i,j) == 1):  
                    visible+=1 
                    continue 
                elif(check_column_up(trees, i, j) == 1):
                    visible+=1
                    continue 
    score = 0 
    viewDistance = 0 
    tmp = 1
    
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            check_right(trees, i,j)
            tmp*= viewDistance
            viewDistance = 0
            
            check_left(trees, i, j)
            tmp *= viewDistance
            viewDistance = 0  
    
            check_column_down(trees, i, j)
            tmp*=viewDistance 
            viewDistance = 0 
            
            check_column_up(trees, i, j)
            tmp*=viewDistance
            viewDistance = 0
            
            if(tmp > score):
                score = tmp 
            tmp = 1 


def taskOne():
    return visible
def taskTwo():
    return score

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")