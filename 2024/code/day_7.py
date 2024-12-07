import re 
import time
if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input():  
    target_values = []
    with open(getFilePath()) as f:    
        for line in f.readlines():
            nums = list(map(int, re.findall("[0-9]+", line)))
            target_values.append((nums[0], nums[1:])) 
    return target_values


def is_solvable_one(target, curr_val, arr):
    if arr == []:
        if target == curr_val: return 1
        return 0

    return 1 if is_solvable_one(target, curr_val * arr[0], arr[1:])\
        else is_solvable_one(target, curr_val + arr[0], arr[1:])

    
def task_one():
    target_values = parse_input() 
    calibration_result = 0
    for target, values in target_values: 
        if(is_solvable_one(target, values[0], values[1:])): 
            calibration_result += target
    return calibration_result


def is_solvable_two(target, current, arr):
    if arr == []:
        if current == target: return 1
        return 0
 
    if(is_solvable_two(target, current + arr[0], arr[1:])): return 1
    if(is_solvable_two(target, current * arr[0], arr[1:])): return 1
    return is_solvable_two(target,  int(str(current) + str(arr[0])), arr[1:])

     
def task_two(): 
    start = time.time()
    target_values = parse_input() 
    calibration_result = 0
    for target, values in target_values: 
        if is_solvable_two(target, values[0], values[1:]): 
            calibration_result += target  
    print(time.time() - start)
    return calibration_result 


print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")

