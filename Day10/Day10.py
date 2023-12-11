import sys
def part1(data):
    class Walker():
        def __init__(self, data):
            sys.setrecursionlimit(100000)
            self.start = None
            self.data = data
            self.grid = []
            self.loop = []
            self.coord_loop = []
            self.create_grid()
            self.pipe_dir = {
                "S": ["N", "S", "E", "W"],
                "|": ["N", "S"],
                "-": ["E", "W"],
                "L": ["N", "E"],
                "J": ["N", "W"],
                "7": ["S", "W"],
                "F": ["S", "E"],
            }
            self.directions = {
                "N": (-1, 0),
                "S": (1, 0),
                "W": (0, -1),
                "E": (0, 1)
            }
            self.opp_directions = {
                "N": "S",
                "S": "N", 
                "E": "W",
                "W": "E"
            }
            self.prev_pos = None
            self.walk(self.start)

        def create_grid(self):
            for y, line in enumerate(self.data):
                self.grid.append([pipe for pipe in line])
                if "S" in line:
                    self.start = (y, line.index("S"))
    
        def walk(self, position):
            #print(self.loop)
            y, x = position               
            pipe = self.grid[y][x]
            adj = {}
            for adj_dir, (dy, dx) in self.directions.items():
                if y+dy < 0 or x+dx < 0 or y+dy >= len(self.grid) or x+dx >= len(self.grid):
                    adj[adj_dir] = None
                else:
                    adj[adj_dir] = self.grid[y+dy][x+dx]
            valid_dir = []
            for direction, adj_pipe in adj.items():
                if adj_pipe == "." or adj_pipe is None:
                    continue
                dy, dx = self.directions[direction]
                if (dy+y, dx+x) == self.prev_pos:
                    continue
                if self.opp_directions[direction] in self.pipe_dir[adj_pipe] and direction in self.pipe_dir[pipe]:
                    valid_dir.append((adj_pipe, (dy+y, dx+x)))
            if len(valid_dir) == 0:
                self.loop.pop(-1)
                return
            for adj_pipe, new_position in valid_dir:
                self.prev_pos = position
                self.loop.append(adj_pipe)
                self.coord_loop.append(new_position)
                if adj_pipe == "S":
                    print(self.loop)
                    print(len(self.loop)/2)
                    exit()
    
                self.walk((new_position))
    Walker(data)

def part2(data):
    class Walker():
        def __init__(self, data):
            sys.setrecursionlimit(100000)
            self.end_found = False
            self.start = None
            self.data = data
            self.grid = []
            self.loop = []
            self.coord_loop = []
            self.create_grid()
            self.pipe_dir = {
                "S": ["N", "S", "E", "W"],
                "|": ["N", "S"],
                "-": ["E", "W"],
                "L": ["N", "E"],
                "J": ["N", "W"],
                "7": ["S", "W"],
                "F": ["S", "E"],
            }
            self.directions = {
                "N": (-1, 0),
                "S": (1, 0),
                "W": (0, -1),
                "E": (0, 1)
            }
            self.opp_directions = {
                "N": "S",
                "S": "N", 
                "E": "W",
                "W": "E"
            }
            self.prev_pos = None
            self.walk(self.start)
            print(len(self.loop)/2)
            self.create_new_grid()
            self.count_inside()
            print(self.cnt)

        def create_grid(self):
            for y, line in enumerate(self.data):
                self.grid.append([pipe for pipe in line])
                if "S" in line:
                    self.start = (y, line.index("S"))
    
        def walk(self, position):
            #print(self.loop)
            y, x = position               
            pipe = self.grid[y][x]
            adj = {}
            for adj_dir, (dy, dx) in self.directions.items():
                if y+dy < 0 or x+dx < 0 or y+dy >= len(self.grid) or x+dx >= len(self.grid):
                    adj[adj_dir] = None
                else:
                    adj[adj_dir] = self.grid[y+dy][x+dx]
            valid_dir = []
            for direction, adj_pipe in adj.items():
                if adj_pipe == "." or adj_pipe is None:
                    continue
                dy, dx = self.directions[direction]
                if (dy+y, dx+x) == self.prev_pos:
                    continue
                if self.opp_directions[direction] in self.pipe_dir[adj_pipe] and direction in self.pipe_dir[pipe]:
                    valid_dir.append((adj_pipe, (dy+y, dx+x)))
            if len(valid_dir) == 0:
                self.loop.pop(-1)
                return
            for adj_pipe, new_position in valid_dir:
                if self.end_found:
                    return
                self.prev_pos = position
                self.loop.append(adj_pipe)
                self.coord_loop.append(new_position)
                if adj_pipe == "S":
                    self.end_found = True
                    return 
                self.walk((new_position))

        def create_new_grid(self):
            new_grid = []
            for y, line in enumerate(self.grid):
                new_line = []
                for x, pipe in enumerate(line):
                    if (y, x) not in self.coord_loop:
                        new_line.append("X")
                    elif pipe == "S":
                        new_line.append("|")
                    else:
                        new_line.append(pipe)
                new_grid.append(new_line)
            self.new_grid = new_grid
        
        def count_inside(self):
            self.cnt = 0
            for y, line in enumerate(self.new_grid):
                for x, pipe in enumerate(line):
                    if pipe != "X":
                        continue
                    cross = 0
                    for z in line[0:x]:
                        #print(z)
                        if z in ["|", "J", "L"]:
                            cross += 1
                    if cross % 2 == 1:
                        self.cnt += 1
    Walker(data)

if __name__ == "__main__":
    with open('Day10\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    #print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")