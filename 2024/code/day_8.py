if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

def parse_input():  
    antenna_coords = {}
    boundaries = {}
    boundaries["min_x"] = 0
    boundaries["min_y"] = 0
    with open(getFilePath()) as f:    
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                if char == ".": continue
                if char not in antenna_coords:
                    antenna_coords[char] = [(j, i)]
                else: antenna_coords[char].append((j, i)) 
        boundaries["max_x"] = len(line) - 1
        boundaries["max_y"] = j 
    return (list(antenna_coords.values()), boundaries)


def validate_antinode(antinode, boundaries):
    x, y = antinode
    if(x < boundaries["min_x"] or x > boundaries["max_x"]):
        return False
    if(y < boundaries["min_y"] or y > boundaries["max_y"]):
        return False 
    return True

    
def task_one():
    antenna_coords, boundaries = parse_input() 
    antinodes = set()
    for coords in antenna_coords:
        for i, main_antenna in enumerate(coords):
            for check_antenna in coords[i + 1:]: 
                antenna_dist = tuple(x - y for x, y in zip(main_antenna, check_antenna)) 
                antinode = tuple(x + y for x, y in zip(main_antenna, antenna_dist))  
                if(validate_antinode(antinode, boundaries)):
                    antinodes.add(antinode)
                antinode = tuple(x + -y for x, y in zip(check_antenna, antenna_dist)) 
                if(validate_antinode(antinode, boundaries)):
                    antinodes.add(antinode) 
    return len(antinodes)


def task_two(): 
    antenna_coords, boundaries = parse_input() 
    antinodes = set()
    for coords in antenna_coords: 
        for i, main_antenna in enumerate(coords):
            for check_antenna in coords[i + 1:]: 
                antinodes.add(main_antenna)
                antinodes.add(check_antenna)
                antenna_dist = tuple(x - y for x, y in zip(main_antenna, check_antenna)) 
                antinode = tuple(x + y for x, y in zip(main_antenna, antenna_dist))  
                while(validate_antinode(antinode, boundaries)):
                    antinodes.add(antinode)
                    antinode = tuple(x + y for x, y in zip(antinode, antenna_dist))  
                antinode = tuple(x - y for x, y in zip(main_antenna, antenna_dist))  
                while(validate_antinode(antinode, boundaries)):
                    antinodes.add(antinode)
                    antinode = tuple(x - y for x, y in zip(antinode, antenna_dist)) 
    return len(antinodes)


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")