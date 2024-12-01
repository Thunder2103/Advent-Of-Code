if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


# Processes the input as needed for each task
def get_file_input():
    left_list = [] 
    right_list = []

    with open(getFilePath()) as f:
        for line in f.readlines(): 
            nums = line.strip().split("  ")
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1])) 
    
    return left_list, right_list

def taskOne(): 
    left_list, right_list = get_file_input() 
    
    # Sort both lists
    left_list.sort()
    right_list.sort() 
    total = 0
    
    for left_num, right_num in zip(left_list, right_list): 
        # Get difference for each pair, add to total
        total += abs(left_num - right_num)
    return total

def taskTwo():
    left_list, right_list = get_file_input()    
    # Map left list numbers to occurences in right list
    num_to_occur = {val : 0 for val in left_list} 
    # Get occurence of each number in rigt list
    for num in right_list:
        if num in num_to_occur: 
            num_to_occur[num] += 1
    
    total = 0
    for num in left_list:  
        # Add number * occurences in right list
        total += num * num_to_occur[num]    
    return total

print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")