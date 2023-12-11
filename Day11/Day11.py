import itertools

def part1(data):
    grid = []
    star_locations = []
    for line in data:
        if list(set(line)) == ["."]:
            grid.append(["."] * len(line))
        grid.append(list(line))
    col_to_add = []
    for idx in range(len(grid[0])):
        col = [line[idx] for line in grid]
        if list(set(col)) == ["."]:
            col_to_add.append(idx)
    for idx in col_to_add:
        idx = idx + col_to_add.index(idx)
        for line_idx in range(len(grid)):
            grid[line_idx].insert(idx, ".")

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                star_locations.append((y, x))
    
    pairs = itertools.combinations(star_locations, 2)
    ans = 0
    for (y1, x1), (y2, x2) in pairs:
        side_a = abs(y1-y2)
        side_b = abs(x1-x2)
        ans += side_a + side_b
    return ans

def part2(data):
    star_locations = []
    row_to_exp = []
    for i, line in enumerate(data):
        if list(set(line)) == ["."]:
            row_to_exp.append(i)
    col_to_exp = []
    for i in range(len(data[0])):
        col = [line[i] for line in data]
        if list(set(col)) == ["."]:
            col_to_exp.append(i)
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                star_locations.append((y, x))
    
    pairs = itertools.combinations(star_locations, 2)
    ans = 0
    for (y1, x1), (y2, x2) in pairs:
        row_exp = 0
        col_exp = 0
        for row_num in row_to_exp:
            if row_num in range(y1, y2):
                row_exp += 999999
            elif row_num in range(y2, y1):
                row_exp += 999999
        for col_num in col_to_exp:
            if col_num in range(x1, x2):
                col_exp += 999999
            if col_num in range(x2, x1):
                col_exp += 999999
        side_a = abs(y1-y2)+row_exp
        side_b = abs(x1-x2)+col_exp
        ans += side_a + side_b
    return ans

def part2short(data):
    #Done after the fact for fun. Same method as above, just sent into list comprehension hell
    star_locations = [(y, x) for y, line in enumerate(data) for x, char in enumerate(line) if char == "#"]    
    empty_rows = [i for i, line in enumerate(data) if list(set(line)) == ["."]]
    empty_cols = [i for i in range(len(data[0])) if list(set([line[i] for line in data])) == ["."]]
    pairs = itertools.combinations(star_locations, 2)
    return sum([abs(y1-y2)+sum([999999 for row_num in empty_rows if row_num in range(*sorted([y1, y2]))])+abs(x1-x2)+sum([999999 for col_num in empty_cols if col_num in range(*sorted([x1, x2]))]) for (y1, x1), (y2, x2) in pairs])

if __name__ == "__main__":
    with open('Day11\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2short(data)}")