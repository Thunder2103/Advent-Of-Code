if(__name__ == "__main__"):
    from puzzle_input import getFilePath
else:
    from .puzzle_input import getFilePath


def parse_input(): 
    with open(getFilePath()) as f:
        return [line.strip() for line in f.readlines()]


def check_left(row, idx): 
    return 1 if row[idx:idx+4] == "XMAS" else 0 


def check_right(row, idx):
    return 1 if row[idx-3:idx+1][::-1] == "XMAS" else 0 


def check_down(word_search, i, j):
    word = "".join([row[j] for row in word_search[i:i+4]]) 
    return 1 if word == "XMAS" else 0 


def check_up(word_search, i, j):
    word = "".join([row[j] for row in word_search[i-3:i+1]][::-1]) 
    return 1 if word == "XMAS" else 0


def check_diagonals_up(word_search, i, j, row_len): 
    xmas_count = 0
    diagonal_text = ""
    idx = j - 3
    for row in word_search[i-3:i+1]:  
        if(idx < 0 or idx == row_len): break 
        diagonal_text += row[idx]
        idx += 1 
    if(diagonal_text[::-1] == "XMAS"): xmas_count += 1 

    idx = j + 3
    diagonal_text = ""
    for row in word_search[i-3:i+1]:
        if(idx >= row_len): break 
        diagonal_text += row[idx]
        idx -= 1 
    if(diagonal_text[::-1] == "XMAS"): xmas_count += 1
    return xmas_count


def check_diagonals_down(word_search, i, j, row_len): 
    xmas_count = 0
    idx = j 
    diagonal_text = ""
    for row in word_search[i:i+4]:  
        if(idx == row_len): break 
        diagonal_text += row[idx]
        idx += 1 
    if(diagonal_text == "XMAS"): xmas_count += 1 

    idx = j 
    diagonal_text = ""
    for row in word_search[i:i+4]:
        if(idx < 0): break 
        diagonal_text += row[idx]
        idx -= 1
    if(diagonal_text == "XMAS"): xmas_count += 1 
    return xmas_count


def taskOne():
    word_search = parse_input()
    row_len = len(word_search[0])
    xmas_count = 0
    for i, row in enumerate(word_search):
        for j, char in enumerate(row):
            if(char == "X"):
                xmas_count += check_left(row, j)
                xmas_count += check_right(row, j)
                xmas_count += check_up(word_search, i, j)
                xmas_count += check_down(word_search, i, j)
                xmas_count += check_diagonals_up(word_search, i, j, row_len)
                xmas_count += check_diagonals_down(word_search, i, j, row_len)
    return xmas_count


def check_diagonal_mas(word_search, i, j):  
    mas_count = 0
    left_diag = word_search[i + 1][j + 1] + word_search[i - 1][j - 1]
    right_diag = word_search[i + 1][j - 1] + word_search[i - 1][j + 1] 
    if(left_diag == "MS" or left_diag == "SM"): mas_count += 1 
    if(right_diag == "MS" or right_diag == "SM"): mas_count += 1 
    return 1 if mas_count == 2 else 0

    
def taskTwo():
    word_search = parse_input() 
    mas_count = 0
    for i, row in enumerate(word_search[1:-1]):
        for j, char in enumerate(row[1:-1]): 
            if char == "A":
                mas_count += check_diagonal_mas(word_search, i + 1, j + 1) 
    return mas_count


print(f"Part 1: {taskOne()}")
print(f"Part 2: {taskTwo()}")