if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input():
    levels = []
    with open(getFilePath()) as f:
        for line in f.readlines(): 
            levels.append(list(map(int, line.strip().split())))  
        return levels


def evaulate_level(level, n):
    # Stores if a pair of numbers are increasing or decreasing
    nums_increasing = [False for _ in range(n)] 
    # Used to evaluate of each pair of numbers is safe
    is_level_safe = [False for _ in range(n - 1)]
    for i in range(n - 1):
            # Difference between pair of nums
            diff = level[i] - level[i + 1] 
            # If difference is strictly positive, the pair is increasing 
            if(diff > 0): nums_increasing[i] = True 
            # Check if difference between nums is between 1 - 3 (inclusive) 
            # And if pair of nums is follwing the same pattern as last pair
            if((abs(diff) >= 1 and abs(diff) <= 3) and 
               (i == 0 or nums_increasing[i] == nums_increasing[i - 1])): 
                # Set pair of nums to safe
                is_level_safe[i] = True  
    # Return 1 if level is safe, else 0
    if(all(is_level_safe)): return 1
    else: return 0


def task_one():
    levels = parse_input()
    safe_levels = 0 
    for level in levels:
        n = len(level)
        # Add one if level is safe, otherwise add 0
        safe_levels += evaulate_level(level, n)
    return safe_levels


def task_two():
    levels = parse_input()
    safe_levels = 0  
    for level in levels:
        n = len(level)        
        # If level is safe, increment counter
        if(evaulate_level(level, n)):
            safe_levels += 1 
            continue
        # Iterate through each number
        # Check if level is safe after removing each number
        for i in range(n):
            # Check level is safe after removing current number 
            if(evaulate_level(level[0:i] + level[i + 1:], n - 1) ):
                safe_levels += 1
                break 
    return safe_levels

print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")