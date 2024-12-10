if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input(): 
    trailheads = set()  
    top_map_info = {
        "map" : [],
        "bounds": None 
    }
    with open(getFilePath()) as f:   
        for i, line in enumerate(f.readlines()):
            crrnt_lvl = []
            for j, num in enumerate(line.strip()): 
                if num == "0": trailheads.add((j, i)) 
                crrnt_lvl.append(int(num))
            top_map_info["map"].append(crrnt_lvl)
    top_map_info["bounds"] = (0, j, 0, i)
    return (top_map_info, trailheads)


def validate_coords(coords, top_map, visited, bounds): 
    x, y, new_x, new_y = coords
    min_x, max_x, min_y, max_y = bounds
    if((new_x, new_y) in visited): return False 
    if(new_x < min_x or new_x > max_x): return False
    if(new_y < min_y or new_y > max_y): return False 
    if(top_map[new_y][new_x] != top_map[y][x] + 1): return False 
    return True 


def depth_first_search(start_coords, top_map_info, check_visited=True):
    stack, visited = [start_coords], set() 
    top_map = top_map_info["map"]
    bounds = top_map_info["bounds"]
    score = 0 
    
    while(stack != []):
        x, y = stack.pop() 
        if(top_map[y][x] == 9): score += 1
        if(validate_coords((x, y, x - 1, y), top_map, visited, bounds)):
            stack.append((x - 1, y))
        if(validate_coords((x, y, x + 1, y), top_map, visited, bounds)):
            stack.append((x + 1, y))
        if(validate_coords((x, y, x, y - 1), top_map, visited, bounds)):
            stack.append((x, y - 1))
        if(validate_coords((x, y, x, y + 1), top_map, visited, bounds)):
            stack.append((x, y + 1))
        if(check_visited):
            visited.add((x, y)) 
    return score
        
    
def task_one():
    top_map_info, trailheads = parse_input()
    trailhead_scores = 0
    for trailhead in trailheads:
        trailhead_scores += depth_first_search(trailhead, top_map_info)
    return trailhead_scores


def task_two(): 
    top_map_info, trailheads = parse_input()
    trailhead_scores = 0
    for trailhead in trailheads:
        trailhead_scores += depth_first_search(trailhead, top_map_info, False)
    return trailhead_scores


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")