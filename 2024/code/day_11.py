from functools import cache

if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input(): 
    with open(getFilePath()) as f:   
        return list(map(int, f.readline().strip().split(" "))) 

@cache
def check_stones(val, it_count):
    if it_count == 0:
        return 1
    
    if val == 0: 
        return check_stones(1, it_count - 1)

    rock_str = str(val)
    num_digits = len(rock_str)

    if(num_digits % 2 == 0):
        half = num_digits // 2 
        return check_stones(int(rock_str[:half]), it_count - 1) + \
            check_stones(int(rock_str[half:]), it_count - 1)  
    else: return check_stones(val * 2024, it_count - 1)


def task_one(): 
    c = 0
    for stone in parse_input() : 
        c += check_stones(stone, 25) 
    return c


def task_two():  
    c= 0
    for stone in parse_input() : 
        c += check_stones(stone, 75)
    return c


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")