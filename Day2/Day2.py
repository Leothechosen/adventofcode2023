#https://adventofcode.com/2023/day/2

def part1(data):
    def cube_checks(round):
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for color in counts:
            if color in round:
                counts[color] = int(round.split(f" {color}")[0].split(" ")[-1])
        return counts
    
    ans = 0
    for game_id, line in enumerate(data, start=1):
        game = line.split(": ")[1].split("; ")
        colors = {'red': {'max': 0, 'limit': 12},
              'green': {'max': 0, 'limit': 13},
              'blue': {'max': 0, 'limit': 14}}
        for round in game:
            counts = cube_checks(round)
            for color in colors:
                if counts[color] > colors[color]['max']:
                    colors[color]['max'] = counts[color]
        for color in colors:
            color_count, color_limit = colors[color].values()
            if color_count > color_limit:
                break
        else:
            ans += game_id
    return ans

def part2(data):
    def cube_checks(round):
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for color in counts:
            if color in round:
                counts[color] = int(round.split(f" {color}")[0].split(" ")[-1])
        return counts
    
    ans = 0
    for game_id, line in enumerate(data, start=1):
        game = line.split(": ")[1].split("; ")
        colors = {'red': 0,
              'green': 0,
              'blue': 0}
        for round in game:
            counts = cube_checks(round)
            for color in colors:
                if counts[color] > colors[color]:
                    colors[color] = counts[color]
        power = 1
        for count in colors.values():
            power *= count
        ans += power
    return ans

if __name__ == "__main__":
    with open('Day2\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")