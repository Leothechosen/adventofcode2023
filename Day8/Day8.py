# 10:16 PM
# 10:34 PM P1 finished
# 10:40 PM P2 finished

from math import lcm

def part1(data):
    instructions = data[0]
    network = data[2:]
    network_map = {}
    start = "AAA"
    for line in network: 
        node = line.split(" = ")[0]
        left, right = line.split("(")[1].split(")")[0].split(", ")
        network_map[node] = {'L': left, 'R': right}
    i = 0
    while True:
        instruction = instructions[i % len(instructions)]
        start = network_map[start][instruction]
        if start == "ZZZ":
            return i+1
        i += 1

def part2(data):
    instructions = data[0]
    network = data[2:]
    network_map = {}
    for line in network: 
        node = line.split(" = ")[0]
        left, right = line.split("(")[1].split(")")[0].split(", ")
        network_map[node] = {'L': left, 'R': right}
    steps = []
    for node in network_map:
        if node[-1] == "A":
            start = node
            i = 0
            while True:
                instruction = instructions[i % len(instructions)]
                start = network_map[start][instruction]
                if start[-1] == "Z":
                    steps.append(i+1)
                    break
                i += 1
    return lcm(*steps)
        
if __name__ == "__main__":
    with open('Day8\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")