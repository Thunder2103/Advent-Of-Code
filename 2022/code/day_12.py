# Not so elegant Dijkstra's shortest path
# 9000 was chosen to represent infinity since it's large enough to work
# And it's over 9000

if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath
class Node:
    def __init__(self, numVal, charVal, weight):
        self.numVal = numVal
        self.charVal = charVal
        self.distance = weight
        self.next = []
        self.visited = 0
        pass

def neighboursTaskOne(graph, node, x, y):
    
    if(y == 0):
        if(graph[x][y+1].numVal <= node.numVal + 1):
            node.next.append(graph[x][y+1]) 
    elif(y == len(graph[x]) - 1):
        if(graph[x][y-1].numVal <= node.numVal + 1):
            node.next.append(graph[x][y-1]) 
    else: 
        if(graph[x][y-1].numVal <= node.numVal + 1):
            node.next.append(graph[x][y-1])
        if(graph[x][y+1].numVal <= node.numVal + 1):
            node.next.append(graph[x][y+1]) 

    if(x == 0):
        if(graph[x+1][y].numVal <= node.numVal + 1):
            node.next.append(graph[x+1][y])  
    elif(x == len(graph) - 1):
        if(graph[x-1][y].numVal <= node.numVal + 1):
            node.next.append(graph[x-1][y])   
    else:
        if(graph[x+1][y].numVal <= node.numVal + 1):
            node.next.append(graph[x+1][y]) 
        if(graph[x-1][y].numVal <= node.numVal + 1):
            node.next.append(graph[x-1][y])   

def taskOne(destination):  
    graph = []
    with open(getFilePath()) as f: 
        for line in f:
            graph.append(list(line.strip()))
    Q = []
    for a in range(len(graph)):
        for b in range(len(graph[a])):
            if(graph[a][b] == destination):
                graph[a][b] = (Node(97,graph[a][b],0)) 
                Q.append(graph[a][b])
            elif(graph[a][b] == "E"):
                graph[a][b] = (Node(122,graph[a][b], 9000)) 
                Q.append(graph[a][b])
            else:
                graph[a][b] = (Node(ord(graph[a][b]), graph[a][b], 9000))
                Q.append(graph[a][b])
                
    for a in range(len(graph)):
        for b in range(len(graph[a])):
            neighboursTaskOne(graph, graph[a][b], a, b)
    
    while(Q): 
        min = 9001
        for a in range(len(Q)):
            if(Q[a].distance < min):
                min = Q[a].distance
                visiting = Q[a] 
                remove = a
        for b in range(len(visiting.next)): 
            if(visiting.visited == 1): continue
            tmpDist = visiting.distance + 1
            if(tmpDist < visiting.next[b].distance):
                visiting.next[b].distance = tmpDist
        Q.pop(remove)
        visiting.visited = 1
        if(visiting.charVal == "E"):
            return visiting.distance

def neighboursTaskTwo(graph, node, x, y):
    if(y == 0):
        if(graph[x][y+1].numVal >= node.numVal - 1):
            node.next.append(graph[x][y+1]) 
    elif(y == len(graph[x]) - 1):
        if(graph[x][y-1].numVal >= node.numVal - 1):
            node.next.append(graph[x][y-1]) 
    else: 
        if(graph[x][y-1].numVal >= node.numVal - 1):
            node.next.append(graph[x][y-1])
        if(graph[x][y+1].numVal >= node.numVal - 1):
            node.next.append(graph[x][y+1]) 

    if(x == 0):
        if(graph[x+1][y].numVal >= node.numVal - 1):
            node.next.append(graph[x+1][y])  
    elif(x == len(graph) - 1):
        if(graph[x-1][y].numVal >= node.numVal - 1):
            node.next.append(graph[x-1][y])   
    else:
        if(graph[x+1][y].numVal >= node.numVal - 1):
            node.next.append(graph[x+1][y])  
        if(graph[x-1][y].numVal >= node.numVal - 1):
            node.next.append(graph[x-1][y])   

    
def taskTwo(destination):
    graph = []
    with open(getFilePath()) as f: 
        for line in f:
            graph.append(list(line.strip()))  
    Q = []
    for a in range(len(graph)):
        for b in range(len(graph[a])):
            if(graph[a][b] == destination):
                graph[a][b] = (Node(122,graph[a][b],0)) 
                Q.append(graph[a][b])
            elif(graph[a][b] == "S"):
                graph[a][b] = (Node(97,graph[a][b], 9000)) 
                Q.append(graph[a][b])
            else:
                graph[a][b] = (Node(ord(graph[a][b]), graph[a][b], 9000))
                Q.append(graph[a][b])
                
    for a in range(len(graph)):
        for b in range(len(graph[a])):
            neighboursTaskTwo(graph, graph[a][b], a, b)
    
    lowest = 9000
    while(Q): 
        min = 9001
        for a in range(len(Q)):
            if(Q[a].distance < min):
                min = Q[a].distance
                visiting = Q[a] 
                remove = a
        for b in range(len(visiting.next)): 
            if(visiting.visited == 1): continue
            tmpDist = visiting.distance + 1
            if(tmpDist < visiting.next[b].distance):
                visiting.next[b].distance = tmpDist
        Q.pop(remove)
        visiting.visited = 1
        if(visiting.charVal == "a" and visiting.distance < lowest):
            lowest = visiting.distance
    return lowest

print(f"Part 1: {taskOne('S')}")
print(f"Part 2: {taskTwo('E')}")