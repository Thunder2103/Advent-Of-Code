import re
import math 
if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
        
def createNetwork(file):
    nodeDict =  {}
    startDict = {}
    for line in file:
        if(line != "\n"):
            nodes = re.sub("\s=|[(),]", "", line.rstrip()).split(" ")
            if(nodes[0] not in nodeDict):
                nodeDict[nodes[0]] = Node(nodes[0])
                if(nodes[0][-1] == "A" and nodes[0] not in startDict):
                    startDict[nodes[0]] = nodeDict[nodes[0]]
            if(nodes[1] not in nodeDict): nodeDict[nodes[1]] = Node(nodes[1])
            if(nodes[2] not in nodeDict): nodeDict[nodes[2]] = Node(nodes[2])
            nodeDict[nodes[0]].left = nodeDict[nodes[1]]
            nodeDict[nodes[0]].right = nodeDict[nodes[2]]
    return startDict

def traverse(instructions, startNode):
    currentNode = startNode
    i = 0
    n = len(instructions)
    steps = 0
    while(True):
        if(currentNode.val[-1] == "Z"): break
        if(currentNode.left.val == currentNode.val and currentNode.right.val == currentNode.val): break 
        if(instructions[i] == "R"): currentNode = currentNode.right
        if(instructions[i] == "L"): currentNode = currentNode.left
        if(i == n - 1): i = 0
        else: i += 1
        steps += 1
    return steps

def taskOne():
    with open(getFilePath()) as file:
        instructions = [*file.readline().rstrip()]
        startNode = createNetwork(file)
    return traverse(instructions, startNode["AAA"])

def taskTwo():
    nearestEnd = []
    with open(getFilePath()) as file:
        instructions = [*file.readline().rstrip()]
        nodes = createNetwork(file)
        for _, node in nodes.items(): nearestEnd.append(traverse(instructions, node))
    lcm = 1 
    for num in nearestEnd:
        lcm = math.lcm(lcm, num)
    return lcm

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")