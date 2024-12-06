if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input(): 
    num_to_nums_before = {}
    with open(getFilePath()) as f:  
        line = f.readline() 
        while(line != "\n"):
            x, y = line.strip().split("|")
            line = f.readline()  
            if(y in num_to_nums_before): 
                num_to_nums_before[y].add(x)
            else: num_to_nums_before[y] = set([x])
        return ([line.strip().split(",")[::-1] for line in f.readlines()], 
                num_to_nums_before)


def categorise_updates(updates, nums_order, update_flag): 
    invalid_updates = []
    for update in updates: 
        num_set = set()
        for num in update: 
            if(len(num_set.intersection(nums_order.get(num, set())))): 
                invalid_updates.append(update)
                break
            num_set.add(num) 
    if(update_flag):
        return [i for i in updates if i not in invalid_updates]
    return invalid_updates


def taskOne():
    updates, nums_order = parse_input()  
    update_sum = 0
    valid_updates = categorise_updates(updates, nums_order, True) 
    for update in valid_updates:
        update_sum += int(update[len(update) // 2])
    return update_sum


def taskTwo(): 
    updates, nums_order = parse_input()  
    update_sum = 0
    invalid_updates = categorise_updates(updates, nums_order, False)  
    for update in invalid_updates: 
        num_set = set() 
        fixed_update = []
        for num in update:
            conflicts = num_set.intersection(nums_order.get(num, set()))
            if(len(conflicts) == 0): 
                fixed_update.append(num) 
            else:
                idx = float("inf")
                for conflict in conflicts:
                    k = min(fixed_update.index(conflict), idx)      
                fixed_update.insert(idx, num)
            num_set.add(num) 
        update_sum += int(fixed_update[len(fixed_update) // 2])
    return update_sum

            
print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")