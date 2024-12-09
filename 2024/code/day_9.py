if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath

import time

def parse_input():  
        id_count, pos = 0, 0 
        id_size = {}
        free_space = []
        is_file = True
        with open(getFilePath()) as f:
             for line in f.readlines():
                for num in line:
                    if(is_file):
                        id_size[id_count] = [int(num), []]
                        id_count += 1
                    for _ in range(int(num)): 
                        if(not is_file): free_space.append(pos) 
                        else: id_size[id_count - 1][1].append(pos)
                        pos += 1 
                    is_file = not is_file 
        return (id_size, free_space, id_count - 1)


def calc_check_sum(file_spaces): 
    check_sum = 0 
    for k, v in file_spaces.items():
        for num in v[1]: 
            check_sum += k * num 
    return check_sum


def task_one():
    file_spaces, free_spaces, curr_id = parse_input()
    space_idx, id_idx = 0, file_spaces[curr_id][0] - 1
    furthest_file = file_spaces[curr_id][1][id_idx]
    while(furthest_file > free_spaces[space_idx]): 
        free_spaces.append(furthest_file)
        file_spaces[curr_id][1][id_idx] = free_spaces[space_idx]
        space_idx +=1
        id_idx -= 1 
        if(id_idx < 0): 
            curr_id -= 1 
            id_idx = file_spaces[curr_id][0] - 1 
        furthest_file = file_spaces[curr_id][1][id_idx]
    return calc_check_sum(file_spaces)


def process_free_spaces(free_spaces):
    split_free_spaces = []
    l, r, n = 0, 1, len(free_spaces)
    while(r <= n):
        if(r == n or free_spaces[r] - free_spaces[r - 1] != 1): 
            split_free_spaces.append(free_spaces[l:r])
            l = r  
        r += 1  
    return split_free_spaces


def get_leftmost_free(split_free_spaces, file_info):
    file_size, file_loc = file_info
    for idx, segment in enumerate(split_free_spaces):
        if(len(segment) >= file_size and segment[0] < file_loc[0]):
            return (idx, segment)
    return (-1, []) 


def task_two():  
    file_spaces, free_spaces, _ = parse_input() 
    s = time.time()
    split_free_spaces = process_free_spaces(free_spaces)
    for id in list(file_spaces.keys())[::-1]:
        idx, free_loc = get_leftmost_free(split_free_spaces, file_spaces[id])
        if(free_loc == []): continue
        spaces_needed = free_loc[:file_spaces[id][0]] 
        file_spaces[id][1] = spaces_needed
        if(spaces_needed == free_loc):
            split_free_spaces.pop(idx)
        else: split_free_spaces[idx] = free_loc[file_spaces[id][0]:]  
    return calc_check_sum(file_spaces) 
    
        
print(f"Part 1: {task_one()}")
print(f"Part 2: {task_two()}")