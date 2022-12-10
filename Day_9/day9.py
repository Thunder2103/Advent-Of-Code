#Is this inefficient? Yes
#Does it work? Somehow
#Did I spend too much time on this? For sure 

snake = [[0,0] for i in range(2)]
nodesVisited = [[0,0]]
visited = 1
with open("day9.txt") as f:
    input = [] 
    for line in f: #for each line in f
            line = line.strip().split(" ") 
            if(line[0] == "R"):
                for x in range(0, int(line[1])):
                    snake[0][0] += 1
                    if(snake[0][0] - snake[1][0] == 2): 
                        if(snake[0][1] != snake[1][1]):
                            snake[1][1] = snake[0][1]
                        snake[1][0]+=1  
                
                        if(snake[1] not in nodesVisited):
                            visited+=1
                            nodesVisited.append([snake[1][0],snake[1][1]])
        
            elif(line[0] == "L"):
                for x in range(0, int(line[1])):
                    snake[0][0] -= 1 
                    if(snake[1][0] - snake[0][0] == 2):
                        if(snake[1][1] != snake[0][1]):
                            snake[1][1] = snake[0][1]
                        snake[1][0]-=1  
                    
                        if(snake[1] not in nodesVisited):
                            visited+=1
                            nodesVisited.append([snake[1][0],snake[1][1]])
        
            elif(line[0] == "U"):
                for y in range(0, int(line[1])):
                    snake[0][1] += 1
                
                    if(snake[0][1] - snake[1][1] == 2):
                        if(snake[0][0] != snake[1][0]):
                            snake[1][0] = snake[0][0]
                        snake[1][1] = snake[0][1]-1 
                 
                    if(snake[1] not in nodesVisited):
                            visited+=1
                            nodesVisited.append([snake[1][0],snake[1][1]]) 
    
            elif(line[0] == "D"):
                for y in range(0, int(line[1])):
                    snake[0][1] -= 1 
                    if(snake[1][1] - snake[0][1] == 2):
                        if(snake[0][0] != snake[1][0]):
                            snake[1][0] = snake[0][0]
                        snake[1][1] = snake[0][1]+1 
                    
                        if(snake[1] not in nodesVisited):
                            visited+=1
                            nodesVisited.append([snake[1][0],snake[1][1]]) 
                        
print("Solution 1", visited)             

snake = [[0,0] for i in range(10)]
position = [0,0]

nodesVisited = [[0,0]]
visited = 1

# solution 2
with open("day9.txt") as f:
    input = [] 
    for line in f: #for each line in f
            line = line.strip().split(" ")
            for x in range(int(line[1])):
                current = snake[0]
                if(line[0] == "R"):
                    snake[0][0] += 1
                
                if(line[0] == "L"): 
                    snake[0][0] -=1
                
                if(line[0] == "U"): 
                    snake[0][1] +=1
                   
                if(line[0] == "D"):
                    snake[0][1] -= 1 

                for a in range(1, len(snake)):
                    if(snake[a-1][0] - snake[a][0] >= 2):
                        snake[a][0] +=1 
                        if(snake[a-1][1] - snake[a][1] == 2):
                            snake[a][1] +=1
                        elif(snake[a][1] - snake[a-1][1] >= 2):
                                snake[a][1]-=1  
                        elif(snake[a][1] != snake[a-1][1]):
                            snake[a][1] = snake[a-1][1]
                    
                    elif(snake[a][0] - snake[a-1][0] >= 2):
                            snake[a][0] -=1 
                            if(snake[a-1][1] - snake[a][1] == 2):
                                snake[a][1]+=1 
                            elif(snake[a][1] - snake[a-1][1] >= 2):
                                snake[a][1]-=1  
                            elif(snake[a][1] != snake[a-1][1]):
                                snake[a][1] = snake[a-1][1]

                    elif(snake[a-1][1] - snake[a][1] >=2): 
                            snake[a][1] +=1
                            if(snake[a-1][0] - snake[a][0] >= 2):
                                snake[a][0]+=1  
                            elif(snake[a][0] - snake[a-1][0] >= 2):
                                snake[a][0]-=1 
                            elif(snake[a][0] != snake[a-1][0]):
                                snake[a][0] = snake[a-1][0]
                          
                    elif(snake[a][1] - snake[a-1][1] >=2): 
                            snake[a][1] -=1  
                            if(snake[a-1][0] - snake[a][0] >= 2):
                                snake[a][0] +=1
                            elif(snake[a][0] - snake[a-1][0] >= 2):
                                snake[a][0]-=1  
                            elif(snake[a][0] != snake[a-1][0]):
                                snake[a][0] = snake[a-1][0] 
                    
                if(snake[9] not in nodesVisited):
                    visited+=1
                    nodesVisited.append([snake[9][0], snake[9][1]]) 

print("Solution 2", visited) 


      
               
            
                    
  
       
        