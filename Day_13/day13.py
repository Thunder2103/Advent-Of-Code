#My solutions are getting longer and a lot less faster
import ast
import copy

def eval_num(left, right):
    if(left < right):
        return 1
    if(left > right):
        return 0
    return 2

def handle_lists(left, right):
    if((type(left)) is list and (type(right)) is list):
        if(len(left) == 0 and len(right) == 0): return 2 
        if(len(left) > 0 and len(right) == 0): return 0 
        if(len(left) == 0 and len(right) > 0): return 1
        result = handle_lists(left[0], right[0])
        if(result == 1 or result == 0):
            return result
        else:
            left.pop(0)
            right.pop(0)
            return handle_lists(left, right)
    
    if((type(left)) is int and (type(right)) is list):
        return handle_lists([left], right)
    
    if((type(left)) is list and (type(right)) is int):
        return handle_lists(left, [right])
    
    if((type(left)) is int and (type(right)) is int):
        return eval_num(left, right)
    
indice = 0
sum = 0

with open("day13.txt") as f:
    for lhs in f: 
        indice+=1
        
        lhs = lhs.strip()
        if(lhs == ""):
            indice-=1
            continue
        
        lhs = ast.literal_eval(lhs)

        rhs = f.readline().strip() 
        rhs = ast.literal_eval(rhs) 

        if(len(lhs) == 0 and len(rhs) > 0): 
            sum += indice
            continue
        if(len(lhs) > 0 and len(rhs) == 0):
            continue
        if(len(lhs) == 0 and len(rhs) == 0):
            continue
        while(lhs and rhs):
            if(type(lhs[0]) is int and (type(rhs[0])is int)):
                result = eval_num(lhs[0], rhs[0])
                if(result == 1):
                    sum += indice
                    break
                if(result == 0): break
                if(result == 2):
                    if(len(lhs) > 1 and len(rhs) == 1): break 
                    if(len(lhs) == 1 and len(rhs) > 1):
                        sum +=indice
                        break
                    if(len(lhs) == 1 and len(rhs) == 1):
                        lhs.pop(0)
                        rhs.pop(0)
                        continue
            if(type(lhs[0]) is list or type(rhs[0]) is list):
           
                result = handle_lists(lhs[0], rhs[0])
                if(result == 1):
                    sum += indice
                    break 
                if(result == 0):
                    break 
                
    
            lhs.pop(0)
            rhs.pop(0)
            
print("Solution 1", sum)

array = [[2], [6]]
order = 0
with open("day13.txt") as f:
    for lhs in f: 
        order = 0
        lhs = lhs.strip()
        if(lhs == ""):
            continue
        lhs = ast.literal_eval(lhs)
        if(len(lhs) == 0): 
            array.insert(0, lhs)
            continue
        lhs_c = copy.deepcopy(lhs)
        i = 0
        while(i < len(array)):
            if(len(array[i]) == 0):
                i +=1
                continue
            rhs_c = copy.deepcopy(array[i])
            while(lhs_c and rhs_c):
                if(type(lhs_c[0]) is int and (type(rhs_c[0])is int)):
                    result = eval_num(lhs_c[0], rhs_c[0])
                    if(result == 1):
                        order = 1
                        array.insert(i, lhs)
                        break
                    if(result == 0): break
                    if(result == 2):
                        if(len(lhs_c) > 1 and len(rhs_c) == 1): break 
                        if(len(lhs_c) == 1 and len(rhs_c) > 1):
                            order = 1
                            array.insert(i, lhs)
                            break
                        if(len(lhs_c) == 1 and len(rhs_c) == 1):
                            lhs_c.pop(0)
                            rhs_c.pop(0)
                            continue
                if(type(lhs_c[0]) is list or type(rhs_c[0]) is list):
                    result = handle_lists(lhs_c[0], rhs_c[0])
                    if(result == 1):
                        order = 1
                        array.insert(i, lhs)
                        break 
                    if(result == 0): break 
                lhs_c.pop(0)
                rhs_c.pop(0)
            if(order == 1):
                break
            if(i == len(array) - 1):
                array.append(lhs)      
                break 
            lhs_c = copy.deepcopy(lhs)
            i+=1
            
print("Solution 2", (array.index([2]) + 1) * (array.index([6]) + 1))



